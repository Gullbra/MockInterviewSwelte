import uvicorn
import json
import os

from ariadne.asgi import GraphQL
from ariadne import gql, QueryType, make_executable_schema

# Define type definitions (schema) using SDL
type_defs = gql(
    """
   type Query {
       places: [Place]
       getData: TAllData
   }


   type Place {
       name: String!
       description: String!
       country: String!
   }
       
   type TPitfall {
        pitfall: String
        handling: [String]
   }
    
   type TPrepAndResearch{
        Appearance: [String]
        onlineInterview: [String]
        research: [String]
   }
    
   type TQObject {
        question: String
        suggestedAnswers: [String]
   }
   type TQtoAnswer {
        technical: [TQObject]
        behavioural: [TQObject]
        personal: [TQObject]
        uncategorized: [TQObject]
   }
    
   type TAllData {
        commonPitfalls: [TPitfall],
        generalThoughtsAndTips: [String],
        prepAndResearch: TPrepAndResearch,
        questionsToAnswer: TQtoAnswer,
        questionsToAsk: [String],
        someLinks: [String],
   }
    
   """
)

# Initialize query

query = QueryType()


# Define resolvers
@query.field("places")
def places(*_):
    return [
        {"name": "Paris", "description": "The city of lights", "country": "France"},
        {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
        {
            "name": "London",
            "description": "The city of big buildings",
            "country": "United Kingdom",
        },
    ]


@query.field("getData")
def get_data(*_):
    def get_path_to_json(cwd: str):
        return "MockInterviewSwelte".join(
            (cwd.split("MockInterviewSwelte")[:-1] + ["/Backend/data/json/data.combinedData.json"]))

    try:
        with open(get_path_to_json(os.getcwd())) as all_data_file:
            all_data_dict = json.loads(all_data_file.read())
        return all_data_dict
    except Exception as error:
        print("error!{}".format(str(error)))
        return {}


# Create executable schema
schema = make_executable_schema(type_defs, query)

# Create ASGI application
app = GraphQL(schema)

if __name__ == "__main__":
    uvicorn.run(app)
#     uvicorn.run("main:app", port=5000
#                 # , log_level="info"
#                 )
