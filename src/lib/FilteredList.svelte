<script>
  import Checkbox from "./Checkbox.svelte";
  import Card from "./Card.svelte";
  import { onMount } from "svelte";
  import { csv, autoType } from "d3";

  let filterMode = "any-of"; // Variable to track the select option (exactly|any-of)
  let materials = [];
  let items = [];
  let checkboxStates = {};
  let filteredItems = [];
  let itemsPerPage = 100;
  let page = 1;
  let totalPages = 1;

  $: totalPages = Math.ceil(filteredItems.length / itemsPerPage);

  $: paginatedItems = filteredItems.slice(
    (page - 1) * itemsPerPage,
    page * itemsPerPage
  );

  onMount(async () => {
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

      // Trigger reactive update
      filteredItems = [...items];
    } catch (error) {
      console.error(error);
    }
  });

  // Updated reactive statement for dynamic filtering
  $: {
    // Reactive statement to get checked materials
    // let checkedMaterials = materials.filter(
    //   (material) => checkboxStates[material.Name]
    // );

    if (materials.length) {
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

      filteredItems = [...new Set([...strictly, ...loosely])];
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
  <p>
    <!-- View clothes that contain -->
    <select bind:value={filterMode} hidden>
      <option value="any-of">any of</option>
      <option value="exactly">exactly</option>
    </select>
    <!-- these materials: -->
  </p>
  <div>
    {#each materials as material}
      <Checkbox {material} bind:checked={checkboxStates[material.Name]} />
    {/each}
  </div>
</form>

<ul>
  {#each paginatedItems as item}
    <Card {item} />
  {/each}
</ul>

<!-- Filtered List -->
<output>{filteredItems.length} items found</output>

<!-- Pagination Controls -->
<nav>
  <button on:click={prevPage}>Previous</button>
  <span>Page {page} of {totalPages}</span>
  <button on:click={nextPage}>Next</button>
</nav>

<style>
  ul {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    list-style: none;
    padding: 0;
  }
</style>
