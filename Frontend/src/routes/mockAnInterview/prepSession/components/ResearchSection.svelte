<script lang="ts">
  export let fetchedData: {
    research: {
      Appearence: string[],
      onlineInterview: string[],
      research: string[]
    },
    generalTips: string[]
  }
  
  type IState = { 
    done: boolean, 
    data: string[] 
  }
  export let twoWayBindChild: IState, twoWayBindParent: IState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  $: currentCheckpoint = 0

  const collapsed = {
    reserch: {
      coll: true,
      subfields: Array.from({length: fetchedData.research.research.length}, () => true),
      editing: {
        isEditing: Array.from({length: fetchedData.research.research.length}, () => false),
        value: Array.from({length: fetchedData.research.research.length}, () => "")
      }
    }
  }
</script>


<section class="prep-research-section">
  {#if (!twoWayBindChild.done && currentCheckpoint < fetchedData.research.research.length)}
    <h3 style="margin-bottom: 2rem;">Research</h3>

    <h4>{fetchedData.research.research[currentCheckpoint]}</h4>

    <textarea
      style="margin-top: 1rem;" placeholder="...write answer here" 
      class="text-area-input" 
      bind:value={twoWayBindChild.data[currentCheckpoint]}/>

    <button
      class="save-btn" 
      on:click|preventDefault={() => {
        currentCheckpoint += 1
        if (currentCheckpoint >= fetchedData.research.research.length) {
          collapsed.reserch.editing.value = twoWayBindChild.data.slice()
          twoWayBindChild.done = true
        }

        stateChange()
      }}
    >Save</button>

  {:else}
    <h3>
      <button class="--unstyled-btn"
        on:click={() => collapsed.reserch.coll = !collapsed.reserch.coll}
        >Research <span>{ collapsed.reserch.coll ? "+" : "-" }</span></button>
    </h3>

    <div class={ !!collapsed.reserch.coll ? "--collapsed-element" : "" }>

      {#each fetchedData.research.research as litItem, i ("list, research, " + litItem)}
        <div class="prep-research-section" style="margin-top: 0.5rem;">
          <h5><button class="--unstyled-btn"
            on:click={() => collapsed.reserch.subfields[i] = !collapsed.reserch.subfields[i]}
          >{litItem} <span>{ collapsed.reserch.subfields[i] ? "+" : "-"}</span></button></h5>

          
          <div class={ `flex-col-center ${!!collapsed.reserch.subfields[i] ? "--collapsed-element" : ""}`}>
            {#if !collapsed.reserch.editing.isEditing[i]}
              <p>{twoWayBindChild.data[i] || "not entered"}</p>
            {:else}
              <textarea
                style="margin-top: 1rem;" placeholder="...write answer here" 
                class="text-area-input" 
                bind:value={collapsed.reserch.editing.value[i]}/>

              <button on:click={() => {
                twoWayBindChild.data[i] = collapsed.reserch.editing.value[i]
                collapsed.reserch.editing.isEditing[i] = !collapsed.reserch.editing.isEditing[i]
                stateChange()
              }}>replace</button>
            {/if}
            <button on:click={() => collapsed.reserch.editing.isEditing[i] = !collapsed.reserch.editing.isEditing[i] }>
              {!collapsed.reserch.editing.isEditing[i] ? "change": "cancel"}
            </button>
          </div>

        </div>
      {/each}

    </div>
  {/if}
</section>


<style>
  .prep-session-container {
    padding-top: 3rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }

  .prep-research-section {
    margin-top: 2rem;
    display: flex;
    flex-direction: column; align-items: center;
  }

  .research-toggle-btn {
    margin-top: 2rem;
  }

  .save-btn {
    padding: 0.3rem 0.4rem;
    margin-top: 1rem;
  }
</style>
