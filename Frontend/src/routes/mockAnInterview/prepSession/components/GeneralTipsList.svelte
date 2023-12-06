<script lang="ts">
  export let fetchedData: string[]

  let collapsed = false
</script>


<section class="prep-session__section">
  <h3 class="prep-section__header">
    <button class="--unstyled-btn"
      on:click={() => collapsed = !collapsed}
    >General tips <span class="--collapsed-icon">{ collapsed ? "+" : "-" }</span></button>
  </h3>

  {#if !collapsed}
    <div class="prep-section__inner-container--working">
      <div class="inner__list">
        {#each fetchedData as tip (tip)}
          <p>{tip}</p>
        {/each}
      </div>
    </div>
  {/if}
</section>


<style>
  .inner__list {
    display: flex; flex-direction: column; gap: 1rem;
  }
</style>
