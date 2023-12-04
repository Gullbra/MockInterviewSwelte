<script lang="ts">
  const options = [
    {
      desc: "Start a prep session",
      route: "/mockAnInterview/prepSession"
    },
    {
      desc: "Go direct to a full interview session",
      route: "/mockAnInterview/interviewSession"
    },
  ]
</script>

<div class="mockAnInterview-container">
  <h2>
    Here will a mockinterview session be
  </h2>

  {#each options as option (option.desc + option.route)}
    <h3 class="session-option">
      <a href={option.route}><i>{option.desc}</i><span class="right-arrow">{"->"}</span></a>
    </h3>
  {/each}
</div>

<style>
  .mockAnInterview-container {
    margin-top: 3rem;
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .session-option {
    margin-top: 2rem;
    --left-padding-hover: 0rem;
    --text-shadow-hover: ;
    padding-left: var(--left-padding-hover);
  }
  .right-arrow {
    padding-left: calc(1rem + var(--left-padding-hover));
  }

  .session-option, .right-arrow {
    text-shadow: var(--text-shadow-hover);
    transition: 
      padding ease-in-out 0.5s, 
      color ease-in-out 0.2s, 
      text-shadow ease-in-out 0.5s;
  }
  .session-option:hover, .right-arrow:hover {
    --left-padding-hover: 1rem;
    --text-shadow-hover: 0 4px 3px rgb(177, 175, 175);
  }

</style>
