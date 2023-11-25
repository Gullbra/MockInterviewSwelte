<script lang="ts">
  import type { IDataContainerQuestions } from '../../../../Backend/data/src/dataInTS'

  export let data
  const questions: IDataContainerQuestions = { 
    technical: [],
    behavioural: [],
    personal: [],
    uncategorized: [],
    ...data.resp
  }

  let stream: MediaStream, videoRef: HTMLVideoElement;

  $: showSuggestedAnswer = false
  $: showAddAnswerForm = false
  $: newAnswer = ""

  async function getStream() {
    try {
      stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false
      });
      videoRef.srcObject = stream;
    } catch (err) {
      console.error(err);
    }
  }

  async function stopStream() {
    stream.getTracks().forEach(track => track.stop());
    videoRef.srcObject = null;
  }
</script>

<div class="about-page">
  <h2 class="about-page__header">Webcam Test!</h2>

  <video class={`mt-4 rounded-sm ${videoRef?.srcObject === null ? "--stream-closed" : "--stream-open"}`} autoplay={true} bind:this={videoRef}><track kind="captions"></video>

  {#if videoRef?.srcObject === null}
    <button class="start-stop-btn rounded-sm bg-slate-600 text-white" on:click={getStream}>Start Stream</button>
  {:else}
    <button class="start-stop-btn rounded-sm bg-red-600 text-white" on:click={stopStream}>Stop Stream</button>
  {/if}

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
  .--stream-closed {
    height: 0px;
  }
  .--stream-open {
    width: 640px;
    height: 480px;
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