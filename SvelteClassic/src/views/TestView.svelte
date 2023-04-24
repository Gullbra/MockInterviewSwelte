<script lang="ts">
  export let name: string;
</script>

<h1 class="tutorial__header">Hello {name}!</h1>
<p>Visit the 
  <a href="https://svelte.dev/tutorial">
    Svelte tutorial
  </a> to learn how to build Svelte apps.
</p>

<style>
	.tutorial__header {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>