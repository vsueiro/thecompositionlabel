<script>
  import TagAnimation from "../lib/TagAnimation.svelte";
</script>

<section>
  <article>
    <h2>Avoid wearing plastic</h2>
    <p>
      Fast fashion’s obsession with plastic-based fabrics, like polyester and
      elastane, is trashing our planet. However, finding more natural
      alternatives can be super time-consuming.
    </p>

    <p>
      That’s why we've sorted through SHEIN to bring you their best in
      biodegradable fashion – focusing on natural fibers like cotton, linen, and
      viscose.
    </p>
  </article>
  <TagAnimation />
</section>

<style>
  section {
    background: #fff;
    display: flex;
    align-items: center;
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
    padding-right: 80px;
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
</style>
