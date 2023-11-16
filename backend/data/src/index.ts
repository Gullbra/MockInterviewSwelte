import fs from 'fs'
import path from 'path'
import { generalThoughts, commonPitfalls, prepAndResearch, duringInterview, questionsToAnswer, questionsToAsk, someLinks } from './dataInTS.ts'

const jsonWriter = async (fileName: string, data: unknown): Promise<void> => fs
  .promises
  .writeFile(path.join('json', `data.${fileName}.json`), JSON.stringify(data, null, 2))

await Promise.all([
  jsonWriter("generalThoughts", generalThoughts),
  jsonWriter("commonPitfalls", commonPitfalls),
  jsonWriter("prepAndResearch", prepAndResearch),
  jsonWriter("duringInterview", duringInterview),
  jsonWriter("questionsToAnswer", questionsToAnswer),
  jsonWriter("questionsToAsk", questionsToAsk),
  jsonWriter("someLinks", someLinks),
]).catch(err => console.log(err.message))
