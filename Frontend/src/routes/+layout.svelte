<script lang="ts">
  import '../styles/base.css'

  
</script>


<header class="site__header">
  <h1>Site Title</h1>
  <nav class="header__links-container">
    <a href="/preparation">Preparation</a>
  </nav>
</header>

<main>
  <slot/>
</main>


<style>
  .site__header {
    width: 100%; height: 6rem;

    background-color: blueviolet;

    display: flex;
    flex-direction: column;
    align-items: center;

  }
  .header__links-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>