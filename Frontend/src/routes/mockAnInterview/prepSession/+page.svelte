<script lang="ts">
  import ResearchSection from './components/ResearchSection.svelte'
  import PrepareQuestionsSection from './components/PrepareQuestionsSection.svelte';
  import OnlineInterview from './components/OnlineInterview.svelte';
  import AppearenceChecklist from './components/AppearenceChecklist.svelte';
  import GeneralTipsList from './components/GeneralTipsList.svelte';
  import ShowNotes from './components/ShowNotes.svelte';
  import './prep-session-classes.css'


  export let data: {
    research: {
      Appearance: string[],
      onlineInterview: string[],
      research: string[]
    },
    generalTips: string[],
  }


  let progress = {
    research: {
      done: false,
      data: Array.from({length: data.research.research.length}, () => "")
    },
    preparedQuestions: {
      done: false,
      data: [] as string[]
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
    fetchedData={data.research.research}/>

  <PrepareQuestionsSection 
    bind:twoWayBindParent={progress.preparedQuestions} twoWayBindChild={{...progress.preparedQuestions}}/>

  <OnlineInterview 
    bind:twoWayBindParent={progress.onlineInterview} twoWayBindChild={{...progress.onlineInterview}} 
    fetchedData={data.research.onlineInterview}/>

  <AppearenceChecklist 
    bind:twoWayBindParent={progress.appearance} twoWayBindChild={{...progress.appearance}} 
    fetchedData={data.research.Appearance}/> 

  <GeneralTipsList 
    fetchedData={data.generalTips}/>

  <ShowNotes
    progress={progress}
    fetchedData={{ 
      research: data.research.research, 
      onlineInterview: data.research.onlineInterview,
      appearance: data.research.Appearance,
      generalTips: data.generalTips
    }} />
</div>


<style>
  .prep-session-container {
    padding-top: 3rem;
    margin-left: 2rem; margin-right: 2rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
