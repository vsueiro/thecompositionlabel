<script>
  import { onMount } from "svelte";

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
  <div class="shirt">
    <div class="tag">
      <div class="base" />
      <div class="info">
        <div class="print">
          <dt>Cotton</dt>
          <dd>…</dd>
        </div>
      </div>
    </div>
  </div>
  <div class="shirt">
    <div class="tag">
      <div class="base" />
      <div class="info">
        <div class="print">
          <dt>Polyester</dt>
          <dd>…</dd>
        </div>
      </div>
    </div>
  </div>
  <div class="shirt">
    <div class="tag">
      <div class="base" />
      <div class="info">
        <div class="print">
          <dt>Metallic Fibers</dt>
          <dd>…</dd>
        </div>
      </div>
    </div>
  </div>
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
