<script lang="ts">
    import AppLayout from "./AppLayout.svelte";
    import TestView from "./views/TestView.svelte";

  // imported from main.ts
	export let name: string;
  let dataIsLoading = true
  //setTimeout(()=>dataIsLoading=true, 1000)
  
  const optionObj = { 
    headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
  }

  const data = fetch('./mock/questions.list.json', optionObj)
    .then(response => response.json())
    .then(data => {dataIsLoading = false; return data})
    .catch(err => console.log(err.message))

</script>

<AppLayout>
  {#if !dataIsLoading}
    <TestView name={name}/>
  {:else}
    <p>loading!</p>
  {/if}
</AppLayout>



