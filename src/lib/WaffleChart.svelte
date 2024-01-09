<script>
  export let amount;
  export let highlights;

  // function calculateColumns(amount) {
  //   // Find the square root of the amount
  //   const sqrt = Math.sqrt(amount);

  //   // Round it to the nearest whole number
  //   const roundedSqrt = Math.floor(sqrt);

  //   // Calculate the number of columns
  //   // If the rounded square root squared is less than the amount,
  //   // use the rounded square root as the number of columns
  //   // Otherwise, use the rounded square root - 1 to ensure
  //   // the total number of cells >= amount
  //   const columns =
  //     roundedSqrt * roundedSqrt >= amount ? roundedSqrt : roundedSqrt - 1;

  //   return columns;
  // }

  const columns = 50;
  const width = `${100 / columns}%`;
  const numbers = Array(amount)
    .fill()
    .map((_, i) => i);

  console.log(columns, width);
</script>

<div class="symbols">
  {#each numbers as number}
    <div
      class="symbol {number > amount - highlights ? 'highlight' : ''}"
      style="width: calc({width} - 1px); margin: 0 1px 1px 0;"
    ></div>
  {/each}
</div>

<style>
  .symbols {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
    /* gap: 1px; */
  }

  .symbol {
    position: relative;
    width: 1%;
    aspect-ratio: 1;
    background: #f0e2f3;
    z-index: 1;
    /* box-shadow: inset 0 0 0 1px white; */
  }

  .symbol.highlight {
    background: #e8f8b9;
    z-index: 2;
    box-shadow: 0 0 0 1px #494b53;
  }
</style>
