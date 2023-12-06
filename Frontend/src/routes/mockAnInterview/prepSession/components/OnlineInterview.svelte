<script lang="ts">
  export let fetchedData: string[]

  type TState = {
    done: [boolean, boolean]
  }
  export let twoWayBindChild: TState, twoWayBindParent: TState
  const setState = () => twoWayBindParent = twoWayBindChild

  let checkedArr = Array.from({length: fetchedData.length}, () => false)
  $: allChecked = !Boolean(checkedArr.filter(el => !el).length)

  let isHaving: string, collapsed = true
</script>


<section class="prep-session__section">
  {#if (!twoWayBindChild.done[0] && !twoWayBindChild.done[1])}
    <h3 class="prep-section__header">Online Interview Checklist</h3>

    <div class="prep-section__inner-container--working" style="justify-content: center;">
      <p>Will you be having an online interview?</p>

      <div 
        role="radiogroup"
        style="display:flex;flex-direction:row; gap:1.5rem;" 
      >
        <label for="yay">
          <input name="yay-or-nay" type="radio" id="yay" value="true" bind:group={isHaving}>
          <span style="padding-left: 0.4rem;">Yes</span>
        </label>
        
        <label for="nay">
          <input name="yay-or-nay" type="radio" id="nay" value="false" bind:group={isHaving}>
          <span style="padding-left: 0.4rem;">No</span>
        </label>
      </div>
  
      <button
        class="save-btn"
        on:click={() => {
          if(isHaving === "true") {
            twoWayBindChild.done[0] = true
          } else {
            twoWayBindChild.done[1] = true
          }
          setState()
        }}
      >
        Proceed
      </button>
    </div>

  {:else if (!twoWayBindChild.done[1])}
    <h3 class="prep-section__header" style="margin-bottom: 2rem;">Online Interview Checklist</h3>

    <div class="prep-section__inner-container--working" style="justify-content: center;">
      <div style="display: flex; flex-direction: column; gap: 1rem;">
        {#each fetchedData as tip, i (tip)}
          <label for={tip}>
            <input type="checkbox" name={tip} id={tip} bind:checked={checkedArr[i]}>
            <span style="margin-left: 0.8rem;">{tip}</span>
          </label>
        {/each}
      </div>

      <button
        class="save-btn"
        style="margin-top: 1rem;"
        disabled={!allChecked}
        on:click={() => {
          twoWayBindChild.done[1] = true; 
          collapsed = true; 
          setState()
        }}
      >proceed</button>
    </div>
  {:else}
    <h3 class="prep-section__header">
      <button class="--unstyled-btn"
        on:click={() => collapsed = !collapsed}
      >Online Interview Checklist <span class="--collapsed-icon">{ collapsed ? "+" : "-" }</span></button>
    </h3>

    {#if !collapsed}      
      <div class="prep-section__inner-container--done">
        <button 
          class="save-btn" style="margin-top: 1rem;"
          on:click={() => {
            twoWayBindChild.done = [true, false]
            setState()
          }
        }>
          {twoWayBindChild.done[0] ? "check again?" : "cheklist"}
        </button>
      </div>
    {/if}
  {/if}

</section>


<style>
</style>
