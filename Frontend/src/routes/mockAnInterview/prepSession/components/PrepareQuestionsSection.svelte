<script lang="ts">
  export let fetchedData: {
    question: string,
    desc: string,
    tips: string[]
  }

  interface IState { 
    done: boolean, 
    data: string[] 
  }
  export let twoWayBindChild: IState, twoWayBindParent: IState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  let workingQuestion = ""

  let collapsed = {
    section: false,
    tips: true
  }
</script>


<section class="prep-session__section">

  <h3 class="prep-section__header">
    <button class="--unstyled-btn"
      on:click={() => collapsed.section = !collapsed.section}
    >Prepare Questions to Ask <span class="--collapsed-icon">{ collapsed.section ? "+" : "-" }</span></button>
  </h3>

  {#if !collapsed.section}

    {#if (!twoWayBindChild.done)}
      <div class="prep-section__inner-container--working">
        <p style="margin-top: 1rem;"><i>Prepare a couple of questions to ask: It's a good way of showing both you interest and your understanding.</i></p>

        {#if twoWayBindChild.data.length > 0}  
          <div style="display: flex; flex-direction:column; gap: 0.4rem;">

            {#each twoWayBindChild.data as sQuestion, i (sQuestion)}
              <div style="display: flex; flex-direction:row; justify-content:space-between; gap:0.7rem;">
                <p style="color: rgb(95, 94, 94);">{sQuestion}</p>

                <button
                  on:click={() => {
                    twoWayBindChild.data = twoWayBindChild.data
                      .slice(0,i)
                      .concat(twoWayBindChild.data.slice(i+1))
                      .map((el, index) => (index + 1) + '.' + el.split('.').slice(1).join('.'))
          
                    stateChange()
                  }
                }>delete</button>
              </div>
            {/each}
          </div>
        {/if}
    
        <textarea
          style="" 
          placeholder="...write your question here" 
          class="text-area-input" 
          bind:value={workingQuestion}
        />

        <h4>
          <button class="--unstyled-btn"
            on:click={() => collapsed.tips = !collapsed.tips}
          >Show tips <span class="--collapsed-icon">{ collapsed.tips ? "+" : "-" }</span></button>
        </h4>

        {#if !collapsed.tips}
          {#each fetchedData.tips as tip, i (tip + i)}          
            <p>{tip}</p>
          {/each}
        {/if}
    
        <div>
          <button
            class="save-btn" 
            on:click|preventDefault={() => {
              twoWayBindChild.data[twoWayBindChild.data.length] = `${twoWayBindChild.data.length+1}. ${workingQuestion}` 
              workingQuestion = ""
              stateChange()
            }}
          >Save</button>
    
          <button class="save-btn" 
            on:click={() => {
              twoWayBindChild.done = true; 
              collapsed.section = true
              stateChange()
            }}
          >{twoWayBindChild.data.length === 0 ? "Skip" : "Done"}</button>
        </div>
      </div>

    {:else}
      <div class="prep-section__inner-container--done" style="display: flex; flex-direction: column; gap: 0.3rem;">
        {#each twoWayBindChild.data as sQuestion (sQuestion)}
          <p style="color: rgb(95, 94, 94);">{sQuestion}</p>
        {/each}

        <button class="save-btn" style="margin-top: 1rem; width: fit-content; align-self: center;" on:click={() => {
          twoWayBindChild.done = false
          stateChange()
        }}>{twoWayBindChild.data.length === 0 ? "Add" : "Edit"}</button>
      </div>
    {/if}

  {/if}
</section>

<style>
</style>
