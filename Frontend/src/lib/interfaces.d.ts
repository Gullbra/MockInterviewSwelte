export interface IDataQuestionObj {
  question: string,
  suggestedAnswers: string[]
}
export interface IDataQuestionTypes {
  technical: IDataModelQuestion[],
  behavioural: IDataModelQuestion[],
  personal: IDataModelQuestion[],
  uncategorized?: IDataModelQuestion[]
}
