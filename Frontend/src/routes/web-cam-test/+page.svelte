<script lang="ts">
  import type { IDataQuestionTypes } from '../../lib/interfaces'
  import WebCamComponent from '../components/WebCamComponent.svelte';

  /*

  "graphql": "^15.4.0"
  "graphql-request": "^3.3.0"
  */
  
  // export let data

  // const questions: IDataQuestionTypes = { 
  //   technical: [],
  //   behavioural: [],
  //   personal: [],
  //   uncategorized: [],
  //   ...data.resp
  // }


  $: showSuggestedAnswer = false
  $: showAddAnswerForm = false
  $: newAnswer = ""
</script>


<div class="about-page">
  <h2 class="about-page__header">Webcam Test!</h2>

  <WebCamComponent/>

  <section style="margin-top: 4rem; display: flex; flex-direction: column; align-items:center;">
    <h3>This is the the QnA section</h3>

    <p style="margin-top: 2rem;"><i>"Here will the question be, can you imagine it?"</i></p>

    {#if showSuggestedAnswer}
      <p style="margin-top: 2rem;">- "Yes I can!"</p>
    {/if}
    <button class="start-stop-btn" style="margin-top: 1rem;" on:click={() => showSuggestedAnswer = !showSuggestedAnswer}>
      {showSuggestedAnswer ? "close answer": "show a suggested answer"}
    </button>

    {#if showAddAnswerForm}
      <textarea placeholder="...write answer here" class="text-area-input" bind:value={newAnswer}/>
    {/if}
    <button class="start-stop-btn" style="margin-top: 1rem;" on:click={() => showAddAnswerForm = !showAddAnswerForm}>
      {showAddAnswerForm ? "close answer form": "add an answer"}
    </button>

    <button class="rounded-sm start-stop-btn" disabled style="margin-top: 4rem;">Next quetion</button>
  </section>
</div>


<style>
  .about-page {
    padding-top: 3rem;
    display: flex; flex-direction: column; align-items: center;
  }
  .about-page__header {
    margin-bottom: 2rem;
  }


  .start-stop-btn {
    margin-top: 2rem;
    padding: 0.2rem 0.5rem;
    display: block;
    cursor: pointer;
  }


  .text-area-input {
    border-radius: 0.3rem;
    padding: 0.5rem;
    margin-top: 3rem;
    text-wrap: wrap;
    width: 100%; height: 3rem;
    resize: vertical;
  }
</style>