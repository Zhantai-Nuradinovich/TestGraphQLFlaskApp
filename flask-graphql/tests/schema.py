from graphql.type.definition import (GraphQLArgument, GraphQLField,
                                     GraphQLNonNull, GraphQLObjectType,
                                     GraphQLList)
from graphql.type.scalars import GraphQLString, GraphQLBoolean, GraphQLInt
from graphql.type.schema import GraphQLSchema


def resolve_raises(*_):
    raise Exception("Throws!")


movies = [{"id": 1, "title": "Hello", "director": "me", "composer": "com", "release_date": "2020"},
          {"id": 2, "title": "Hell", "director": "m52e", "composer": "cm", "release_date": "202"},
          {"id": 3, "title": "Hel", "director": "e", "composer": "co", "release_date": "220"},
          {"id": 4, "title": "He", "director": "m", "composer": "om", "release_date": "2"}]

MovieType = GraphQLObjectType(
    name="movies",
    description="this represents a movie",
    fields={
        "id": GraphQLInt,
        "title": GraphQLString,
        "director": GraphQLString,
        "composer": GraphQLString,
        "release_date": GraphQLString
    }
)

QueryRootType = GraphQLObjectType(
    name="QueryRoot",
    fields={
        "thrower": GraphQLField(GraphQLNonNull(GraphQLString), resolve=resolve_raises),
        "request": GraphQLField(
            GraphQLNonNull(GraphQLString),
            resolve=lambda obj, info: info.context["request"].args.get("q"),
        ),
        "movies": GraphQLField(
            description="This is a list of books",
            type_=GraphQLList(MovieType),
            resolve=lambda x, y: movies
        ),
        "context": GraphQLField(
            GraphQLObjectType(
                name="context",
                fields={
                    "session": GraphQLField(GraphQLString),
                    "request": GraphQLField(
                        GraphQLNonNull(GraphQLString),
                        resolve=lambda obj, info: info.context["request"],
                    ),
                },
            ),
            resolve=lambda obj, info: info.context,
        ),
        "test": GraphQLField(
            type_=GraphQLString,
            args={"who": GraphQLArgument(GraphQLString)},
            resolve=lambda obj, info, who="World": "Hello %s" % who,
        ),
        "characters": GraphQLField(
            type_=GraphQLString,
            args={"who": GraphQLArgument(GraphQLString)},
            resolve=lambda obj, info, who="World": "Hello %s" % who,
        ),
    },
)

MutationRootType = GraphQLObjectType(
    name="MutationRoot",
    description="Root mutations",
    fields={
        "writeTest": GraphQLField(type_=QueryRootType, resolve=lambda *_: QueryRootType),
        "addMovie": GraphQLField(
            type_=MovieType,
            description="Add a movie",
            args={
                "id": GraphQLArgument(GraphQLInt),
                "title": GraphQLArgument(GraphQLString),
                "director": GraphQLArgument(GraphQLString),
                "composer": GraphQLArgument(GraphQLString),
                "release_date": GraphQLArgument(GraphQLString)
            },
            resolve=lambda obj, info, id, title, director, composer, release_date: newMovie(id, title, director, composer, release_date)
        )
    },
)


def newMovie(id, title, director, composer, release_date):
    movie = {"id": id, "title": title, "director": director, "composer": composer, "release_date": release_date}
    movies.append(movie)
    return movie


Schema = GraphQLSchema(QueryRootType, MutationRootType)
