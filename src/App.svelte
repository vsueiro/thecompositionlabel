<script>
  import Header from "./lib/Header.svelte";
  import Cover from "./lib/Cover.svelte";
  import List from "./lib/List.svelte";
</script>

<div id="app">
  <Header />
  <Cover />
  <List />
</div>

<style>
  #app {
    max-width: 1440px;
    width: calc(100% - 48px);
    margin: 24px auto 48px;
  }
</style>
