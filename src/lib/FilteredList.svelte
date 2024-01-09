<script>
  import Checkbox from "./Checkbox.svelte";
  import Card from "./Card.svelte";
  import RadioButtons from "./RadioButtons.svelte";

  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
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

  // Function to check if the browser is Safari
  function isSafari() {
    return /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
  }

  const onSafari = isSafari();

  let materials = [];
  let items = [];
  let filteredItems = [];
  let filteredMaterials = [];
  let checkboxStates = {};
  let selectedType = "all";
  let itemsPerPage = onSafari ? 25 : 100;
  let page = 1;
  let totalPages = 1;
  let listElement;

  // Reactive declaration to update filteredMaterials
  $: if (materials.length > 0) {
    filteredMaterials = materials.filter((material) => icons[material.Name]);
  }

  $: totalPages = Math.ceil(filteredItems.length / itemsPerPage) || 1;

  $: paginatedItems = filteredItems.slice(
    (page - 1) * itemsPerPage,
    page * itemsPerPage
  );

  onMount(async () => {
    window.addEventListener("resize", handleResize);

    try {
      items = await csv("./data/items.csv", autoType);

      items = items.map((d) => {
        d.Biodegradable = d.Biodegradable === "True";
        return d;
      });

      materials = await csv("./data/materials.csv", autoType);

      materials = materials.map((d) => {
        d.Biodegradable = d.Biodegradable === "True";
        d.Checked = d.Checked === "True";
        return d;
      });

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
      // Filter by type
      let itemsClone = items.filter((item) => {
        if (selectedType === "all") {
          return true;
        } else {
          return item.Type === parseInt(selectedType);
        }
      });

      let others = [];

      if (checkboxStates["Others"]) {
        // Does not contain any of the main materials
        others = itemsClone.filter(
          (item) =>
            !filteredMaterials.some((material) => {
              const hasMaterial = item[material.Name] > 0;
              return hasMaterial;
            })
        );
      }

      // Contains any of those materials
      const loosely = itemsClone.filter((item) =>
        materials.some((material) => {
          const isSelected = checkboxStates[material.Name];
          const hasMaterial = item[material.Name] > 0;
          return isSelected && hasMaterial;
        })
      );

      filteredItems = [...new Set([...loosely, ...others])].sort((a, b) => {
        // Sort by most biodegradable first
        const BiodegradableRatioDiff =
          b.BiodegradableRatio - a.BiodegradableRatio;

        if (BiodegradableRatioDiff === 0) {
          // Break tie by prioritizing items made from less materials
          return a.MaterialCount - b.MaterialCount;
        }

        return BiodegradableRatioDiff;
      });

      // Reset page number
      page = 1;
    }
  }
  function setPage(change) {
    if (typeof change === "number") {
      page = change;
    } else {
      if (change === "next" && page < totalPages) {
        page++;
      } else if (change === "prev" && page > 1) {
        page--;
      }
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
      icon=""
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
      <Card {item} {materials} />
    </li>
  {/each}
</ul>

<footer>
  <p>
    {#if filteredItems.length > 0}
      Showing
      {(page - 1) * itemsPerPage + 1}–{page * itemsPerPage >
      filteredItems.length
        ? (page - 1) * itemsPerPage + (filteredItems.length % itemsPerPage)
        : page * itemsPerPage} of
    {/if}
    {filteredItems.length.toLocaleString("en-US")}
    {filteredItems.length === 1 ? "result" : "results"}
  </p>
  <nav>
    <button on:click={() => setPage("prev")}>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.5"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="feather feather-chevron-left"
        ><polyline points="15 18 9 12 15 6"></polyline></svg
      >
      <span class="screen-reader">Previous</span>
    </button>

    {#if windowWidth >= 576 && totalPages <= 10}
      <div class="page-numbers">
        {#each Array(totalPages) as _, i}
          <button
            on:click={() => setPage(i + 1)}
            style={i + 1 === page ? "font-weight: bold" : ""}
          >
            {i + 1}
          </button>
        {/each}
      </div>
    {:else}
      <p>Page {page} of {totalPages}</p>
    {/if}

    <button on:click={() => setPage("next")}>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.5"
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
    width: 100%;
    background: #ede7de;
    /* border: 1px dashed #494b5380; */

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
  nav .page-numbers {
    display: flex;
  }
  nav .page-numbers button {
    border: none;
    width: initial;
    padding: 0 0.4em;
  }
  nav .page-numbers button:hover {
    background: white;
    color: #494b53;
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
  footer nav p {
    margin: 0 0.4em;
  }
  footer output {
    font-family: "Dela Gothic One";
    font-size: 40px;
  }
  @media (max-width: 864px) {
    footer {
      padding: 40px 20px;
    }
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
