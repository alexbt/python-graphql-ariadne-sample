import os

from ariadne import make_executable_schema, gql, load_schema_from_path, graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from flask import Response
from flask_cors import CORS

from model import query, mutation

type_defs = gql(load_schema_from_path("../graphql/schema.graphql"))
schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__, root_path=os.path.abspath(".."))
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})


@app.route('/')
def index() -> str:
    return app.send_static_file('index.html')


@app.route("/graphql", methods=["GET"])
def graphql_playgroud() -> (str, int):
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server() -> (Response, int):
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code


app.run(debug=True)
