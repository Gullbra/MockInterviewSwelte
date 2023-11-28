from typing import TypedDict


class TypePrepAndResearch(TypedDict):
    Appearance: list[str]
    onlineInterview: list[str]
    research: list[str]


prepAndResearch: TypePrepAndResearch = {
    "Appearance": [
        "Dress for success, business casual. It doesn't hurt to take a shower, shave/get a haircut, "
        + "wear a clean shirt and generally looking polished for the interview."
    ],
    "onlineInterview": [
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
        "Anticipate relevant follow up questions, and bring them up yourself "
        + "when applicable(in case the interviewer \"misses the mark\")",
        "Write notes - find star model stories to relevant topics/questions"
    ]
}
