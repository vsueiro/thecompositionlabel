<script>
  import { modalOpen } from "./modalStore.js";
</script>

<div class="modal {$modalOpen ? 'modal-open' : ''}">
  <div class="overlay" on:click={() => modalOpen.set(false)}></div>
  <aside>
    {#if $modalOpen}
      <button class="button" on:click={() => modalOpen.set(false)}>
        Close
      </button>
    {/if}

    <h3>Why Should I Care?</h3>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus voluptas
      quibusdam similique.
    </p>

    <p>
      Inventore reprehenderit error eius facere cum, facilis quasi eligendi
      necessitatibus.
    </p>

    <p>vero, doloremque natus ducimus fugit tempora? Eos, minima!</p>
  </aside>
</div>

<style>
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

  aside {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: 80%;
    max-width: 576px;
    background: white;
    padding: 40px;
    transform: translateX(100%);
    pointer-events: none;
    user-select: none;
    transition: all 0.4s;
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
    padding: 3px 16px 0;
    border-radius: 999px;
    font-size: 14px;
    width: fit-content;
    text-transform: uppercase;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.4s;
    z-index: 2;
    cursor: pointer;
    user-select: none;
  }

  .button:hover {
    background: #494b53;
    color: white;
  }
</style>
