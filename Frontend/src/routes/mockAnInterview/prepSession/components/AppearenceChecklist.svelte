<script lang="ts">
  export let fetchedData: string[]

  type TState = {done:boolean}
  export let twoWayBindParent: TState, twoWayBindChild: TState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  let checkedArr = Array.from({length: fetchedData.length}, () => false)
  $: allChecked = !Boolean(checkedArr.filter(el => !el).length)

  let collapsed = false
</script>


<section class="prep-session__section">

  <h3 class="prep-section__header">
    <button class="--unstyled-btn"
      on:click={() => collapsed = !collapsed}
    >Appearence Checklist <span class="--collapsed-icon">{ collapsed ? "+" : "-" }</span></button>
  </h3>

  {#if !collapsed}
    {#if !twoWayBindChild.done}

      <div class="prep-section__inner-container--working" style="justify-content: center; gap: 1rem;">
        <div>
          <div style="display: flex; flex-direction: column; gap: 1rem;">
            {#each fetchedData as tip, i (tip)}
              <label for={tip}>
                <input type="checkbox" name={tip} id={tip} bind:checked={checkedArr[i]}>
                <span style="margin-left: 0.8rem;">{tip}</span>
              </label>
            {/each}
          </div>
        </div>

        <button
          class="save-btn"
          style="margin-top: 1rem;"
          disabled={!allChecked}
          on:click={() => {
            twoWayBindChild.done = true; 
            collapsed = true; 
            stateChange()
          }}
        >proceed</button>
      </div>
      
    {:else}
      <div class="prep-section__inner-container--done">
        <button 
          class="save-btn" style="margin-top: 1rem;"
          on:click={() => {
            twoWayBindChild.done = false
            stateChange()
          }}>check again?</button>
      </div>
    {/if}
  {/if}
</section>


<style>
</style>
