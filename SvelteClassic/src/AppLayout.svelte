<script lang="ts">
</script>


<header class="site__header">
  <h1 class="site-header__header-element">My Test Header</h1>
</header>

<main>
  <slot/>
</main>

<footer class="site__footer">
  hey
</footer>


<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  .site__header {
    height: 6rem;
    display: flex; justify-content: center; align-items: center;
    background-color: #ff3e00;
  }
  .site__footer {
    width: 100%;
    display: flex; justify-content: center; align-items: center;
    position: fixed; bottom: 0;
    background-color: #ff3e00;
    height: 4rem;
  }
  .site-header__header-element {
    color: white;
    text-transform: uppercase;

		font-weight: 100;
  }


	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>