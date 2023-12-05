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


<section class="online-interview-tips-container">
  {#if (!twoWayBindChild.done[0] && !twoWayBindChild.done[1])}
    <h3 style="margin-bottom: 2rem;">Online Interview Checklist</h3>
    <p>Will you have an online interview?</p>

    <div 
      role="radiogroup"
      style="display:flex;flex-direction:column;" 
    >
      <label for="yay">
        <input name="yay-or-nay" type="radio" id="yay" value="true" bind:group={isHaving}>
        Yes
      </label>
      
      <label for="nay">
        <input name="yay-or-nay" type="radio" id="nay" value="false" bind:group={isHaving}>
        No
      </label>
    </div>

    <button 
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
  {:else if (!twoWayBindChild.done[1])}
    <h3 style="margin-bottom: 2rem;">Online Interview Checklist</h3>
    <div style="display:flex; flex-direction:column;">
      {#each fetchedData as tip, i (tip)}
        <label for={tip}>
          <input type="checkbox" name={tip} id={tip} bind:checked={checkedArr[i]}>
          {tip}
        </label>
      {/each}

      <button disabled={!allChecked} style="margin-top: 1rem;"
        on:click={() => {twoWayBindChild.done[1] = true; collapsed = true; setState()}}
      >proceed</button>
    </div>
  {:else}
    <h3>
      <button class="--unstyled-btn"
        on:click={() => collapsed = !collapsed}
      >Online Interview Checklist <span>{ collapsed ? "+" : "-" }</span></button>
    </h3>

    <div class={`${ !!collapsed ? "--collapsed-element" : ""}`}>
      <button on:click={() => twoWayBindChild.done = [true, false]}>
        {twoWayBindChild.done[0] ? "check again?" : "cheklist"}
      </button>
    </div>
  {/if}

</section>


<style>
  .online-interview-tips-container {
    padding-top: 3rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
