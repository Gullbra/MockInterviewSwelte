export const load = async ({ fetch }) => {
  return {
    research: await fetch('../mock/data.prepAndResearch.json')
      .then(response => response.json())
      .then(json => json)
      .catch(err => {error: err}),
    generalTips: await fetch("../mock/data.generalThoughtsAndTips.json")
      .then(response => response.json())
      .then(json => json)
      .catch(err => {error: err}),
  }
}