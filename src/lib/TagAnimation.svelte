<script>
  const tags = [
    {
      name: "Cotton",
      icon: "cotton.svg",
      tagline: "A natural fiber",
      labels: ["Versatile", "Breathable", "Comfortable"],
      biodegradable: true,
    },
    {
      name: "Polyester",
      icon: "polyester.svg",
      tagline: "A synthetic fiber",
      labels: ["Microplastics", "Chemical", "Pollution"],
      biodegradable: false,
    },
    {
      name: "Linen",
      icon: "linen.svg",
      tagline: "A natural fiber",
      labels: ["Stylish", "Hypoallergenic", "Strong"],
      biodegradable: true,
    },
    {
      name: "Elastane",
      icon: "elastane.svg",
      tagline: "A synthetic fiber",
      labels: ["Allergen", "Pollution", "Microplastics"],
      biodegradable: false,
    },
    {
      name: "Viscose",
      icon: "viscose.svg",
      tagline: "A semi synthetic fiber",
      labels: ["Light", "Durable", "Absorbent"],
      biodegradable: true,
    },
    {
      name: "Nylon",
      icon: "nylon.svg",
      tagline: "A synthetic fiber",
      labels: ["Non-breathable", "Plastic", "Chemical"],
      biodegradable: false,
    },
  ];
</script>

<dl>
  {#each tags as tag}
    <div class="shirt" data-biodegradable={tag.biodegradable}>
      <div class="tag">
        <div class="base" />
        <div class="info">
          <div class="print">
            <dt>
              <span class="name">{tag.name}</span>
              <span class="tagline">{tag.tagline}</span>
            </dt>
            <dd>
              <img src="assets/icons/{tag.icon}" alt="" />
              <div class="biodegradable">
                {tag.biodegradable ? "Biodegradable" : "Non-Biodegradable"}
              </div>
              <div class="labels">
                {#each tag.labels as label, index}
                  <span>{label}</span>
                  {#if index < tag.labels.length - 1}
                    <span aria-hidden="true">•</span>
                  {/if}
                {/each}
              </div>
            </dd>
          </div>
        </div>
      </div>
    </div>
  {/each}
</dl>

<style>
  :root {
    --height: 66.666vh;
    --duration: 24s;
    --count: 6;
  }
  @media (min-height: 960px) {
    :root {
      --height: 640px;
    }
  }
  dl {
    background: linear-gradient(180deg, #c8b4d2 0%, #dfc1d0 50%, #f1e6ec 100%);
    width: 50%;
    height: var(--height);
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    border-radius: 16px;
  }
  dl::after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    box-shadow: inset 0 0 96px #ceb8d280;
  }
  dd {
    margin: 0;
  }
  dt {
    position: absolute;
    left: 80px;
    top: 32px;
    right: 0;
    bottom: 32px;
    border-left: 1px solid #494b53;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 16px;
  }
  .name {
    font-family: "Dela Gothic One";
    font-size: 24px;
    text-transform: uppercase;
  }
  img {
    position: absolute;
    left: 16px;
    top: calc(32px + 18px);
    width: 48px;
    height: 48px;
  }
  .shirt {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: start;
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
  }
  .shirt[data-biodegradable="false"] {
    justify-content: end;
  }
  .tag {
    width: fit-content;
    display: flex;
  }
  .shirt[data-biodegradable="false"] .tag {
    flex-direction: row-reverse;
  }
  .base {
    position: relative;
    width: 32px;
    background: white;
    transform: translate(0, var(--height));
    animation: showTagBase var(--duration) infinite;
    border-right: 1px dashed #494b53;
    /* animation-play-state: paused; */
    /* animation-fill-mode: backwards; */
  }
  .shirt[data-biodegradable="false"] .base {
    border-right: none;
    border-left: 1px dashed #494b53;
  }
  /* .base::before {
    content: "";
    position: absolute;
    display: block;
    width: 1px;
    top: 0;
    bottom: 0;
    right: -1px;
    border-right: 1px dashed #494b53;
  }
  .shirt[data-biodegradable="false"] .base::before {
    right: initial;
    left: -1px;
    border-right: none;
    border-left: 1px dashed #494b53;
  } */
  .base::after {
    content: "";
    position: absolute;
    display: block;
    right: 0;
    bottom: 12px;
    width: 24px;
    height: 24px;
    background-image: url(/assets/scissors.svg);
    background-repeat: no-repeat;
    background-size: 100%;
    background-position-x: 8px;
    animation: cut var(--duration) infinite;
  }
  .shirt[data-biodegradable="false"] .base::after {
    right: initial;
    left: 0;
    transform: rotateY(180deg);
    animation: cutRight var(--duration) infinite;
  }
  .info {
    position: relative;
    width: 384px;
    height: 176px;
    background: white;
    /* border-left: 1px dashed #494b53; */
    /* margin-left: 2px; */
    transform: translate(0, var(--height));
    animation: showTagInfoLeft var(--duration) infinite;
    /* animation-play-state: paused; */
    /* animation-fill-mode: backwards; */
  }
  .shirt[data-biodegradable="false"] .info {
    animation: showTagInfoRight var(--duration) infinite;
    /* margin-right: 2px;
    margin-left: 0; */
    /* border-left: none; */
    /* border-right: 1px dashed #494b53; */
  }
  .shirt:nth-child(1) .base,
  .shirt:nth-child(1) .info,
  .shirt:nth-child(1) .base::after {
    animation-delay: 0s;
  }
  .shirt:nth-child(2) .base,
  .shirt:nth-child(2) .info,
  .shirt:nth-child(2) .base::after {
    animation-delay: calc(calc(var(--duration) / var(--count)) * calc(1 * 1));
  }
  .shirt:nth-child(3) .base,
  .shirt:nth-child(3) .info,
  .shirt:nth-child(3) .base::after {
    animation-delay: calc(calc(var(--duration) / var(--count)) * calc(2 * 1));
  }
  .shirt:nth-child(4) .base,
  .shirt:nth-child(4) .info,
  .shirt:nth-child(4) .base::after {
    animation-delay: calc(calc(var(--duration) / var(--count)) * calc(3 * 1));
  }
  .shirt:nth-child(5) .base,
  .shirt:nth-child(5) .info,
  .shirt:nth-child(5) .base::after {
    animation-delay: calc(calc(var(--duration) / var(--count)) * calc(4 * 1));
  }
  .shirt:nth-child(6) .base,
  .shirt:nth-child(6) .info,
  .shirt:nth-child(6) .base::after {
    animation-delay: calc(calc(var(--duration) / var(--count)) * calc(5 * 1));
  }

  /* .info::before {
    content: "";
    position: absolute;
    display: block;
    width: 1px;
    top: 0;
    bottom: 0;
    left: -2px;
    border-right: 1px dashed #494b53;
  }
  .shirt[data-biodegradable="false"] .info::before {
    left: initial;
    right: -2px;
    border-right: none;
    border-left: 1px dashed #494b53;
  } */
  .print {
    position: relative;
    border: 1px solid #494b53;
    margin: 12px;
    padding: 12px;
    height: calc(100% - 24px);
    border-radius: 6px;
  }
  .biodegradable {
    height: 32px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 12px;
    border-bottom: 1px solid #494b53;
  }
  .labels {
    height: 32px;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    text-transform: uppercase;
    gap: 8px;
    letter-spacing: 0.05em;
    font-size: 12px;
    border-top: 1px solid #494b53;
  }
  .tagline {
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 12px;
  }

  @keyframes showTagBase {
    0% {
      transform: translate(0, var(--height));
    }
    18% {
      transform: translate(0, 0);
    }
    21% {
      transform: translate(0, 0);
    }
    36% {
      transform: translate(0, calc(-1 * var(--height)));
    }
    100% {
      transform: translate(0, calc(-1 * var(--height)));
    }
  }

  @keyframes showTagInfoLeft {
    0% {
      transform: translate(0, var(--height));
    }
    18% {
      transform: translate(0, 0);
    }
    21% {
      transform: translate(4px, -24px) rotate(-2.5deg);
    }
    36% {
      transform: translate(var(--height), calc(var(--height) * -1.1))
        rotate(60deg);
    }
    100% {
      transform: translate(var(--height), calc(var(--height) * -1.1))
        rotate(60deg);
    }
  }

  @keyframes showTagInfoRight {
    0% {
      transform: translate(0, var(--height));
    }
    18% {
      transform: translate(0, 0);
    }
    21% {
      transform: translate(-4px, -24px) rotate(2.5deg);
    }
    36% {
      transform: translate(calc(-1 * var(--height)), calc(var(--height) * -1.1))
        rotate(-60deg);
    }
    100% {
      transform: translate(var(--height), calc(var(--height) * -1.1))
        rotate(60deg);
    }
  }

  @keyframes cut {
    0% {
      transform: translateY(0);
    }
    18% {
      transform: translateY(0);
    }
    21% {
      transform: translateY(-140px);
    }
    100% {
      transform: translateY(-140px);
    }
  }

  @keyframes cutRight {
    0% {
      transform: translateY(0) rotateY(180deg);
    }
    18% {
      transform: translateY(0) rotateY(180deg);
    }
    21% {
      transform: translateY(-140px) rotateY(180deg);
    }
    100% {
      transform: translateY(-140px) rotateY(180deg);
    }
  }

  @media (max-width: 864px) {
    dl {
      display: none;
    }
  }
</style>
