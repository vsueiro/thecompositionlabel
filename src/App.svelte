<script>
  import Backlight from "./lib/Backlight.svelte";
  import Header from "./lib/Header.svelte";
  import Cover from "./lib/Cover.svelte";
  import List from "./lib/List.svelte";
</script>

<Backlight />

<div class="container">
  <Header />
  <Cover />
  <List />
</div>

<style>
  .container {
    max-width: 1376px;
    width: calc(100% - 48px);
    margin: 24px auto 48px;
  }
</style>
