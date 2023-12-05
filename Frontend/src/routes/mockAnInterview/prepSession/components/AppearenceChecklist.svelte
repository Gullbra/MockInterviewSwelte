<script lang="ts">
  export let fetchedData: string[]

  type TState = {done:boolean}
  export let twoWayBindParent: TState, twoWayBindChild: TState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  let checkedArr = Array.from({length: fetchedData.length}, () => false)
  $: allChecked = !Boolean(checkedArr.filter(el => !el).length)

  let collapsed = true
</script>


<section class="prep-session__section">
  {#if !!twoWayBindChild.done}
    <h3 class="prep-section__header">
      <button class="--unstyled-btn"
        on:click={() => collapsed = !collapsed}
      >Appearence Checklist <span class="--collapsed-icon">{ collapsed ? "+" : "-" }</span></button>
    </h3>

    <div class={`${ !!collapsed ? "--collapsed-element" : ""}`}>
      <button on:click={() => twoWayBindChild.done = false}>check again?</button>
    </div>
  {:else}
    <!-- style="margin-bottom: 2rem;" -->
    <h3 class="prep-section__header">Appearence Checklist</h3>

    <div style="display:flex; flex-direction:column;">
      {#each fetchedData as tip, i (tip)}
        <label for={tip}>
          <input type="checkbox" name={tip} id={tip} bind:checked={checkedArr[i]}>
          {tip}
        </label>
      {/each}
 
      <button disabled={!allChecked} style="margin-top: 1rem;"
        on:click={() => {twoWayBindChild.done= true; collapsed = true; stateChange()}}
      >proceed</button>
    </div>
  {/if}
</section>


<style>
</style>
