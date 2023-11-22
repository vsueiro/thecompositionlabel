<script>
  export let item;
</script>

<li class="card">
  <figure>
    <img src={item.Image} loading="lazy" />
    <figcaption>
      <div>
        <h3>{item.Title}</h3>
        <data value={item.Price}>${item.Price}</data>
      </div>
      <ol>
        {#each item.Composition.split(",") as item}
          <li>{item}</li>
        {/each}
      </ol>
    </figcaption>
  </figure>
</li>

<style>
  .card {
    width: 240px;
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
  }

  .card:hover {
    outline: 1px solid black;
  }

  .card:hover figcaption {
    border-color: currentColor;
  }

  figure {
    margin: 0;
  }

  figcaption {
    padding: 8px 0 0;
    border-top: 1px solid transparent;
  }

  figcaption > div {
    display: flex;
    justify-content: space-between;
  }

  data {
    margin-right: 8px;
    font-size: 14px;
  }

  img {
    display: block;
    width: 100%;
  }

  h3 {
    margin: 0 8px;
    font-size: 14px;
    font-weight: normal;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  ol {
    list-style: none;
    padding: 8px;
    display: flex;
    flex-wrap: wrap;
    justify-items: start;
    gap: 4px;
  }

  ol > li {
    font-size: 12px;
    text-transform: lowercase;
    padding: 0 0.4em;
    background: #f5f2ec;
    border-radius: 4px;
    align-self: start;
    width: fit-content;
  }
</style>
