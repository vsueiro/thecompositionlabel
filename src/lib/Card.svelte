<script>
  export let item;
</script>

<style>
  li {
    width: 240px;
  }

  img {
    max-width: 100%;
  }
</style>

<li>
  <img src={item.Image} loading="lazy">
  <h3>{item.Title}</h3>
  <p><small>{item.Composition}</small></p>
</li>