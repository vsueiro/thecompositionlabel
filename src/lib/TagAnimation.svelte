<style>
  swiper-container {
    background: Plum;
  }

  swiper-slide {
    display: flex;
    align-items: center;
    height: 100%;
  }

  .tag {
    background: white;
    border: 1px solid black;
    padding: 16px;
    width: fit-content;
    user-select: none;
  }
</style>


<swiper-container
  direction="vertical"
  height="400"
  auto-height="true"
  autoplay-delay="1500"
  autoplay-disable-on-interaction="false"
  loop="true"
  allow-touch-move="false"
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