<script>
  import { onMount } from "svelte";

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

  const duration = 6;

  onMount(() => {
    let tags = document.querySelectorAll(".tag");
    let index = 0;

    setInterval(() => {
      tags.forEach((tag, i) => {
        const isCurrent = i === index;
        tag.style.opacity = isCurrent ? 1 : 0;
        tag.style.animationPlayState = isCurrent ? "running" : "paused";
      });

      index++;
      if (index > tags.length - 1) {
        index = 0;
      }
    }, duration * 1000);
  });
</script>

<dl>
  {#each tags as tag}
    <div class="shirt">
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
    --height: 70vh;
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
    box-shadow: inset 0 0 48px #ceb8d280;
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
    left: calc(0 + 16px);
    top: calc(32px + 16px);
    bottom: 32px;
    width: 48px;
  }
  .shirt {
    height: 100%;
    display: flex;
    align-items: center;
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
  }
  .tag {
    width: fit-content;
    display: flex;
  }
  .base {
    position: relative;
    width: 32px;
    background: white;

    transform: translate(0, var(--height));
    animation: showTagBase 6s infinite;
  }
  .base::before {
    content: "";
    position: absolute;
    display: block;
    width: 1px;
    top: 0;
    bottom: 0;
    right: -1px;
    border-right: 1px dashed white;
  }
  .info {
    position: relative;
    width: 384px;
    height: 176px;
    background: white;
    border-left: 1px dashed white;
    margin-left: 2px;
    transform: translate(0, var(--height));
    animation: showTagInfo 6s infinite;
  }
  .info::before {
    content: "";
    position: absolute;
    display: block;
    width: 1px;
    top: 0;
    bottom: 0;
    left: -2px;
    border-right: 1px dashed white;
  }
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
    50% {
      transform: translate(0, 0);
    }
    60% {
      transform: translate(0, 0);
    }
    100% {
      transform: translate(0, calc(-1 * var(--height)));
    }
  }

  @keyframes showTagInfo {
    0% {
      transform: translate(0, var(--height));
    }
    50% {
      transform: translate(0, 0);
    }
    60% {
      transform: translate(0, -20px);
    }
    100% {
      transform: translate(var(--height), calc(var(--height) * -1.1))
        rotate(60deg);
    }
  }
</style>
