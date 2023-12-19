export const load = async ({ fetch }) => {
  return {
    ...await fetch('../mock/data.questionsToAnswer.json')
      .then(response => response.json())
      .then(json => json)
      .catch(err => {error: err}),
    // generalTips: await fetch("../mock/data.generalThoughtsAndTips.json")
    //   .then(response => response.json())
    //   .then(json => json)
    //   .catch(err => {error: err}),
  }
}
