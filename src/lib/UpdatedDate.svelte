<script>
  import { onMount } from "svelte";

  $: formattedDate = "";

  onMount(async () => {
    try {
      let response = await fetch("./data/updated.txt");
      let timestamp = await response.text();

      // Format the timestamp
      const date = new Date(timestamp);
      const formatted = new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      }).format(date);

      // Update the reactive variable
      formattedDate = `Last updated in ${formatted}`;
    } catch (error) {
      console.error("Failed to fetch timestamp:", error);
      formattedDate = "";
    }
  });
</script>

<!-- Display the formatted date inside a paragraph tag -->
<p><small>{formattedDate}</small></p>

<style>
  p {
    margin: 1em 0;
  }
</style>
