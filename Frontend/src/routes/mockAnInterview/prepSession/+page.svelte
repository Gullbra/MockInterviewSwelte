<script lang="ts">
  import ResearchSection from './components/ResearchSection.svelte'
  import PrepareQuestionsSection from './components/PrepareQuestionsSection.svelte';
  export let data

  interface IFetchedData {
    research: {
      Appearence: string[],
      onlineInterview: string[],
      research: string[]
    },
    generalTips: string[]
  }
  const fetchedData = data as IFetchedData

  let progress = {
    research: {
      done: false,
      data: Array.from({length: fetchedData.research.research.length}, () => "")
    },
    preparedQuestions: {
      done: false,
      data: [] as string[]
    }
  }
</script>


<div class="prep-session-container">
  <h2>test: prep session</h2>

  <ResearchSection bind:twoWayBindParent={progress.research} twoWayBindChild={{...progress.research}} fetchedData={fetchedData}/>
  <PrepareQuestionsSection bind:twoWayBindParent={progress.preparedQuestions} twoWayBindChild={{...progress.preparedQuestions}}/>

</div>


<style>
  .prep-session-container {
    padding-top: 3rem;

    display: flex; 
    flex-direction: column; align-items: center;
  }
</style>
