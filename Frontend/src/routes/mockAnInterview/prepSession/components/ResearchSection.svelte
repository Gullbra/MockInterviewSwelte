<script lang="ts">
  export let fetchedData: string[]
  
  interface IState { 
    done: boolean, 
    data: string[] 
  }
  export let twoWayBindChild: IState, twoWayBindParent: IState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  $: currentCheckpoint = 0

  const collapsed = {
    all: true,
    subfields: Array.from({length: fetchedData.length}, () => true),
    editing: {
      isEditing: Array.from({length: fetchedData.length}, () => false),
      value: Array.from({length: fetchedData.length}, () => "")
    }
  }
</script>


<section class="prep-session__section">
  {#if (!twoWayBindChild.done && currentCheckpoint < fetchedData.length)}
    <h3 class="prep-section__header">Research</h3>

    <h4 class="research-question">{`Q: ${fetchedData[currentCheckpoint]}`}</h4>

    <textarea
      style="margin-top: 1rem;" placeholder="...write answer here" 
      class="text-area-input" 
      bind:value={twoWayBindChild.data[currentCheckpoint]}/>

    <button
      class="save-btn" 
      on:click|preventDefault={() => {
        currentCheckpoint += 1
        if (currentCheckpoint >= fetchedData.length) {
          collapsed.editing.value = twoWayBindChild.data.slice()
          twoWayBindChild.done = true
        }

        stateChange()
      }}
    >Save</button>

  {:else}
    <h3 class="prep-section__header">
      <button class="--unstyled-btn"
        on:click={() => collapsed.all = !collapsed.all}
        >Research <span class="--collapsed-icon">{ collapsed.all ? "+" : "-" }</span></button>
    </h3>

    <div class={ !!collapsed.all ? "--collapsed-element" : "" }>

      {#each fetchedData as litItem, i ("list, research, " + litItem)}
        <div class="prep-session__section" style="margin-top: 0.5rem;">
          <h5><button class="--unstyled-btn"
            on:click={() => collapsed.subfields[i] = !collapsed.subfields[i]}
          >{litItem} <span class="--collapsed-icon">{ collapsed.subfields[i] ? "+" : "-"}</span></button></h5>

          
          <div class={ `flex-col-center ${!!collapsed.subfields[i] ? "--collapsed-element" : ""}`}>
            {#if !collapsed.editing.isEditing[i]}
              <p>{twoWayBindChild.data[i] || "not entered"}</p>
            {:else}
              <textarea
                style="margin-top: 1rem;" placeholder="...write answer here" 
                class="text-area-input" 
                bind:value={collapsed.editing.value[i]}/>

              <button on:click={() => {
                twoWayBindChild.data[i] = collapsed.editing.value[i]
                collapsed.editing.isEditing[i] = !collapsed.editing.isEditing[i]
                stateChange()
              }}>replace</button>
            {/if}
            <button on:click={() => collapsed.editing.isEditing[i] = !collapsed.editing.isEditing[i] }>
              {!collapsed.editing.isEditing[i] ? "change": "cancel"}
            </button>
          </div>

        </div>
      {/each}

    </div>
  {/if}
</section>


<style>
  .research-toggle-btn {
    margin-top: 2rem;
  }

  .save-btn {
    padding: 0.3rem 0.4rem;
    margin-top: 1rem;
  }
</style>
