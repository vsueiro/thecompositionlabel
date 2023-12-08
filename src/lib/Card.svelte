<script>
  export let item;

  // quick and dirty
  let biodegradableMaterials = [
    "Linen",
    "Cotton",
    "Viscose",
    "Lyocell",
    "Silk",
    "Modal",
  ];
  let materials = item.Composition.split(",");
  let biodegradableCount = 0;

  for (let material of materials) {
    if (
      biodegradableMaterials.some((biodegradableMaterial) =>
        material.includes(biodegradableMaterial)
      )
    ) {
      biodegradableCount++;
    }
  }

  $: isBiodegradable = materials.length === biodegradableCount;
</script>

<li class="card {isBiodegradable ? 'biodegradable' : 'non-biodegradable'}">
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
              style="background: {biodegradableMaterials.some(
                (biodegradableMaterial) =>
                  material.includes(biodegradableMaterial)
              )
                ? '#bcf2ff'
                : '#ffd7df'}
                "
            >
              {material}
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
    outline: 1px solid black;
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
    background: #f5f2ec;
    border-radius: 4px;
    align-self: start;
    width: fit-content;
  }

  .biodegradable a:after {
    content: "";
    display: block;
    position: absolute;
    width: 64px;
    height: 64px;
    top: -12px;
    left: -12px;
    background: blue;
    border-radius: 50%;
  }
</style>
