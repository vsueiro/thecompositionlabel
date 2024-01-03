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
  .container {
    max-width: 1376px;
    width: calc(100% - 48px);
    margin: 24px auto 48px;
  }
  @media (max-width: 960px) {
    .container {
      width: calc(100% - 24px);
      margin: 12px auto 24px;
    }
  }
</style>
