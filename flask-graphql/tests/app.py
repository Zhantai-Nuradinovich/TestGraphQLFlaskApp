from flask import Flask
from flask_cors import CORS

from flask_graphql import GraphQLView
from tests.schema import Schema


def create_app(path="/graphql", **kwargs):
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(
        path, view_func=GraphQLView.as_view("graphql", schema=Schema, **kwargs)
    )
    CORS(app)
    return app


if __name__ == "__main__":
    app = create_app(graphiql=True)
    app.run("0.0.0.0")
