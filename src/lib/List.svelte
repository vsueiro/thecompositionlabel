<script>
  import FilteredList from "../lib/FilteredList.svelte";
</script>

<section id="list">
  <div>
    <h3>Types of materials</h3>
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
    padding: 60px 40px 20px 40px;
    display: flex;
    align-items: center;
    gap: 40px;
  }

  h3 {
    font-size: 40px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    padding-right: 40px;
    text-wrap: pretty;
  }
</style>
