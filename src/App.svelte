<script>
  import Backlight from "./lib/Backlight.svelte";
  import Header from "./lib/Header.svelte";
  import Cover from "./lib/Cover.svelte";
  import CareInstructions from "./lib/CareInstructions.svelte";
  import List from "./lib/List.svelte";
  import Footer from "./lib/Footer.svelte";

  import { modalOpen } from "./lib/modalStore.js";

  $: {
    if ($modalOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
  }
</script>

<Backlight />

<div class="container">
  <Header />
  <Cover />
  <CareInstructions />
  <List />
  <Footer />
</div>

<style>
  :root {
    --card-width: 240px;
  }

  @media (max-width: 1392px) {
    /* 4 Cards per row */
    :root {
      --card-width: calc(calc(100vw - calc(96px + calc(3 * 24px))) / 4);
    }
  }

  @media (max-width: 1128px) {
    /* 3 Cards per row */
    :root {
      --card-width: calc(calc(100vw - calc(96px + calc(2 * 24px))) / 3);
    }
  }

  @media (max-width: 864px) {
    /* 2 Cards per row */
    :root {
      --card-width: calc(calc(100vw - calc(56px + calc(1 * 16px))) / 2);
    }
  }

  .container {
    max-width: 1344px;
    width: calc(100% - 48px);
    margin: 24px auto 48px;
  }
  @media (max-width: 864px) {
    .container {
      width: calc(100% - 24px);
      margin: 12px auto 24px;
    }
  }
</style>
