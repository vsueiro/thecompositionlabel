<script>
  export let amount;
  export let highlights;

  const columns = 20;
  const width = `${100 / columns}%`;
  const numbers = Array(amount)
    .fill()
    .map((_, i) => i);
</script>

<div class="symbols">
  {#each numbers as number}
    <div
      class="
        symbol
        {number >= amount - highlights
        ? highlights === 1
          ? 'highlight unique'
          : 'highlight'
        : ''}
        "
      style="width: {width}"
    ></div>
  {/each}
</div>

<style>
  .symbols {
    display: flex;
    flex-direction: row-reverse;
    flex-wrap: wrap;
    width: 100%;
    margin: 1em 0 2em;
  }

  .symbol {
    position: relative;
    aspect-ratio: 1;
    z-index: 1;
    background-image: url(/assets/tee-non-biodegradable.svg);
    background-repeat: no-repeat;
    background-size: 100%;
  }

  .symbol.highlight {
    z-index: 2;
    background-image: none;
  }

  .symbol.highlight.unique::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: #e8f8b9;
    opacity: 0.5;
    border-radius: 50%;
    transform: scale(2);
  }

  .symbol.highlight::after {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-image: url(/assets/tee-biodegradable-alt.svg);
    background-repeat: no-repeat;
    background-size: 100%;
  }
</style>
