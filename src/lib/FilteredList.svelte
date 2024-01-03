<script>
  import Checkbox from "./Checkbox.svelte";
  import Card from "./Card.svelte";
  import RadioButtons from "./RadioButtons.svelte";

  import { onMount } from "svelte";
  import { fade, slide, scale } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { csv, autoType } from "d3";

  const icons = {
    Cotton: "cotton.svg",
    Elastane: "elastane.svg",
    Linen: "linen.svg",
    Polyamide: "nylon.svg",
    Polyester: "polyester.svg",
    Viscose: "viscose.svg",
  };

  // Synthetic object for "Others"
  const othersMaterial = { Name: "Others" };

  const radioOptions = [
    { value: "all", label: "All" },
    { value: "1738", label: "T-Shirts" },
    { value: "1733", label: "Blouses" },
    { value: "2223", label: "Tops" },
    { value: "1779", label: "Tank Tops & Camis" },
  ];

  let windowWidth = window.innerWidth;

  function handleResize() {
    windowWidth = window.innerWidth;
    if (windowWidth < 576) {
      selectedType = "all";
    }
  }

  let materials = [];
  let items = [];
  let filteredItems = [];
  let filteredMaterials = [];
  let biodegradableMaterials = [];
  let checkboxStates = {};
  let selectedType = "all";
  let itemsPerPage = 100;
  let page = 1;
  let totalPages = 1;
  let listElement;

  // Reactive declaration to update filteredMaterials
  $: if (materials.length > 0) {
    filteredMaterials = materials.filter((material) => icons[material.Name]);
  }

  $: if (materials.length > 0) {
    biodegradableMaterials = materials
      .filter((material) => material.Biodegradable)
      .map((material) => material.Name);
  }

  $: totalPages = Math.ceil(filteredItems.length / itemsPerPage);

  $: paginatedItems = filteredItems.slice(
    (page - 1) * itemsPerPage,
    page * itemsPerPage
  );

  onMount(async () => {
    window.addEventListener("resize", handleResize);

    try {
      materials = await csv("./data/materials.csv", autoType);
      items = await csv("./data/items.csv", autoType);

      // Filter materials where any matching item in 'items' has a value > 0
      materials = materials.filter((material) => {
        return items.some((item) => item[material.Name] > 0);
      });

      // Initialize checkboxStates based on loaded materials
      for (const material of materials) {
        checkboxStates[material.Name] = material.Checked;
      }

      // Add a special "Others" entry
      checkboxStates["Others"] = false;

      items.forEach((item, index) => {
        const materials = item.Composition.split(",");
        const biodegradableCount = materials.filter((material) =>
          biodegradableMaterials.some((biodegradableMaterial) =>
            material.includes(biodegradableMaterial)
          )
        ).length;

        items[index].isBiodegradable = materials.length === biodegradableCount;
      });

      // Trigger reactive update
      filteredItems = [...items];
    } catch (error) {
      console.error(error);
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const backlight = document.querySelector(".backlight");
        if (entry.isIntersecting) {
          backlight.style.opacity = 1;
        } else {
          backlight.style.opacity = 0;
        }
      });
    });

    observer.observe(listElement);
  });

  // Updated reactive statement for dynamic filtering
  $: {
    if (materials.length) {
      let others = [];
      if (checkboxStates["Others"]) {
        // Does not contain any of the main materials
        others = items.filter(
          (item) =>
            !filteredMaterials.some((material) => {
              const hasMaterial = item[material.Name] > 0;
              return hasMaterial;
            })
        );
      }

      // Contains exactly those materials
      let strictly = items.filter((item) =>
        materials.every((material) => {
          const isSelected = checkboxStates[material.Name];
          const hasMaterial = item[material.Name] > 0;
          return isSelected ? hasMaterial : !hasMaterial;
        })
      );

      // Contains any of those materials
      let loosely = items.filter((item) =>
        materials.some((material) => {
          const isSelected = checkboxStates[material.Name];
          const hasMaterial = item[material.Name] > 0;
          return isSelected && hasMaterial;
        })
      );

      filteredItems = [...new Set([...strictly, ...loosely, ...others])];

      filteredItems.sort((a, b) => {
        if (a.isBiodegradable && !b.isBiodegradable) {
          return -1;
        } else if (!a.isBiodegradable && b.isBiodegradable) {
          return 1;
        } else {
          return 0;
        }
      });

      if (selectedType !== "all") {
        filteredItems = filteredItems.filter(
          (item) => item.Type === parseInt(selectedType)
        );
      }

      // Reset page number
      page = 1;
    }
  }

  function prevPage() {
    if (page > 1) {
      page--;
    }
  }

  function nextPage() {
    if (page < totalPages) {
      page++;
    }
  }
</script>

<!-- Dynamic Checkbox filters -->
<form action="return false">
  <div class="checkboxes">
    {#each filteredMaterials as material}
      <Checkbox
        {material}
        icon={icons[material.Name]}
        bind:checked={checkboxStates[material.Name]}
      />
    {/each}

    <Checkbox
      material={othersMaterial}
      bind:checked={checkboxStates["Others"]}
    />
  </div>
</form>

<ul bind:this={listElement} data-count={paginatedItems.length}>
  {#if windowWidth >= 576}
    <li class="category-filter">
      <form action="return false">
        <h4>Women Top&nbsp;Rated</h4>
        <RadioButtons {radioOptions} bind:selectedType />
      </form>
    </li>
  {/if}
  {#if paginatedItems.length === 0}
    <li class="no-items">
      <p>Oh no! Try picking another material ↑</p>
    </li>
  {/if}
  {#each paginatedItems as item (item.SKU)}
    <li animate:flip={{ duration: 400 }} transition:fade={{ duration: 100 }}>
      <Card {item} {biodegradableMaterials} />
    </li>
  {/each}
</ul>

<footer>
  <p>
    <output>{filteredItems.length.toLocaleString("en-US")}</output>
    <span>{filteredItems.length === 1 ? "item" : "items"} found</span>
  </p>

  <nav>
    <button on:click={prevPage}>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="feather feather-chevron-left"
        ><polyline points="15 18 9 12 15 6"></polyline></svg
      >
      <span class="screen-reader">Previous</span>
    </button>
    <span>Page {page} of {totalPages}</span>
    <button on:click={nextPage}>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="feather feather-chevron-right"
        ><polyline points="9 18 15 12 9 6"></polyline></svg
      >
      <span class="screen-reader">Next</span>
    </button>
  </nav>
</footer>

<style>
  form {
    width: 100%;
  }
  .category-filter {
    display: flex;
    width: var(--card-width);
    background: #fff;
    border-radius: 8px;
    min-height: 100%;
    flex-shrink: 0;
  }
  .category-filter form {
    min-height: calc(388px + 1px);
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .category-filter form h4 {
    font-size: 24px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    text-wrap: pretty;
    margin-bottom: 1em;
  }
  .no-items {
    min-height: calc(388px + 1px);
    width: calc(100% - 1px);
    background: #494b5310;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    height: 100%;
    align-items: center;
  }
  .no-items p {
    height: fit-content;
  }
  .checkboxes {
    display: flex;
    justify-content: start;
    gap: 16px;
    flex-wrap: wrap;
    width: 100%;
    padding: 40px;
  }
  ul {
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
    gap: 24px;
    list-style: none;
    padding: 40px 24px;
    background: #f5f2ed;
    width: 100%;
    min-height: 108px;
  }
  ul[data-count="0"] {
    flex-wrap: nowrap;
  }
  footer {
    padding: 40px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  nav {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  nav button {
    color: inherit;
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
    appearance: none;
    box-shadow: none;
    height: 32px;
    width: 32px;
    border: 1px solid #494b53;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    transition: all 0.4s;
  }
  nav button:hover {
    background: #494b53;
    color: white;
  }
  .screen-reader {
    clip: rect(0 0 0 0);
    clip-path: inset(50%);
    height: 1px;
    overflow: hidden;
    position: absolute;
    white-space: nowrap;
    width: 1px;
  }
  footer p {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1em;
  }
  footer output {
    font-family: "Dela Gothic One";
    font-size: 40px;
  }
  @media (max-width: 864px) {
    .checkboxes {
      gap: 8px;
      padding: 20px;
    }
    ul {
      gap: 16px;
      padding: 40px 16px;
    }
  }
</style>
