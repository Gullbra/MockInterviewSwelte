<script lang="ts">
  import ResearchSection from './components/ResearchSection.svelte'
  import PrepareQuestionsSection from './components/PrepareQuestionsSection.svelte';
  import OnlineInterview from './components/OnlineInterview.svelte';
  export let data

  interface IFetchedData {
    research: {
      Appearence: string[],
      onlineInterview: string[],
      research: string[]
    },
    generalTips: string[],
  }
  const fetchedData = data as IFetchedData

  let progress = {
    research: {
      done: true, //false,
      data: Array.from({length: fetchedData.research.research.length}, () => "")
    },
    preparedQuestions: {
      done: true, //false,
      data: [] as string[]
    },
    onlineInterview: {
      done: [false, false] as [boolean, boolean]
    }
  }
</script>


<div class="prep-session-container">
  <h2>test: prep session</h2>

  <ResearchSection bind:twoWayBindParent={progress.research} twoWayBindChild={{...progress.research}} fetchedData={fetchedData}/>
  <PrepareQuestionsSection bind:twoWayBindParent={progress.preparedQuestions} twoWayBindChild={{...progress.preparedQuestions}}/>
  <OnlineInterview bind:twoWayBindParent={progress.onlineInterview} twoWayBindChild={{...progress.onlineInterview}} fetchedData={fetchedData.research.onlineInterview}/>
  <!-- <AppearenceChecklist /> -->
  <!-- <GerneralTips /> -->

</div>


<style>
  .prep-session-container {
    padding-top: 3rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
