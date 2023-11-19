<script>
  export let material;
  export let checked;
</script>

<label>
  <input type="checkbox" bind:checked={checked} />
  {material.Name}
</label>
