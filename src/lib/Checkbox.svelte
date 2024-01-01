<script>
  export let material;
  export let checked;
</script>

<label>
  <input type="checkbox" bind:checked />
  {material.Name}
</label>

<style>
  label {
    user-select: none;
  }
</style>
