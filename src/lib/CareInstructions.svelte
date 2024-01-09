<script>
  import { onMount } from "svelte";
  import { csv, autoType } from "d3";
  import { modalOpen } from "./modalStore.js";
  import Treemap from "./Treemap.svelte";
  import WaffleChart from "./WaffleChart.svelte";
  import LastUpdated from "./LastUpdated.svelte";

  $: meta = {};
  $: items = new Intl.NumberFormat("en-US").format(meta.Items);
  $: biodegradableItems = new Intl.NumberFormat("en-US").format(
    meta.Biodegradable
  );
  $: biodegradableItemsPer1000 = Math.round(meta.Ratio * 10);

  onMount(async () => {
    try {
      let response = await csv("./data/meta.csv", autoType);
      meta = response[0];
    } catch (error) {
      console.error("Failed to fetch timestamp:", error);
    }
  });
</script>

<div class="modal {$modalOpen ? 'modal-open' : ''}">
  <div class="overlay" on:click={() => modalOpen.set(false)}></div>
  <aside>
    <button
      class="button"
      on:click={() => modalOpen.set(false)}
      disabled={!$modalOpen}
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.5"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="feather feather-chevron-left"
        ><polyline points="15 18 9 12 15 6"></polyline></svg
      >
    </button>
    <div class="scrollable">
      <h3>Why Should I Care?</h3>

      <p>
        A major concern with synthetic fabric clothing are
        <a href="https://en.wikipedia.org/wiki/Microplastics" target="_blank"
          >microplastics</a
        >, the tiny pieces of trash they keep leaving behind, which end up in
        oceans, in the
        <a
          href="https://artsexperiments.withgoogle.com/plasticair/"
          target="_blank">air</a
        >, and in our food.
      </p>

      <p>
        However,
        <span
          style="
            background: #f0e2f3;
            padding: .25em;
            white-space: nowrap;
            border-radius: 3px">synthetic materials</span
        >
        are present in most clothes from
        <a href="https://us.shein.com/" target="_blank">SHEIN</a>, a leading
        fast fashion ecommerce in the U.S.
      </p>
      <!--
      <p>
        Microplastics from non-biodegradable fabrics pollute oceans, enter our
        food and bodies, with unknown long-term health effects.
      </p>
      -->

      <h4>How many clothes on SHEIN are made from each material?</h4>

      <Treemap />

      <p>
        We exist to help you find those rare <span
          style="
          background: #e8f8b9;
          padding: .25em;
          white-space: nowrap;
          border-radius: 3px">biodegradable</span
        > items, by analzying SHEIN’s top-rated products every week.
      </p>

      {#if "Items" in meta}
        <p>
          Out of the {items}
          items we collected this week, {biodegradableItems}
          are biodegradable, in other words…
        </p>

        <h4>
          For every 1,000 items,
          {biodegradableItemsPer1000}
          {biodegradableItemsPer1000 === 1 ? "is" : "are"}
          fully biodegradable
        </h4>

        <WaffleChart amount={1000} highlights={biodegradableItemsPer1000} />
      {/if}

      {#if "Updated" in meta}
        <LastUpdated timestamp={meta.Updated} />
      {/if}
    </div>
  </aside>
</div>

<style>
  .scrollable {
    height: 100%;
    max-height: 100%;
    overflow-y: scroll;
    scroll-behavior: smooth;
    padding: 40px 40px 60px;
  }
  .scrollable p + p {
    margin-top: 1em;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: #494b53cc;
    z-index: 4;
    opacity: 0;
    pointer-events: none;
    transition: all 0.4s;
  }

  .modal-open .overlay {
    opacity: 1;
    pointer-events: all;
  }

  h3 {
    font-size: 40px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    margin: 1em 0;
    text-wrap: pretty;
  }

  h4 {
    font-size: 24px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    text-wrap: pretty;
    margin: 1.5em 0 0.75em;
  }

  aside {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: calc(100% - 24px);
    max-width: 552px;
    background: white;
    padding: 0;
    transform: translateX(calc(100% + 28px));
    pointer-events: none;
    user-select: none;
    transition: transform 0.4s;
    z-index: 5;
  }

  .modal-open aside {
    transform: translateX(0);
    pointer-events: all;
    user-select: all;
  }

  .button {
    background: white;
    white-space: nowrap;
    border: 1px solid #494b53;
    color: #494b53;
    height: 40px;
    width: 40px;
    border-radius: 999px;
    font-size: 14px;
    text-transform: uppercase;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.4s;
    z-index: 2;
    cursor: pointer;
    user-select: none;
    padding: 0;
    position: absolute;
    top: 40px;
    left: -20px;
    box-shadow: 0 0 0 8px white;
  }

  .button:hover {
    background: #494b53;
    color: white;
  }

  @media (max-width: 864px) {
    .scrollable {
      padding: 20px 20px 80px;
      border-top: 1px solid #494b53;
    }
    h3 {
      margin-top: 0;
      font-size: 32px;
    }
    .button {
      position: relative;
      top: initial;
      left: initial;
      margin: 20px 20px 16px;
    }
    aside {
      width: calc(100% - 12px);
    }
  }
</style>
