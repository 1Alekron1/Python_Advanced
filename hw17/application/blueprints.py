from marshmallow import Schema, fields, validates, ValidationError, post_load
from models import get_book_by_title, Book, get_author_by_id, Author


class BaseSchema(Schema):
    """Базовая схема для общих методов валидации."""

    @staticmethod
    def validate_existence(fetch_func, identifier, error_message):
        """Метод для проверки существования записи по идентификатору."""
        if fetch_func(identifier) is None:
            raise ValidationError(error_message)


class BookSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Int(required=True)

    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_by_title(title) is not None:
            raise ValidationError(
                f'Book with title "{title}" already exists, '
                'please use a different title.'
            )

    @validates('author')
    def validate_author(self, author: int) -> None:
        self.validate_existence(get_author_by_id, author, "Author does not exist")

    @post_load
    def create_book(self, data: dict, **kwargs) -> Book:
        return Book(**data)


class AuthorSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    middle_name = fields.Str(required=False)

    @post_load
    def create_author(self, data: dict, **kwargs) -> Author:
        return Author(**data)
