<script lang="ts">
  export let fetchedData: {
    question: string,
    desc: string
  }[]
  
  interface IState { 
    done: boolean, 
    data: string[] 
  }
  export let twoWayBindChild: IState, twoWayBindParent: IState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  $: currentCheckpoint = 0

  const collapsed = {
    all: false,
    subfields: Array.from({length: fetchedData.length}, () => true),
    editing: {
      isEditing: Array.from({length: fetchedData.length}, () => false),
      value: Array.from({length: fetchedData.length}, () => "")
    }
  }
</script>


<section class="prep-session__section">

  <h3 class="prep-section__header">
    <button class="--unstyled-btn"
      on:click={() => collapsed.all = !collapsed.all}
      >Research <span class="--collapsed-icon">{ collapsed.all ? "+" : "-" }</span></button>
  </h3>

  {#if !collapsed.all}
    {#if (!twoWayBindChild.done && currentCheckpoint < fetchedData.length)}

      <div class="prep-section__inner-container--working">
        <div>
          <p style="text-align: center;"><i>"By failing to prepare you are preparing to fail"</i></p>
          <p style="text-align: center; margin-top: 1.3rem;">Find out and write down the answers to the successive questions below.</p>
        </div>

        <div style="display: flex; flex-direction:column; align-items:center; gap:1.3rem;">
          <h4 style="margin-top:1rem; display:flex; flex-direction:row; gap: 0.7rem; max-width:90%; text-align: center;">
            <div style="display: flex; align-items:center;">{"Q:"}</div>
            <div >{`${fetchedData[currentCheckpoint].question}`}</div>
          </h4>
          <p style="text-align:center;">{`${fetchedData[currentCheckpoint].desc}`}</p>
        </div>

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
      </div>

    {:else}

      <div class="prep-section__inner-container--done" style="padding-left: 10%; padding-right:5%;">
 
        {#each fetchedData as litItem, i ("list, research, " + litItem.question)}
          <div class="" style="margin-top: 0.5rem;">
            <h5>
              <button class="--unstyled-btn" style="text-align:start;" on:click={() => collapsed.subfields[i] = !collapsed.subfields[i]}>
                {litItem.question}
                <span class="--collapsed-icon" style="align-self: center;">{ collapsed.subfields[i] ? "+" : "-"}</span>
              </button>
            </h5>
  
            {#if !collapsed.subfields[i]}
              <div 
                style="padding-top: 0.8rem; padding-bottom:0.8rem; padding-left:2rem; padding-right:0.5rem; width:fit-content; display: flex; flex-direction: row; align-items: center; gap:1rem;"
              >
                {#if !collapsed.editing.isEditing[i]}
                  <p>{twoWayBindChild.data[i] || "Not Entered"}</p>
                {:else}
                  <textarea
                    style="margin-top: 1rem;" placeholder="...write answer here" 
                    class="text-area-input" 
                    bind:value={collapsed.editing.value[i]}/>
    
                  <button class="save-btn" on:click={() => {
                    twoWayBindChild.data[i] = collapsed.editing.value[i]
                    collapsed.editing.isEditing[i] = !collapsed.editing.isEditing[i]
                    stateChange()
                  }}>replace</button>
                {/if}
                <button class="save-btn" on:click={() => collapsed.editing.isEditing[i] = !collapsed.editing.isEditing[i] }>
                  {!collapsed.editing.isEditing[i] ? "change": "cancel"}
                </button>
              </div>
            {/if}

          </div>
        {/each}

      </div>

    {/if}
  {/if}
</section>


<style>
</style>
