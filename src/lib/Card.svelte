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
    border-radius: 8px;
    overflow: hidden;
    outline: 1px solid transparent;
    transition: all 0.4s;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  .card:hover {
    outline: 1px solid black;
  }

  .card:hover figcaption {
    border-color: currentColor;
  }

  .card:hover .photo:after {
    opacity: 0.2;
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

  .photo {
    position: relative;
  }

  .photo:after {
    content: "";
    display: block;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-image: radial-gradient(#ffd7df 33%, transparent 33%);
    background-attachment: fixed;
    background-size: 2px 2px;
    opacity: 1;
    transition: all 0.4s;
  }

  .biodegradable .photo:after {
    background-image: radial-gradient(#bcf2ff 33%, transparent 33%);
  }
</style>
