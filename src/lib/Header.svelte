<header>
  <a href="/">
    <h1>
      <span>The</span>
      <span>Composition</span>
      <span>Label</span>
    </h1>
  </a>
</header>

<style>
  header {
    background: #fff;
    height: 72px;
    display: flex;
    align-items: center;
    padding: 0 40px;
    margin: 8px auto;
    border-radius: 16px;
  }
  a {
    text-decoration: none;
    color: inherit;
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

  @media (max-width: 960px) {
    header {
      height: 56px;
      padding: 0 20px;
    }
    h1 {
      font-size: 17.6px;
    }
  }
</style>
