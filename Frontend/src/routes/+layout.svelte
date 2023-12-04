<script lang="ts">
  import '../styles/base.css'
  import '../styles/colors.css'
  import '../styles/fonts.css'

  import DropdownMenu from './components/DropdownMenu.svelte'

  const navbarData = [
    { 
      menuTitle: "Site navigation",
      menuItems: [
        { title: "Mock an Interview", path: "/mockAnInterview" },
        { title: "Preparation", path: "/preparation" },
        { title: "Webcam test", path: "/web-cam-test" },
        { title: "About", path: "/about" },
      ]
    },
    { 
      menuTitle: "Svelte Tutorial",
      menuItems: [
        { title: "Svelte tutorial start", path: "https://learn.svelte.dev/tutorial/welcome-to-svelte" },
        { path: "https://learn.svelte.dev/tutorial/welcome-to-svelte", title: "Svelte tutorial" },
        { path: "https://learn.svelte.dev/tutorial/reactive-declarations", title: "Svelte states" },
        { path: "https://learn.svelte.dev/tutorial/declaring-props", title: "Svelte props and imports" },
        { path: "https://learn.svelte.dev/tutorial/default-values", title: "Svelte default props" },
        { path: "https://learn.svelte.dev/tutorial/spread-props", title: "Svelte spread props" },
        { path: "https://learn.svelte.dev/tutorial/else-if-blocks", title: "Svelte if/else" },
        { path: "https://learn.svelte.dev/tutorial/each-blocks", title: "Svelte loops/maps" },
        { path: "https://learn.svelte.dev/tutorial/keyed-each-blocks", title: "Svelte keyed each" },
        { path: "https://learn.svelte.dev/tutorial/await-blocks", title: "Svelte promise-handling" },
        { path: "https://learn.svelte.dev/tutorial/dom-events", title: "Svelte events" },
        { path: "https://learn.svelte.dev/tutorial/event-modifiers", title: "Svelte event modifiers" },
        { path: "https://learn.svelte.dev/tutorial/component-events", title: "Svelte components events" },
        { path: "https://learn.svelte.dev/tutorial/text-inputs", title: "Svelte inputs" },
        { path: "https://learn.svelte.dev/tutorial/onmount", title: "Svelte onMount" },
      ]
    },
    { 
      menuTitle: "Other Tutorials",
      menuItems: [
        { title: "Webcam + Svelte", path: "https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415" },
        { title: "Links css", path: "https://codepen.io/martinwolf/pen/eNNdme" },
        { title: "Color palette", path: "https://colorhunt.co/palette/fefbe9e1eeddf0a04b183a1d" },
      ]
    },
  ]

</script>


<header class="site__header">
  <h1><a href="/">Site Title E</a></h1>

  <nav class="header__links-container">
    {#each navbarData as navItem (navItem.menuTitle)}
      <DropdownMenu title={navItem.menuTitle} menuItems={navItem.menuItems}/>
    {/each}
  </nav>
</header>

<!--
  https://codepen.io/martinwolf/pen/eNNdme
  https://colorhunt.co/palette/fefbe9e1eeddf0a04b183a1d
-->

<main class="site__main">
  <slot/>
</main>


<style>
  :root {
    --header-height: 8rem;
  }


  .site__header {
    padding-left: 2rem; padding-right: 4rem;

    width: 100%; height: var(--header-height);

    background-color: var(--dark-blue);

    display: flex; flex-direction: row;
    align-items: center; justify-content: space-between;
  }
  .site__main {    
    width: 100%; height: calc(100vh - var(--header-height));
  }


  .header__links-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
  }
</style>