<script lang="ts">
  import '../styles/base.css'
  import '../styles/colors.css'
  import '../styles/fonts.css'
</script>


<header class="site__header">
  <h1><a href="/">Site Title E</a></h1>
  <nav class="header__links-container">
    <nav class="links-container__dropdown-container dev-border">
      <h4 class="links-container__dropdown-header">Site Navigation</h4>
      
      <div class="links-container__dropdown-menu">
        <p class="dropdown-menu__dropdown-element"><a href="/preparation">/preparation</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="/web-cam-test">/webcam test</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="/about">/about</a></p>
      </div>
    </nav>
    <nav class="links-container__dropdown-container">
      <h4 class="links-container__dropdown-header">Other Tutorials</h4>
      <div class="links-container__dropdown-menu">
        <p class="dropdown-menu__dropdown-element"><a href="https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415">Webcam + Svelte</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://codepen.io/martinwolf/pen/eNNdme">Links css</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://colorhunt.co/palette/fefbe9e1eeddf0a04b183a1d">Color palette</a></p>
      </div>
    </nav>
    <nav class="links-container__dropdown-container">
      <h4 class="links-container__dropdown-header">Svelte Tutorial</h4>
      <div class="links-container__dropdown-menu">
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/welcome-to-svelte">Svelte tutorial</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/reactive-declarations">Svelte states</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/declaring-props">Svelte props and imports</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/default-values">Svelte default props</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/spread-props">Svelte spread props</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/else-if-blocks">Svelte if/else</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/each-blocks">Svelte loops/maps</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/keyed-each-blocks">Svelte keyed each</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/await-blocks">Svelte promise-handling</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/dom-events">Svelte events</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/event-modifiers">Svelte event modifiers</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/component-events">Svelte components events</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/text-inputs">Svelte inputs</a></p>
        <p class="dropdown-menu__dropdown-element"><a href="https://learn.svelte.dev/tutorial/onmount">Svelte onMount</a></p>
      </div>
    </nav>
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
  .links-container__dropdown-container {
    position: relative;
    --dropdown-max-height: 0;

    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }
  .links-container__dropdown-container:hover {
    --dropdown-max-height: 60rem;
  }
  /* .links-container__dropdown-header {} */
  .links_container__invisible-dropdown-wrapper {
    position: absolute;
  }
  .links-container__dropdown-menu {
    width: 8rem; max-height: var(--dropdown-max-height); 

    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;

    position: absolute; top: 1rem;
    overflow-y: hidden;
    background-color: var(--medium-light-blue);
  }
  .dropdown-menu__dropdown-element {
    width: 100%;
    padding: 0.3rem 0.5rem;
    border: 1px solid black;
    text-align: center;
  }
</style>