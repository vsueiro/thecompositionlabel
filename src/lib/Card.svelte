<script>
  export let item;
  export let materials;

  const sortedMaterials = materials
    .filter((material) => {
      return material.Name in item && item[material.Name] > 0;
    })
    .sort((a, b) => {
      return item[b.Name] - item[a.Name];
    });
</script>

<div class="card {item.Biodegradable ? 'biodegradable' : ''}">
  <a href={item.Link} target="_blank">
    <figure>
      <div class="photo">
        <img src={item.Image} loading="lazy" alt={item.Title} />
        <div class="button">See on Shein</div>
      </div>
      <figcaption>
        <div>
          <h5 title={item.Title}>{item.Title}</h5>
          {#if item.Price}
            <data value={item.Price}>${item.Price}</data>
          {/if}
        </div>
        <ol>
          {#each sortedMaterials as material}
            <li class={material.Biodegradable ? "biodegradable" : ""}>
              {item[material.Name]}%
              {material.Name.replace("Polyamide", "Nylon")}
            </li>
          {/each}
        </ol>
      </figcaption>
    </figure>
  </a>
</div>

<style>
  .card {
    width: var(--card-width);
    background: #fff;
    outline: 1px solid #494b53;
    transition: all 0.25s;
    border-radius: 8px;
    height: 100%;
  }

  a {
    position: relative;
    display: block;
    text-decoration: none;
    color: inherit;
    height: 100%;
    border-radius: 8px;
  }

  a:focus-visible {
    outline: 2px solid #1c6fd4;
    outline-offset: 2px;
  }

  figure {
    margin: 0;
    border-radius: 8px;
    overflow: hidden;
  }

  .photo {
    position: relative;
  }

  .photo::after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background: #494b53;
    display: block;
    opacity: 0;
    pointer-events: none;
    transition: all 0.4s;
    z-index: 1;
  }

  .button {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, 0);
    opacity: 0;
    background: white;
    white-space: nowrap;
    border: 1px solid #494b53;
    color: #494b53;
    height: 40px;
    padding: 3px 16px 0;
    border-radius: 999px;
    font-size: 14px;
    width: fit-content;
    text-transform: uppercase;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.4s;
    user-select: none;
    z-index: 2;
  }

  .button:hover {
    background: #494b53;
    color: white;
  }

  a:hover .photo::after {
    opacity: 0.3;
  }

  a:hover .button {
    opacity: 1;
    transform: translate(-50%, -16px);
  }

  figcaption {
    padding: 12px 0 4px;
    border-top: 1px solid #494b53;
  }

  figcaption > div {
    display: flex;
    justify-content: space-between;
  }

  data {
    margin-right: 12px;
    font-size: 14px;
  }

  img {
    display: block;
    width: 100%;
    aspect-ratio: 240/321;
    object-fit: cover;
  }

  h5 {
    margin: 0 12px;
    font-size: 14px;
    font-weight: normal;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  ol {
    list-style: none;
    padding: 4px 12px 8px;
    display: flex;
    flex-wrap: wrap;
    justify-items: start;
    gap: 4px;
  }

  ol > li {
    font-size: 12px;
    text-transform: lowercase;
    padding: 0 0.4em;
    background: #f0e2f3;
    border-radius: 3px;
    align-self: start;
    width: fit-content;
  }

  ol > li.biodegradable {
    background: #e8f8b9;
  }

  .card.biodegradable a:after {
    content: "";
    display: block;
    position: absolute;
    width: 64px;
    height: 64px;
    top: -12px;
    left: -12px;
    background: url(/assets/badge.svg) center no-repeat;
    background-size: 100%;
    z-index: 3;
  }

  @media (max-width: 576px) {
    .card.biodegradable a:after {
      width: 48px;
      height: 48px;
    }
  }
</style>
