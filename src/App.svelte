<script>
	import TagAnimation from "./lib/TagAnimation.svelte";
	import FilteredList from "./lib/FilteredList.svelte";

	// import function to register Swiper custom elements
	import { register } from 'swiper/element/bundle';
	// register Swiper custom elements
	register();	
</script>

<main>
	<TagAnimation />
	<FilteredList />
</main>