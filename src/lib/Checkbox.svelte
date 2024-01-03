<script>
  export let checked;
  export let material;
  export let icon;
</script>

<label data-biodegradable={material.Biodegradable}>
  <input type="checkbox" bind:checked class="screen-reader" />
  {#if icon}
    <img src="assets/icons/{icon}" alt="" />
  {/if}
  <div>{material.Name === "Polyamide" ? "Nylon" : material.Name}</div>
</label>

<style>
  label {
    font-family: "Dela Gothic One";
    user-select: none;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    border-radius: 6px;
    border: 1px solid #494b53;
    width: fit-content;
    height: 56px;
    cursor: pointer;
    flex-shrink: 0;
    font-size: 14px;
  }

  img {
    width: 48px;
    height: 100%;
    object-position: center;
    margin: 0 4px;
  }

  div {
    display: flex;
    align-items: center;
    padding: 0 16px;
    height: 100%;
  }

  img + div {
    border-left: 1px solid #494b53;
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

  label {
    transition: transform 0.2s;
  }

  label:has(input:focus-visible) {
    outline: 2px solid #494b53;
  }

  label:hover {
    transform: scale(1.05);
  }

  label:has(input:checked) {
    background: #f4e1f0;
  }

  label[data-biodegradable="true"]:has(input:checked) {
    background: #e5f4bc;
  }

  @media (max-width: 960px) {
    label {
      height: 48px;
      font-size: 12px;
    }
    img {
      width: 40px;
    }
    div {
      padding: 0 12px;
    }
  }
</style>
