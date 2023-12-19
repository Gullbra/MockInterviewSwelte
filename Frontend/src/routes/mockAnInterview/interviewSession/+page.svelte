<script lang="ts">
  import WebCamComponent from '../../components/WebCamComponent.svelte';
  import { randomizeArrayElement, randomizeArrayIndex } from '$lib/personalLib/pseudoRandomizing';

  interface IQuestionObj {
    question: string,
    suggestedAnswers: string[]
  }
  export let data: {
    technical: IQuestionObj[]
    behavioural: IQuestionObj[]
    personal: IQuestionObj[]
    uncategorized: IQuestionObj[]
  }

  let mode: undefined | string;

  let unaskedQuestions = {
    technical: data.technical.slice(),
    behavioural: data.behavioural.slice(),
    personal: data.personal.slice(),
    uncategorized: data.uncategorized.slice(),
  }
  const nonEmptyQArr = ["technical", "behavioural", "personal", "uncategorized"]

  let workingQuestion: IQuestionObj & { index: number, type: string }


  const answerQuestion = () => {
    switch (workingQuestion.type) {
      case "technical": 
        unaskedQuestions.technical.splice(workingQuestion.index, 1)
        if (!unaskedQuestions.technical.length) {
          nonEmptyQArr.splice(nonEmptyQArr.findIndex(el => el === "technical"), 1)
        }
        break;
      case "behavioural": 
        unaskedQuestions.behavioural.splice(workingQuestion.index, 1)
        if (!unaskedQuestions.behavioural.length) {
          nonEmptyQArr.splice(nonEmptyQArr.findIndex(el => el === "behavioural"), 1)
        }
        break;
      case "personal": 
        unaskedQuestions.personal.splice(workingQuestion.index, 1)
        if (!unaskedQuestions.personal.length) {
          nonEmptyQArr.splice(nonEmptyQArr.findIndex(el => el === "personal"), 1)
        }
        break;
      case "uncategorized": 
        unaskedQuestions.uncategorized.splice(workingQuestion.index, 1)
        if (!unaskedQuestions.uncategorized.length) {
          nonEmptyQArr.splice(nonEmptyQArr.findIndex(el => el === "uncategorized"), 1)
        }
        break;

      default: throw new Error("could not determine mode in answerQuestion()")
    }

    !nonEmptyQArr.includes(mode as string)
      ? mode = undefined
      : getQuestion()
  }


  const getQuestion = () => {
    const type = mode === undefined
      ? randomizeArrayElement(nonEmptyQArr)
      : mode

    const questionArrReference = (() => {
      switch (type) {
        case "technical": return unaskedQuestions.technical
        case "behavioural": return unaskedQuestions.behavioural
        case "personal": return unaskedQuestions.personal
        case "uncategorized": return unaskedQuestions.uncategorized

        default: throw new Error("could not determine mode in getQuestion()")
      }
    })()

    const index = randomizeArrayIndex(questionArrReference)

    workingQuestion = {
      index,
      type,
      ...questionArrReference[index]
    }
  }

</script>


<div class="about-page">
  <h2 class="about-page__header">test: interview session</h2>
  {#if mode === undefined}
    <p>What type of interview?</p>
    <div>
      {#each nonEmptyQArr as qType (qType)}
        <button on:click|preventDefault={() => {mode = qType; getQuestion()}}>{`${qType}`}</button>
      {/each}
      <button on:click|preventDefault={() => {mode = "mix"; getQuestion()}}>mix</button>
    </div>
  {:else}
    <p>{`mode: ${mode}`}</p>
    <p>{workingQuestion.question}</p>
    <button on:click={() => getQuestion()}>new Q</button>
    <button on:click={() => answerQuestion()}>answer Q</button>
  {/if}
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
