<script>
  import FilteredList from "../lib/FilteredList.svelte";
</script>

<section id="list">
  <div class="columns">
    <h3>Types of <br />materials</h3>
    <div>
      <p class="description">
        Play with the filters below to discover a more sustainable closet.
        <br />
        Legend colors reveal the eco&#8209;friendliness of each fabric.
      </p>
      <p class="legend">
        <span class="green">Biodegradable</span>
        <span class="red">Non-Biodegradable</span>
      </p>
    </div>
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

  .columns {
    padding: 60px 40px 20px 40px;
    display: flex;
    align-items: center;
    width: 100%;
  }

  .columns > * {
    width: 50%;
  }

  h3 {
    font-size: 40px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    text-wrap: pretty;
  }

  .legend {
    display: flex;
    gap: 1em;
    font-size: 14px;
    white-space: nowrap;
    margin-top: 1em;
  }
  .green,
  .red {
    display: flex;
    align-items: center;
  }
  .green::before,
  .red::before {
    content: "";
    display: block;
    height: 16px;
    width: 16px;
    border-radius: 50%;
    transform: translateY(-1px);
    margin-right: 0.5em;
  }
  .green:before {
    background: #e5f4bc;
    border: 1px solid hsl(75, 82%, 56%);
  }
  .red::before {
    background: #f4e1f0;
    border: 1px solid hsl(289, 41%, 84%);
  }

  @media (max-width: 864px) {
    .columns {
      padding: 40px 20px 20px 20px;
      gap: 0;
      flex-direction: column;
      align-items: start;
    }
    .columns > * {
      width: 100%;
    }
    h3 br {
      display: none;
    }
    .description br {
      display: none;
    }
    h3 {
      font-size: 32px;
      padding-right: 0;
      margin-bottom: 1em;
    }
  }
</style>
