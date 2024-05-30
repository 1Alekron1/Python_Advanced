from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book, update_book_by_id, get_book_by_id, delete_book_by_id, add_author, get_author_by_id,
    get_books_by_author, delete_author_by_id,
)
from blueprints import BookSchema, AuthorSchema

app = Flask(__name__)
api = Api(app)


class BookListResource(Resource):
    def get(self) -> tuple[list[dict], int]:
        schema = BookSchema()
        books = get_all_books()
        return schema.dump(books, many=True), 200

    def post(self) -> tuple[dict, int]:
        schema = BookSchema()
        data = request.json
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class BookResource(Resource):
    def get(self, book_id: int) -> tuple[dict, int]:
        book = get_book_by_id(book_id)
        if book is None:
            return {"message": "Book not found"}, 404

        schema = BookSchema()
        return schema.dump(book), 200

    def put(self, book_id: int) -> tuple[dict, int]:
        schema = BookSchema()
        data = request.json
        try:
            book = schema.load(data)
            book.id = book_id
        except ValidationError as exc:
            return exc.messages, 400

        if get_book_by_id(book_id) is None:
            return {"message": "Book not found"}, 404

        update_book_by_id(book)
        return schema.dump(book), 200

    def delete(self, book_id: int) -> tuple[dict, int]:
        if get_book_by_id(book_id) is None:
            return {"message": "Book not found"}, 404

        delete_book_by_id(book_id)
        return {"message": "Book deleted"}, 200


class AuthorListResource(Resource):
    def post(self) -> tuple[dict, int]:
        schema = AuthorSchema()
        data = request.json
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        author = add_author(author)
        return schema.dump(author), 201


class AuthorResource(Resource):
    def get(self, author_id: int) -> tuple[dict, int]:
        author = get_author_by_id(author_id)
        if author is None:
            return {"message": "Author not found"}, 404

        books = get_books_by_author(author_id)
        schema = BookSchema()
        return schema.dump(books, many=True), 200

    def delete(self, author_id: int) -> tuple[dict, int]:
        if get_author_by_id(author_id) is None:
            return {"message": "Author not found"}, 404

        delete_author_by_id(author_id)
        return {"message": "Author deleted"}, 200


api.add_resource(BookListResource, '/api/books')
api.add_resource(BookResource, '/api/book/<int:book_id>')
api.add_resource(AuthorListResource, "/api/authors")
api.add_resource(AuthorResource, '/api/authors/<int:author_id>')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
