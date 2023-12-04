<script lang="ts">
  export let data

  interface IPrepdata {
    research: {
      Appearence: string[],
      onlineInterview: string[],
      research: string[]
    },
    generalTips: string[]
  }

  const prepData = data as IPrepdata

  let progress = {
    research: {
      done: false,
      data: Array.from({length: prepData.research.research.length}, () => "")
    }
  }

  $: currentCheckpoint = 0

  const collapsed = {
    reserch: {
      coll: true,
      subfields: Array.from({length: prepData.research.research.length}, () => true),
      editing: {
        isEditing: Array.from({length: prepData.research.research.length}, () => false),
        value: Array.from({length: prepData.research.research.length}, () => "")
      }
    }
  }
</script>


<div class="prep-session-container">
  <h3>test: prep session</h3>

  <section class="prep-research-section">
    {#if (!progress.research.done && currentCheckpoint < prepData.research.research.length)}

      <h4>{prepData.research.research[currentCheckpoint]}</h4>

      <textarea
        style="margin-top: 1rem;" placeholder="...write answer here" 
        class="text-area-input" 
        bind:value={progress.research.data[currentCheckpoint]}/>

      <button
        class="save-btn" 
        on:click|preventDefault={() => {
          currentCheckpoint += 1
          if (currentCheckpoint >= prepData.research.research.length) {
            collapsed.reserch.editing.value = progress.research.data.slice()
            progress.research.done = true
          }
        }}
      >Save</button>

    {:else}
      <h3>
        <button class="--unstyled-btn"
          on:click={() => collapsed.reserch.coll = !collapsed.reserch.coll}
          >Research <span>{ collapsed.reserch.coll ? "+" : "-"}</span></button>
      </h3>

      <div class={ !!collapsed.reserch.coll ? "--colapsed-closed" : "" }>

        {#each prepData.research.research as litItem, i ("list, research, " + litItem)}
          <div class="prep-research-section" style="margin-top: 0.5rem;">
            <h5><button class="--unstyled-btn"
              on:click={() => collapsed.reserch.subfields[i] = !collapsed.reserch.subfields[i]}
            >{litItem} <span>{ collapsed.reserch.subfields[i] ? "+" : "-"}</span></button></h5>

            
            <div class={ `flex-col-center ${!!collapsed.reserch.subfields[i] ? "--colapsed-closed" : ""}`}>
              {#if !collapsed.reserch.editing.isEditing[i]}
                <p>{progress.research.data[i] || "not entered"}</p>
              {:else}
                <textarea
                  style="margin-top: 1rem;" placeholder="...write answer here" 
                  class="text-area-input" 
                  bind:value={collapsed.reserch.editing.value[i]}/>

                <button on:click={() => {
                  console.log(litItem, i, collapsed.reserch.editing.value)
                  console.log("saving?", progress.research.data[i], "=>", collapsed.reserch.editing.value[i])
                  progress.research.data[i] = collapsed.reserch.editing.value[i]
                  console.log(progress)
                  collapsed.reserch.editing.isEditing[i] = !collapsed.reserch.editing.isEditing[i]
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

</div>

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

  .--colapsed-closed {
    height: 0;
    overflow: hidden;
  }

  .--unstyled-btn {
    background: none;
    color: inherit;
    border: none;
    padding: 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
  }

  .flex-col-center {
    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
