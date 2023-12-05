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

  <div 
    class={`${ !!collapsed ? "--collapsed-element" : ""}`}
    style="display:flex; flex-direction:column; align-items: center;"
  >
    {#each fetchedData as tip (tip)}
      <p>{tip}</p>
    {/each}
  </div>
</section>


<style>
</style>
