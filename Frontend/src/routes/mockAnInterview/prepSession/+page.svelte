<script lang="ts">
  import ResearchSection from './components/ResearchSection.svelte'
  import PrepareQuestionsSection from './components/PrepareQuestionsSection.svelte';
  import PrepareIntroductionSection from './components/PrepareIntroductionSection.svelte';
  import OnlineInterview from './components/OnlineInterview.svelte';
  import AppearenceChecklist from './components/AppearenceChecklist.svelte';
  import GeneralTipsList from './components/GeneralTipsList.svelte';
  import ShowNotes from './components/ShowNotes.svelte';
  import './prep-session-classes.css'


  export let data: {
    research: {
      question: string,
      desc: string
    }[],

    questionsToAsk: {
      question: string,
      desc: string,
      tips: string[]
    },

    prepareIntroduction: {
      goalsWithIntroduction: string[],
      keyPoints: {
        point: string,
        desc: string
      }[],
      examples: string[]
    },

    onlineInterview: string[],

    appearance: string[],

    generalTips: string[],
  }


  let progress = {
    research: {
      done: false,
      data: Array.from({length: data.research.length}, () => "")
    },
    preparedQuestions: {
      done: false,
      data: [] as string[]
    },
    preparedIntroduction: {
      done: false,
      data: ""
    },
    onlineInterview: {
      done: [false, false] as [boolean, boolean]
    },
    appearance: {
      done: false,
    }
  }
</script>


<div class="prep-session-container">
  <h2>Interview Prep</h2>

  <ResearchSection 
    bind:twoWayBindParent={progress.research} twoWayBindChild={{...progress.research}} 
    fetchedData={data.research} />

  <PrepareQuestionsSection 
    bind:twoWayBindParent={progress.preparedQuestions} twoWayBindChild={{...progress.preparedQuestions}} 
    fetchedData={data.questionsToAsk} />

  <PrepareIntroductionSection 
    bind:twoWayBindParent={progress.preparedIntroduction} twoWayBindChild={{...progress.preparedIntroduction}} 
    fetchedData={data.prepareIntroduction} /> 

  <!-- TODO prepareAnswers -->>

  <OnlineInterview 
    bind:twoWayBindParent={progress.onlineInterview} twoWayBindChild={{...progress.onlineInterview}} 
    fetchedData={data.onlineInterview} />

  <AppearenceChecklist 
    bind:twoWayBindParent={progress.appearance} twoWayBindChild={{...progress.appearance}} 
    fetchedData={data.appearance} /> 

  <GeneralTipsList 
    fetchedData={data.generalTips} />

  <ShowNotes
    progress={progress}
    fetchedData={data} />
</div>


<style>
  .prep-session-container {
    padding-top: 3rem;
    margin-left: 2rem; margin-right: 2rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
