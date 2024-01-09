<script>
  import TagAnimation from "../lib/TagAnimation.svelte";
</script>

<section>
  <article>
    <div class="spacer"></div>

    <div>
      <h2>Avoid wearing plastic</h2>
      <p>
        Fast fashion’s obsession with plastic-based fabrics, like polyester and
        elastane, is trashing our planet. However, finding more natural
        alternatives can be super time-consuming.
      </p>

      <p>
        That’s why we've sorted through
        <a href="https://us.shein.com/" target="_blank">SHEIN</a>
        to bring you their best in
        <span
          style="
            background: #e8f8b9;
            padding: .25em;
            white-space: nowrap;
            border-radius: 3px">biodegradable</span
        > fashion – focusing on natural fibers like cotton, linen, and viscose.
      </p>
    </div>

    <a href="#list" class="button">
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
        class="feather feather-arrow-down"
        ><line x1="12" y1="5" x2="12" y2="19"></line><polyline
          points="19 12 12 19 5 12"
        ></polyline></svg
      >
      <span class="screen-reader">Scroll Down</span>
    </a>
  </article>
  <TagAnimation />
</section>

<style>
  section {
    background: #fff;
    display: flex;
    align-items: normal;
    justify-content: space-between;
    gap: 40px;
    padding: 40px;
    margin: 8px auto;
    border-radius: 16px;
  }
  article {
    max-width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding-right: 80px;
    min-height: 100%;
  }
  h2 {
    font-size: 48px;
    line-height: 1;
    font-family: "Dela Gothic One";
    font-synthesis: none;
    margin-bottom: 1em;
    text-wrap: pretty;
  }
  p {
    font-size: 18px;
    margin-bottom: 1em;
  }
  a.button {
    color: inherit;
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    font: inherit;
    cursor: pointer;
    /* outline: inherit; */
    appearance: none;
    box-shadow: none;
    height: 56px;
    width: 56px;
    border: 1px solid #494b53;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    user-select: none;
    transition:
      background-color 0.4s,
      color 0.4s;
  }
  a.button:hover {
    background: #494b53;
    color: white;
  }
  a.button:focus-visible {
    outline: 2px solid #1c6fd4;
    outline-offset: 1px;
  }
  .screen-reader {
    clip: rect(0 0 0 0);
    clip-path: inset(50%);
    height: 1px;
    overflow: hidden;
    position: absolute;
    white-space: nowrap;
    width: 1px;
  }
  @media (max-width: 1280px) {
    article {
      padding-right: 40px;
    }
  }
  @media (max-width: 864px) {
    section {
      gap: 20px;
      padding: 20px;
    }
    article {
      max-width: 100%;
      padding-right: 0;
      padding-top: 20px;
    }
    h2 {
      font-size: 36px;
    }
    p {
      font-size: 16px;
    }
    a.button {
      height: 36px;
      width: 36px;
      display: none;
    }
    .spacer {
      display: none;
    }
  }
</style>
