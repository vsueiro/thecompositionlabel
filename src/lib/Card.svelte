<script>
  export let item;
  export let biodegradableMaterials;
</script>

<li class="card {item.isBiodegradable ? 'biodegradable' : 'non-biodegradable'}">
  <a href={item.Link} target="_blank">
    <figure>
      <div class="photo">
        <img src={item.Image} loading="lazy" alt={item.Title} />
      </div>
      <figcaption>
        <div>
          <h3>{item.Title}</h3>
          {#if item.Price}
            <data value={item.Price}>${item.Price}</data>
          {/if}
        </div>
        <ol>
          {#each item.Composition.split(",") as material}
            <li
              class={biodegradableMaterials.some((biodegradableMaterial) =>
                material.includes(biodegradableMaterial)
              )
                ? "biodegradable"
                : ""}
            >
              {material.replace("Polyamide", "Nylon")}
            </li>
          {/each}
        </ol>
      </figcaption>
    </figure>
  </a>
</li>

<style>
  .card {
    width: 240px;
    background: #fff;
    outline: 1px solid #494b53;
    transition: all 0.25s;
    border-radius: 8px;
  }

  a {
    position: relative;
    display: block;
    text-decoration: none;
    color: inherit;
  }

  figure {
    margin: 0;
    border-radius: 8px;
    overflow: hidden;
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
    aspect-ratio: 240/321;
    object-fit: cover;
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
    background: #f4e1f0;
    border-radius: 3px;
    align-self: start;
    width: fit-content;
  }

  ol > li.biodegradable {
    background: #e5f4bc;
  }

  .card.biodegradable a:after {
    content: "";
    display: block;
    position: absolute;
    width: 64px;
    height: 64px;
    top: -12px;
    left: -12px;
    background: url(assets/badge.svg) center no-repeat;
    background-size: 100%;
  }
</style>
