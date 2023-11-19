interface IDataModelQuestion {
  question: string,
  suggestedAnswers: string[]
}
interface IDataContainerQuestions {
  technical: IDataModelQuestion[],
  behavioural: IDataModelQuestion[],
  personal: IDataModelQuestion[],
  uncategorized?: IDataModelQuestion[]
}


export const generalThoughts = [
  "The underlining message should always be \"I'm the one you're looking for/You should hire me\".",
  "0 correlation between level of technical skills and who gets hired. Technical skills are just a checkbox.",
  "Companies are looking for a candidate who can do the job well(tech skills) and fit in(Personality type, culture, team player) with the company/team, preferably for the long run(Indicates that he/she isn't gonna change work after 6 months).",
  "Offered coffee? Accept the invitation :)"
]

export const commonPitfalls = {
  "unclear story": [
    "STAR: Situation, Task, Action, Result",
    "https://www.youtube.com/watch?v=2EbgsRHLF9Y",
    "https://www.indeed.com/career-advice/interviewing/how-to-use-the-star-interview-response-technique"
  ],
  "Excusing, undermining oneself": {
    "I don't know. I haven't worked with that before.": "Mention what you have done before: \"I'm not sure, but I have worked with this similar thing and...\"",
    "Talking about developing": "Speak as a developer",
    "\"This is just a small project I did for fun on my spare time, it's not finished\"": "\"This is what I managed to do in this this amount of time. If I get the chance I'd like to improve <...>...\"",
    "Excuse your previous choice of career.": " Be proud of what you've done before and use it to your advantage.",
    "Since I didn't have any experience before </salt>...": "Everyone we hire has some experience to build from.",
    "How long does it take to become a productive developer at your company?": "\"How do people collaborate within the team?\", \"How does a day/week as a developer at your company look like?\" or \" Do you have any social activities?\""
  },
  "people hire people - not technical skills": [
    "Come prepare and read up on the company, role/job description, people you will be meeting with",
    "Find a common ground, talk about the values, experiences and interests that you share.",
    "The interview should be a pleasant dialogue and not a one way conversation of questions and answers. Develop your replies and ask questions back! Be relaxed and genuinely curious!",
    "Everyone want to feel valued and appreciated. Why not compliment on the company, their ways of working or tech stack, how they've built their products and services. Remember to be professional and sincere."
  ]
}


export const prepAndResearch = {
  "Appearence": [
    "Dress for success, business casual. It doesn't hurt to take a shower, shave/get a haircut, wear a clean shirt and generally looking polished for the interview."
  ],
  "onlineinterview":  [
    "Light on your face, not from behind",
    "Check that your audio works",
    "Screen share settings (give Chrome approval)"
  ],
  "research": [
    "What do they do?",
    "What are their values?",
    "What could I offer them?",
    "What could they offer me?",
    "What questions do I have for them? (What do I want to know)",
    "What questions will they likely want to ask me? (What do they want to know about me)",
    "Anticipate relevant follow up questions, and bring them up yourself when applicable(in case the interviewer \"misses the mark\")",
    "Write notes - find star model stories to relevant topics/questions"
  ]
}


export const duringInterview = {
  "Demenure": [
    "keep eye contact.",
    "Sit still. Posture - straight, relaxed. No crossed legs or arms.",
    "talk slowly and articulate. Don't rush it and don't mumble, basically",
    "smiling never hurts to bring more energy, seem more engaging and positive",
    "Thank everyone involved for taking the time to meet/talk"
  ],

  "template phrases": [
    "that is a very good question, let me think about that one for a moment.",
    "I haven't thought about that before, but if I were to give you an answer here and now...",
    "As I understand your question, I ...",
    "Something I learned about myself during my time at SALT is ...",
    "The reason \"X\" is important to me is because of \"Y\" and \"Z\"",
    "If you would ask me what I believe to be the top three skills as a web developer I would say ...",
    "I have found that I thrive in a work environment where ...",
    "I would like to tie in to what you said before about X, this resonates with my values/experience ..."
  ],

  "introducing yourself": { 
    "goals with introduction": [
      "get personal and establish some connection, rapport",
      "comunicate your journey, and where you are professionaly",
      "comunicate interests and who you are as a person"
    ],
    "keypoints" : {
      "Starting point: When was your initial contact with coding/technology?": [
        "what sparked your interest for coding and how did it manifest itself?"
      ],
      "Key events/turning points in your life that pushed you in this direction" : [
        "Everything relating to technology counts: hobbies when you were younger, dabbling with code,, online bootcamps, internships, interrupted studies, working in a technical environment etc.",
        "Mention what code languages and tools you've touched upon before.",
        "Add notes about how one thing led to another." 
      ],
      "wrap up": [
        "Why did you decide to apply to SALT?",
        "Share some reflections about your experience SALT.",
        "What are your thoughts for the future?"
      ]
    }
  }
}


export const questionsToAnswer: IDataContainerQuestions = {
  "technical": [
    {
      question: "Tell me about a project you're extra proud of.",
      suggestedAnswers: [
        "Construct narrativ about DeutschLernen. Narrative about regexp tester."
      ]
    },
    {
      question: "Where do you find inspiration and stay up to day within software development? (Articles, podcasts, people you follow on social media, books etc.)",
      suggestedAnswers: ["Right now, just by googling. I should think about this one."]
    },
    {
      question: "What is it about coding that makes you tick?",
      suggestedAnswers: [
        "Stimulans. Finn liknelser för att göra det intressant."
      ]
    },
    {
      question: "What is a flaw (design, code, security or otherwise) that you decided to leave in an app? Why did you make that decision?",
      suggestedAnswers: [
        "This one I could do quickly after some thinking - I could find examples in NodeModuleRemover"
      ]
    },
    {
      question: "JS vs TS; pro:s and cons?",
      suggestedAnswers: [
        "Pro: transpiler and bundeling (efficient output). typechecks.",
        "con: Lerning curve, tsconfig. Etc.",
        "Compatibility. Synthetic imorts exist, but there there a lot of packages that are developed with either just JS or TS only. Swelte => JS only."
      ]
    },
    {
      question: "What is the difference between object-oriented and functional programming?",
      suggestedAnswers: [
        "Objects, acces levels. A lot to say but boring - have to write it out. AI gen?"
      ]
    }
  ],
  
  "behavioural": [
    {
      question: "What is a good boss?",
      suggestedAnswers: [
        "Have to think about this one"
      ]
    },
    {
      question: "How would somebody close to you describe you?",
      suggestedAnswers: [
        "Fuck. This is a hard one."
      ]
    },
    {
      question: "What makes you get up out of bed in the morning?",
      suggestedAnswers: [
        "Coffee (maybe a chuckle -  talk about good coffee)",
        "Some solution I'm dying to try.",
        "A problem I'm working on."
      ]
    },
    {
      question: "Give me an example of a difficult problem you solved. How did you solve this problem?",
      suggestedAnswers: [
        "Hm..."
      ]
    },
    {
      question: "Tell me about a mistake that you've made. How did you handle it?",
      suggestedAnswers: [
        "Hm..."
      ]
    },
    {
      question: "Tell me about a time you learned a new skill. How did you approach it and how did you apply your new learnings?",
      suggestedAnswers: [
        "Talk about levels. Youtube tutorials, stack overflow, AI, always testing and playing with new tech."
      ]
    },
    {
      question: "Has there been a time when you had to pitch an idea to a manager or senior leader? What was the outcome?",
      suggestedAnswers: [
        "no. Can't se this one comming up - but I'd look it over later."
      ]
    },
    {
      question: "Tell me about a time when you overcame a conflict at work",
      suggestedAnswers: ["Talk about salt. Practice answering so I descibe it well."]
    },
    {
      question: "Explain a situation in which you would have handled things differently.",
      suggestedAnswers: [
        "Hm..."
      ]
    },
    {
      question: "Tell me about a time you handled a stressful situation when you were under a lot of pressure.",
      suggestedAnswers: ["Maybe something from AG?"]
    },
    {
      question: "Can you tell me about a time you set and achieved a certain goal?",
      suggestedAnswers: [
        "Hm..."
      ]
    },
    {
      question: "What is your proudest professional accomplishment and why?",
      suggestedAnswers: [
        "Hm..."
      ]
    }
  ],

  "personal": [
    {
      question: 'Tell me about yourself and your coding journey. Who are you and why are you here today?',
      suggestedAnswers: [""]
    },
    {
      question: 'What did you learn at </salt> (what was fun, easy, difficult?)',
      suggestedAnswers: [""]
    },
    {
      question: 'Why do you think you were one of all those thousands of applicant that got in to </salt>?',
      suggestedAnswers: [""]
    },
    {
      question: 'Tell me about a project (within coding) that you have worked on from start to finish.',
      suggestedAnswers: [""]
    },
    {
      question: 'What role do you strive to take in a team?',
      suggestedAnswers: [""]
    },
    {
      question: 'How do you handle failure and setbacks?',
      suggestedAnswers: [""]
    },
    {
      question: 'How do you respond to criticism?',
      suggestedAnswers: [""]
    },
    {
      question: 'Can you define success in the context of web development?',
      suggestedAnswers: [""]
    },
    {
      question: 'Give an example of when you delivered beyond the expectations?',
      suggestedAnswers: [""]
    },
    {
      question: 'Where  would you like to see yourself in three years from now?',
      suggestedAnswers: [""]
    },
    {
      question: "What's your preferred way of working on a group pr…or the entire team meets and works together? Why?", 
      suggestedAnswers: [""]
    },
    {
      question: "Tell me about a time you had to work with a colleague/teammate that you didn't get along with", 
      suggestedAnswers: [""]
    },
    {
      question: "Tell me about a time when a collaboration didn't w… a team you worked with. How did you sort it out?", 
      suggestedAnswers: [""]
    },
    {
      question: 'Define how a good team looks like',
      suggestedAnswers: [""]
    },
    {
      question: 'What motivates you?',
      suggestedAnswers: [""]
    },
    {
      question: 'How are you as a person?',
      suggestedAnswers: [""]
    },
    {
      question: 'What kind of situations make you upset or annoyed?',
      suggestedAnswers: [""]
    },
    {
      question: 'What positive qualities do you have?',
      suggestedAnswers: [""]
    },
    {
      question: 'What negative qualities do you have?',
      suggestedAnswers: [""]
    },
    {
      question: 'Give an example of an occupation in your career when you delivered beyond the expectation?',
      suggestedAnswers: [""]
    },
    {
      question: 'Tell me about three of your strengths?',
      suggestedAnswers: [""]
    },
    {
      question: 'Tell me about one of your weaknesses? What do you do to improve in that area?',
      suggestedAnswers: [""]
    },
    {
      question: 'Tell me about some feedback you have received, how have you worked on that?',
      suggestedAnswers: [""]
    },
    {
      question: 'What role do you usually take in a team?',
      suggestedAnswers: [""]
    },
    {
      question: 'Why should we hire you? (Tydligt och sjalvsakert -> knyt an till bolaget!)',
      suggestedAnswers: [""]
    },
    {
      question: 'Feedback',
      suggestedAnswers: [""]
    }
  ],

  "uncategorized": [
    {
      question: "Your personal story. What made you switch careers and apply to SALT?",
      suggestedAnswers: [ "Hm..." ]
    },
    {
      question: "Your personal story. What made you switch careers and apply to SALT?",
      suggestedAnswers: [ "write it out." ]
    },
    {
      question: "your dev-profile. What are your strengths as a developer today? Where is there room for improvement? What do you enjoy doing as a developer? What do you strive for in your work?",
      suggestedAnswers: [ "I REALLY have to work on this one." ]
    },
    {
      question: "your three key take-aways from your time at SALT. E.g. learning through mob-programming.",
      suggestedAnswers: [ "Important" ]
    },
    {
      question: "your personal pitch. Why should xxx hire you? What will you bring to the team?",
      suggestedAnswers: [ "Even more important" ]
    }
  ]
}

export const questionsToAsk = [
  "I'm curious to learn more about your company. Can you tell me where you are now and where you are headed?",
  "How would you describe the way your development team work on a daily basis?",
  "You mentioned that you do X and Y. Could you tell me a bit more about that?"
]

export const someLinks = [
  "https://www.youtube.com/watch?v=2mc2B8NZhvY",
  "https://www.ted.com/talks/amy_cuddy_your_body_language_may_shape_who_you_are/comments",
  "https://www.youtube.com/watch?v=y66YKWz_sf0",
  "https://www.youtube.com/watch?v=5v-wyR5emRw",
  "https://www.youtube.com/watch?v=zZCk2z9ymmY",
  "https://www.randstad.ca/job-seeker/career-resources/resume-tips/what-do-recruiters-really-look-for-in-a-cover-letter/#:~:text=Recruiters%20want%20a%20document%20that's,organization%20uses%20to%20describe%20itself."
]
