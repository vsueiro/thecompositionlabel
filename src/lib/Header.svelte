<script>
  import { modalOpen } from "./modalStore.js";

  function toggleModal() {
    modalOpen.set(true);
  }
</script>

<header>
  <a href="./">
    <h1>
      <span>The</span>
      <span>Composition</span>
      <span>Label</span>
    </h1>
  </a>
  <button class="button" on:click={toggleModal}
    >Care<span>&nbsp;Instructions</span></button
  >
</header>

<style>
  header {
    background: #fff;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    margin: 8px auto;
    border-radius: 16px;
  }
  a {
    text-decoration: none;
    color: inherit;
  }
  a:focus-visible {
    outline: 2px solid #1c6fd4;
    outline-offset: 1px;
  }
  h1 {
    display: flex;
    text-transform: lowercase;
    font-weight: 400;
    font-size: 22px;
  }
  span:nth-child(2) {
    font-weight: 700;
  }

  .button {
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
    transition:
      background-color 0.4s,
      color 0.4s;
    z-index: 2;
    cursor: pointer;
    user-select: none;
  }

  .button:hover {
    background: #494b53;
    color: white;
  }

  .button:focus-visible {
    outline: 2px solid #1c6fd4;
    outline-offset: 1px;
  }

  @media (max-width: 864px) {
    header {
      height: 56px;
      padding: 0 20px;
    }
    h1 {
      font-size: 17.6px;
    }
  }

  @media (max-width: 480px) {
    .button span {
      display: none;
    }
  }
</style>
