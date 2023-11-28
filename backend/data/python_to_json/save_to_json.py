from python_data_files.common_pitfalls import commonPitfalls
from python_data_files.general_thoughts_and_tips import generalThoughtsAndTips
from python_data_files.non_verbal_during_interview import duringInterview
from python_data_files.prep_and_research import prepAndResearch
from python_data_files.questions_to_answer import questionsToAnswer
from python_data_files.questions_to_ask import questionsToAsk
from python_data_files.some_links import someLinks


def save_partial_data_to_json(save_to_name: str, data: dict | list):
    import json

    try:
        # with open('../json/data.{}.json'.format(file_name)) as existing_file:
        with open('../json/data.{}.json'.format(save_to_name), 'w') as save_file:
            # json.dump(json.loads(existing_file.read()), new_file)
            json.dump(data, save_file)

    except OSError:
        return 'No data found'


def save_all_data_to_different_files():
    save_partial_data_to_json("commonPitfalls", commonPitfalls)
    save_partial_data_to_json("generalThoughtsAndTips", generalThoughtsAndTips)
    save_partial_data_to_json("duringInterview", duringInterview)
    save_partial_data_to_json("prepAndResearch", prepAndResearch)
    save_partial_data_to_json("questionsToAnswer", questionsToAnswer)
    save_partial_data_to_json("questionsToAsk", questionsToAsk)
    save_partial_data_to_json("someLinks", someLinks)


def save_all_data_to_one_file():
    save_partial_data_to_json(
        "combinedData",
        {
            "commonPitfalls": commonPitfalls,
            "generalThoughtsAndTips": generalThoughtsAndTips,
            "duringInterview": duringInterview,
            "prepAndResearch": prepAndResearch,
            "questionsToAnswer": questionsToAnswer,
            "questionsToAsk": questionsToAsk,
            "someLinks": someLinks,
        }
    )


if __name__ == '__main__':
    save_all_data_to_one_file()
