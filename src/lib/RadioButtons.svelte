<script>
  export let radioOptions = []; // Array of objects { value, label }
  export let selectedType; // Bound group variable
</script>

<div>
  {#each radioOptions as option}
    <label class="button">
      <input
        class="screen-reader"
        type="radio"
        bind:group={selectedType}
        name="clothing"
        value={option.value}
      />
      <span>{option.label}</span>
    </label>
  {/each}
</div>

<style>
  .screen-reader {
    clip: rect(0 0 0 0);
    clip-path: inset(50%);
    height: 1px;
    overflow: hidden;
    position: absolute;
    white-space: nowrap;
    width: 1px;
  }

  div {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  label {
    background: white;
    white-space: nowrap;
    border: 1px solid #494b53;
    color: #494b53;
    border-radius: 999px;
    font-size: 14px;
    width: fit-content;
    text-transform: uppercase;
    display: flex;
    gap: 8px;
    justify-content: center;
    align-items: center;
    transition: all 0.4s;
    cursor: pointer;
    user-select: none;
    padding: 8px 16px 8px;
    border-radius: 999px;
    width: fit-content;
  }

  label:hover {
    background: #494b5320;
  }

  label:has(input:checked) {
    background: #494b53;
    color: white;
  }

  label::before {
    content: "";
    display: flex;
    width: 8px;
    height: 8px;
    outline: 1px solid #494b53;
    border-radius: 50%;
    background: white;
  }
  span {
    padding-top: 2px;
  }
</style>
