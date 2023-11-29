import json

from flask import Flask, jsonify, request
from ariadne.explorer.playground import PLAYGROUND_HTML
from ariadne import load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers, graphql_sync, ObjectType
from flask_cors import CORS
from data.graphQl.resolvers import get_data_resolver

query = ObjectType("Query")
query.set_field("getData", get_data_resolver)

app = Flask(__name__)
CORS(app)

schema_from_file = load_schema_from_path("../data/graphQl/schema.graphql")
refined_schema = make_executable_schema(
    schema_from_file,
    query,
    snake_case_fallback_resolvers
)


@app.route('/')
def hello():
    return "Hey"


# https://www.apollographql.com/blog/graphql/python/complete-api-guide/
# https://studio.apollographql.com/sandbox/explorer
@app.get('/api/graphql/v1/')
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.post('/api/graphql/v1/')
def graphql_server():
    data = request.get_json()
    print("get_json_data:", data)
    success, result = graphql_sync(
        refined_schema,
        data,
        context_value=request,
        debug=app.debug
    )
    print("after gql_sync", result)
    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.get('/api/data/<file_name>')
def get_api_data(file_name):
    try:
        json_file = open('../data/json/data.{}.json'.format(file_name))
        json_data = json.load(json_file)
        json_file.close()
        return jsonify(json_data)
    except OSError:
        return 'No data found'


if __name__ == '__main__':
    app.run()
