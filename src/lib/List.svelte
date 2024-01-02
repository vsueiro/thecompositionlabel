<script>
  import FilteredList from "../lib/FilteredList.svelte";
</script>

<section>
  <div>
    <h2>Types of materials</h2>
    <p>
      Play with the filters below to discover a more sustainable closet. Inserir
      algum conteúdo sobre a diferença das cores serem biodegradáveis ou não
    </p>
  </div>

  <FilteredList />
</section>

<style>
  section {
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: start;
    margin: 8px auto;
    border-radius: 16px;
  }

  section > div {
    padding: 40px 40px 0 40px;
  }
</style>
