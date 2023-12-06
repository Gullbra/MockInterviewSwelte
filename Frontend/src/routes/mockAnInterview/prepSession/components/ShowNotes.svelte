<script lang="ts">
  export let progress: {
    research: {
      data: string[]
    },
    preparedQuestions: {
      data: string[]
    },
    onlineInterview: {
      done: [boolean, boolean]
    }
  }, fetchedData: {
    research: string[],
    onlineInterview: string[],
    appearance: string[],
    generalTips: string[]
  }

  $: text = (() => {
    let textWIP = "\t\tNotes:\n\n"

    textWIP += "Research:\n"
    textWIP += progress.research.data.map((savedAnswer, index) => {
      if (savedAnswer === "") 
        return ""

      return `\tQ: ${fetchedData.research[index]}\n\t\t-  ${savedAnswer}\n`
    }).join("")

    textWIP += "\nQuestions to Ask:"
    textWIP += progress.preparedQuestions.data.map(question => {
      return `\n\t-  ${question.split('.').slice(1).join('').trim()}`
    }).join("")

    textWIP += "\n\nChecklist before Interview:"
    if (!!progress.onlineInterview.done[0]) {
      textWIP += fetchedData.onlineInterview.map(tip => `\n\t•  ${tip}`).join("") + "\n"
    }

    textWIP += fetchedData.appearance.map(tip => `\n\t•  ${tip}`).join("") + "\n"

    textWIP += "\nGeneral Tips:"
    textWIP += fetchedData.generalTips.map(tip => `\n\t•  ${tip}`).join("") + "\n"

    return textWIP
  })()
</script>


<section class="prep-session__section">
  <h3 class="prep-section__header">Auto-compiled Notes</h3>

  <div class="prep-section__inner-container--working">

    <textarea style="width: 600px; height: 400px;"
      value={text}
    />
  </div>
</section>

