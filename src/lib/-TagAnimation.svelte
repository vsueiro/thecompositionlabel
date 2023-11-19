<script>
  import { onMount } from "svelte";

  onMount(() => {
    const swiperEl = document.querySelector("swiper-container");

    swiperEl.addEventListener("swiperslidechangetransitionstart", (event) => {
      const [swiper] = event.detail;
      console.log(swiper);
      const prev = swiper.slides[swiper.realIndex - 1];
      const current = swiper.slides[swiper.realIndex];
      const next = swiper.slides[swiper.realIndex + 1];

      // if (prev){
      prev.style.background = "red";

      // current.style.background = 'blue'
      next.style.background = "blue";
    });
  });
</script>

<swiper-container
  direction="vertical"
  height="400"
  auto-height="true"
  autoplay-delay="1500"
  autoplay-disable-on-interaction="false"
  loop="true"
  allow-touch-move="false"
  speed="1000"
>
  <swiper-slide>
    <div class="tag">Cool Material</div>
  </swiper-slide>
  <swiper-slide>
    <div class="tag">Nicest Material</div>
  </swiper-slide>
  <swiper-slide>
    <div class="tag">A Material</div>
  </swiper-slide>
  <swiper-slide>
    <div class="tag">Lovely Material</div>
  </swiper-slide>
</swiper-container>

<style>
  swiper-container {
    background: Plum;
  }

  swiper-slide {
    display: flex;
    align-items: center;
    height: 100%;
    background: pink;
    transition: all 1s;
  }

  .tag {
    background: white;
    border: 1px solid black;
    padding: 16px;
    width: fit-content;
    user-select: none;
    transition: all 1s;
  }

  /* swiper-slide.swiper-slide-active {
    background: blue !important;
  } */
</style>
