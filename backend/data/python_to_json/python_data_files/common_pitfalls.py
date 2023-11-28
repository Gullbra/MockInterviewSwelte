from typing import TypedDict


class TypePitfall(TypedDict):
    pitfall: str
    handling: list[str]


commonPitfalls: list[TypePitfall] = [
    {
        "pitfall": "unclear story",
        "handling": [
            "STAR: Situation, Task, Action, Result",
            "https://www.youtube.com/watch?v=2EbgsRHLF9Y",
            "https://www.indeed.com/career-advice/interviewing/how-to-use-the-star-interview-response-technique"
        ]
    },
    {
        "pitfall": "Excusing, undermining oneself",
        "handling": [
            "I don't know. I haven't worked with that before. => "
            + "Mention what you have done before: \"I'm not sure, but I have worked with this similar thing and...\"",
            "Talking about developing => Speak as a developer",
            "\"This is just a small project I did for fun on my spare time, it's not finished\" => \"This is what I "
            + "managed to do in this this amount of time. If I get the chance I'd like to improve <...>...\"",
            "Excuse your previous choice of career. => "
            + "Be proud of what you've done before and use it to your advantage.",
            "Since I didn't have any experience before </salt>... => "
            + "Everyone we hire has some experience to build from.",
            "How long does it take to become a productive developer at your company? => \"How do people collaborate "
            + "within the team?\", \"How does a day/week as a developer at your company "
            + "look like?\" or \" Do you have any social activities?\""
        ]
    },
    {
        "pitfall": "people hire people - not technical skills",
        "handling": [
            "Come prepare and read up on the company, role/job description, people you will be meeting with",
            "Find a common ground, talk about the values, experiences and interests that you share.",
            "The interview should be a pleasant dialogue and not a one way conversation of questions and answers. "
            + "Develop your replies and ask questions back! Be relaxed and genuinely curious!",
            "Everyone want to feel valued and appreciated. Why not compliment on the company, their ways of working or "
            + "tech stack, how they've built their products and services. Remember to be professional and sincere."
        ]
    }
]
