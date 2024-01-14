<script>
  export let timestamp;

  // Format the timestamp (with UTC)
  const date = new Date(timestamp + "Z");
  const formatted = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  }).format(date);
</script>

<!-- Display the formatted date inside a paragraph tag -->
<p><small>Last updated in {formatted}.</small></p>

<style>
  p {
    margin: 3em 0 0;
  }
</style>
