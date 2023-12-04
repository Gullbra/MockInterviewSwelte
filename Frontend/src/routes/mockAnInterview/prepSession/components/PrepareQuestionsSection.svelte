<script lang="ts">
  type IState = { 
    done: boolean, 
    data: string[] 
  }
  export let twoWayBindChild: IState, twoWayBindParent: IState
  const stateChange = () => twoWayBindParent = twoWayBindChild

  let workingQuestion = ""

  let collapsed = {
    coll: true
  }
</script>

<section class="prepare-questions-section flex-col-center">
  {#if (!twoWayBindChild.done)}
    <h3>Prepare Questions to Ask</h3>
    <p style="margin-top: 1rem;"><i>Prepare a couple of questions to ask: It's a good way of showing both you interest and your understanding.</i></p>

    <div class="">
      {#each twoWayBindChild.data as sQuestion, i (sQuestion)}
        <p style="color: rgb(95, 94, 94);">{sQuestion}</p><button on:click={() => {
          twoWayBindChild.data = twoWayBindChild.data
            .slice(0,i)
            .concat(twoWayBindChild.data.slice(i+1))
            .map((el, index) => (index + 1) + '.' + el.split('.').slice(1).join('.'))

          stateChange()
        }}>delete</button>
      {/each}
    </div>

    <textarea
      style="margin-top: 1rem;" 
      placeholder="...write your question here" 
      class="text-area-input" 
      bind:value={workingQuestion}/>

    <button
      class="save-btn" 
      on:click|preventDefault={() => {
        twoWayBindChild.data[twoWayBindChild.data.length] = `${twoWayBindChild.data.length+1}. ${workingQuestion}` 
        workingQuestion = ""
        stateChange()
      }}
    >Save</button>

    <button on:click={() => {twoWayBindChild.done = true; collapsed.coll = true}}>{twoWayBindChild.data.length === 0 ? "Skip" : "Done"}</button>
  {:else}
    <h3>
      <button class="--unstyled-btn"
        on:click={() => collapsed.coll = !collapsed.coll}
      >Prepare Questions to Ask <span>{ collapsed.coll ? "+" : "-" }</span></button>
    </h3>
    <div class={`${ !!collapsed.coll ? "--collapsed-element" : ""}`}>


      {#each twoWayBindChild.data as sQuestion (sQuestion)}
        <p style="color: rgb(95, 94, 94);">{sQuestion}</p>
      {/each}

      <button on:click={() => twoWayBindChild.done = false}>edit</button>
    </div>
  {/if}


</section>

<style>
  .prepare-questions-section{
    margin-top: 2rem;
  }
</style>
