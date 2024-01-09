<script>
  import { onMount } from "svelte";
  import { csv, autoType } from "d3";

  $: formattedDate = "";

  onMount(async () => {
    try {
      let response = await csv("./data/meta.csv", autoType);

      let meta = response[0];

      let timestamp = meta.Updated;

      // Format the timestamp
      const date = new Date(timestamp);
      const formatted = new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      }).format(date);

      // Update the reactive variable
      formattedDate = `
        Last updated in ${formatted}. <br>
        Out of the 
        ${new Intl.NumberFormat("en-US").format(meta.Items)}
        items we collected this week,
        ${new Intl.NumberFormat("en-US").format(meta.Biodegradable)}
        are biodegradable.`;
    } catch (error) {
      console.error("Failed to fetch timestamp:", error);
      formattedDate = "";
    }
  });
</script>

<!-- Display the formatted date inside a paragraph tag -->
<p><small>{@html formattedDate}</small></p>

<style>
  p {
    margin: 1em 0;
  }
</style>
