<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";

  let data;
  let treemapData = [];
  let size = [480, 360];

  let highlights = {
    Elastane: {
      text: "Most in blended compositions",
      icon: "./assets/washing-machine.svg",
    },
    Polyester: {
      text: "Appears 1000x in ”Women Top Rated”",
      icon: "./assets/shirts.svg",
    },
  };

  onMount(async () => {
    data = await d3.csv("./data/materials.csv", d3.autoType);
    console.log(data);
    createTreemap();
  });

  function createTreemap() {
    const root = d3
      .hierarchy({ children: data })
      .sum((d) => d.Percent)
      .sort((a, b) => b.height - a.height || b.value - a.value);

    d3.treemap().size(size).padding(0).round(true).tile(d3.treemapBinary)(root);

    treemapData = root.leaves();

    console.log(treemapData);
  }

  function percentX(number) {
    return `${(number / size[0]) * 100}%`;
  }

  function percentY(number) {
    return `${(number / size[1]) * 100}%`;
  }
</script>

<div class="container">
  <svg viewBox="-1 -1 {size[0] + 2} {size[1] + 2}">
    {#each treemapData as node}
      <rect
        x={node.x0}
        y={node.y0}
        width={node.x1 - node.x0}
        height={node.y1 - node.y0}
        fill={node.data.Biodegradable === "True" ? "#e8f8b9" : "#f0e2f3"}
        stroke-width="1"
        stroke="#494b53"
      >
      </rect>
      {#if node.data.Percent > 3}
        <text
          x={node.x0 + 10}
          y={node.y0 + 30}
          fill="#494b53"
          font-size="20"
          font-family="Dela Gothic One"
        >
          {Math.round(node.data.Percent)}%
        </text>
        <text x={node.x0 + 10} y={node.y0 + 50} fill="#494b53" font-size="16">
          {node.data.Name.replace("Polyamide", "Nylon")}
        </text>
      {/if}
    {/each}
  </svg>
  <div class="hotspots">
    {#each treemapData as node}
      {#if node.data.Name in highlights}
        <div
          class="hotspot"
          style="top: {percentY(node.y0)}; left: {percentX(
            node.x0
          )}; width: {percentX(node.x1 - node.x0)}; height: {percentY(
            node.y1 - node.y0
          )};"
        >
          <div class="info">
            <div class="shadow"></div>
            <div class="box">
              <img src={highlights[node.data.Name].icon} alt="" />
              <span>{highlights[node.data.Name].text}</span>
            </div>
          </div>
        </div>
      {/if}
    {/each}
  </div>
</div>

<style>
  /* rect {
    fill-opacity: 1;
    transition: fill-opacity 0.4s;
  }
  rect:hover {
    fill-opacity: 1;
  } */
  text {
    pointer-events: none;
  }
  .container {
    position: relative;
  }
  .hotspots {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    font-size: 14px;
  }

  .hotspot {
    position: absolute;
    display: flex;
    align-items: end;
    padding: 10px;
    overflow: hidden;
  }

  .info {
    width: 100%;
    position: relative;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.4s;
  }

  .hotspot:hover .info {
    opacity: 1;
    transform: translateY(0);
  }

  .box {
    border-radius: 4px;
    outline: 1px solid currentColor;
    background: white;
    line-height: 1.25;
    position: relative;
    display: flex;
    align-items: center;
  }

  .box img {
    object-fit: contain;
    width: 24px;
    margin: 0 8px;
    height: 100%;
  }

  .box > span {
    padding: 8px 8px;
  }

  .box img + span {
    border-left: 1px solid currentColor;
  }

  .shadow {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    border-radius: 6px 4px;
    border: 1px solid currentColor;
    transform: translate(3px, 3px);
  }
</style>
