from typing import TypedDict


class TypeQObject(TypedDict):
    question: str
    suggestedAnswers: list[str]


class TypeQtoAnswer(TypedDict):
    technical: list[TypeQObject]
    behavioural: list[TypeQObject]
    personal: list[TypeQObject]
    uncategorized: list[TypeQObject]


questionsToAnswer: TypeQtoAnswer = {
    "technical": [
        {
            "question": "Tell me about a project you're extra proud of.",
            "suggestedAnswers": [
                "Construct narrative about DeutschLernen. Narrative about regexp tester."
            ]
        },
        {
            "question": "Where do you find inspiration and stay up to day within software development? "
                        "(Articles, podcasts, people you follow on social media, books etc.)",
            "suggestedAnswers": ["Right now, just by googling. I should think about this one."]
        },
        {
            "question": "What is it about coding that makes you tick?",
            "suggestedAnswers": [
                "Stimmulans. Finn liknelser för att göra det intressant."
            ]
        },
        {
            "question": "What is a flaw (design, code, security or otherwise) that you decided to leave in an app? "
                        "Why did you make that decision?",
            "suggestedAnswers": [
                "This one I could do quickly after some thinking - I could find examples in NodeModuleRemover"
            ]
        },
        {
            "question": "JS vs TS; pro:s and cons?",
            "suggestedAnswers": [
                "Pro: transpiler and bundling (efficient output). typechecks.",
                "con: Learning curve, ts-config. Etc.",
                "Compatibility. Synthetic imports exist, but there there a lot of packages that are developed with"
                + " either just JS or TS only. Svelte => JS only."
            ]
        },
        {
            "question": "What is the difference between object-oriented and functional programming?",
            "suggestedAnswers": [
                "Objects, access levels. A lot to say but boring - have to write it out. AI gen?"
            ]
        }
    ],

    "behavioural": [
        {
            "question": "What is a good boss?",
            "suggestedAnswers": [
                "Have to think about this one"
            ]
        },
        {
            "question": "How would somebody close to you describe you?",
            "suggestedAnswers": [
                "Fuck. This is a hard one."
            ]
        },
        {
            "question": "What makes you get up out of bed in the morning?",
            "suggestedAnswers": [
                "Coffee (maybe a chuckle -  talk about good coffee)",
                "Some solution I'm dying to try.",
                "A problem I'm working on."
            ]
        },
        {
            "question": "Give me an example of a difficult problem you solved. How did you solve this problem?",
            "suggestedAnswers": [
                "Hm..."
            ]
        },
        {
            "question": "Tell me about a mistake that you've made. How did you handle it?",
            "suggestedAnswers": [
                "Hm..."
            ]
        },
        {
            "question": "Tell me about a time you learned a new skill. "
                        "How did you approach it and how did you apply your new learnings?",
            "suggestedAnswers": [
                "Talk about levels. Youtube tutorials, stack overflow, AI, always testing and playing with new tech."
            ]
        },
        {
            "question": "Has there been a time when you had to pitch an idea to a manager or senior leader? "
                        "What was the outcome?",
            "suggestedAnswers": [
                "no. Can't se this one coming up - but I'd look it over later."
            ]
        },
        {
            "question": "Tell me about a time when you overcame a conflict at work",
            "suggestedAnswers": ["Talk about salt. Practice answering so I describe it well."]
        },
        {
            "question": "Explain a situation in which you would have handled things differently.",
            "suggestedAnswers": [
                "Hm..."
            ]
        },
        {
            "question": "Tell me about a time you handled a stressful situation when you were under a lot of pressure.",
            "suggestedAnswers": ["Maybe something from AG?"]
        },
        {
            "question": "Can you tell me about a time you set and achieved a certain goal?",
            "suggestedAnswers": [
                "Hm..."
            ]
        },
        {
            "question": "What is your proudest professional accomplishment and why?",
            "suggestedAnswers": [
                "Hm..."
            ]
        }
    ],

    "personal": [
        {
            "question": 'Tell me about yourself and your coding journey. Who are you and why are you here today?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What did you learn at </salt> (what was fun, easy, difficult?)',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Why do you think you were one of all those thousands of applicant that got in to </salt>?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Tell me about a project (within coding) that you have worked on from start to finish.',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What role do you strive to take in a team?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'How do you handle failure and setbacks?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'How do you respond to criticism?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Can you define success in the context of web development?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Give an example of when you delivered beyond the expectations?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Where  would you like to see yourself in three years from now?',
            "suggestedAnswers": [""]
        },
        {
            "question": "What's your preferred way of working on a group pr…or the entire "
                        "team meets and works together? Why?",
            "suggestedAnswers": [""]
        },
        {
            "question": "Tell me about a time you had to work with a colleague/teammate that you didn't get along with",
            "suggestedAnswers": [""]
        },
        {
            "question": "Tell me about a time when a collaboration "
                        "didn't w… a team you worked with. How did you sort it out?",
            "suggestedAnswers": [""]
        },
        {
            "question": 'Define how a good team looks like',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What motivates you?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'How are you as a person?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What kind of situations make you upset or annoyed?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What positive qualities do you have?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What negative qualities do you have?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Give an example of an occupation in your career when you delivered beyond the expectation?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Tell me about three of your strengths?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Tell me about one of your weaknesses? What do you do to improve in that area?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Tell me about some feedback you have received, how have you worked on that?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'What role do you usually take in a team?',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Why should we hire you? (Tydligt och sjalvsakert -> knyt an till bolaget!)',
            "suggestedAnswers": [""]
        },
        {
            "question": 'Feedback',
            "suggestedAnswers": [""]
        }
    ],

    "uncategorized": [
        {
            "question": "Your personal story. What made you switch careers and apply to SALT?",
            "suggestedAnswers": ["Hm..."],
        },
        {
            "question": "Your personal story. What made you switch careers and apply to SALT?",
            "suggestedAnswers": ["write it out."]
        },
        {
            "question": "your dev-profile. What are your strengths as a developer today? Where is there room for "
                        "improvement? What do you enjoy doing as a developer? What do you strive for in your work?",
            "suggestedAnswers": ["I REALLY have to work on this one."]
        },
        {
            "question": "your three key take-away's from your time at SALT. E.g. learning through mob-programming.",
            "suggestedAnswers": ["Important"]
        },
        {
            "question": "your personal pitch. Why should xxx hire you? What will you bring to the team?",
            "suggestedAnswers": ["Even more important"]
        }
    ]
}
