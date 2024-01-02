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
              <span>{tag.name}</span>
              <span>{tag.tagline}</span>
            </dt>
            <dd>
              <img src="assets/icons/{tag.icon}" alt="" />
              <div class="biodegradable">
                {tag.biodegradable ? "Biodegradable" : "Non-Biodegradable"}
              </div>
              <div class="labels">
                {#each tag.labels as label}
                  <span>{label}</span>
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
    width: 24px;
    background: white;
    border-right: 1px dashed black;
    transform: translate(0, var(--height));
    animation: showTagBase 6s infinite;
  }
  .info {
    padding: 16px;
    min-width: 120px;
    background: white;
    border-left: 1px dashed black;
    transform: translate(0, var(--height));
    animation: showTagInfo 6s infinite;
  }
  .print {
    border: 1px solid black;
    padding: 16px;
  }
  dd {
    margin: 0;
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
