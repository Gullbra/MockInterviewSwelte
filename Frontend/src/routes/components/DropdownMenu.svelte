<script lang="ts">
  export let title: string
  export let menuItems: {
    title: string,
    path: string
  }[]
</script>


<nav class="links-container__dropdown-container dev-border">
  <h4 class="links-container__dropdown-header">{title}</h4>
  
  <div class="links-container__dropdown-menu">
    {#each menuItems as menuItem (menuItem.title)}
      <p class="dropdown-menu__dropdown-element">
        <a href={menuItem.path}>{menuItem.title}</a>
      </p>
    {/each}
  </div>
</nav>


<style>
 .links-container__dropdown-container {
    position: relative;
    --dropdown-max-height: 0;

    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }
  .links-container__dropdown-container:hover {
    --dropdown-max-height: 60rem;
  }
  /* .links-container__dropdown-header {} */
  /* .links_container__invisible-dropdown-wrapper {
    position: absolute;
  } */
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
