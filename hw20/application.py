from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean

# Database setup
engine = create_engine('sqlite:///library.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Flask app setup
app = Flask(__name__)


# Models
class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)


class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_students_with_scholarship(cls):
        session = Session()
        students_with_scholarship = session.query(cls).filter(cls.scholarship == True).all()
        student_list = [{"id": student.id, "name": student.name, "surname": student.surname} for student in
                        students_with_scholarship]
        session.close()
        return jsonify(student_list)

    @classmethod
    def get_students_with_higher_average_score(cls, score):
        session = Session()
        students_higher_score = session.query(cls).filter(cls.average_score > score).all()
        student_list = [{"id": student.id, "name": student.name, "surname": student.surname} for student in
                        students_higher_score]
        session.close()
        return jsonify(student_list)


class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(Date, nullable=False)
    date_of_return = Column(Date)

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now().date() - self.date_of_issue).days


def initialize_db():
    Base.metadata.create_all(engine)
    session = Session()

    # Add authors
    author1 = Authors(name='John', surname='Doe')
    author2 = Authors(name='Jane', surname='Smith')
    session.add_all([author1, author2])
    session.commit()

    # Add books with correct author_ids
    book1 = Books(name='Book 1', release_date=datetime(2020, 1, 15).date(), author_id=author1.id)
    book2 = Books(name='Book 2', release_date=datetime(2019, 5, 20).date(), author_id=author2.id)
    session.add_all([book1, book2])

    # Add students
    student1 = Students(name='Alice', surname='Johnson', phone='123456789', email='alice@example.com',
                        average_score=85.0, scholarship=True)
    student2 = Students(name='Bob', surname='Smith', phone='987654321', email='bob@example.com', average_score=78.0,
                        scholarship=False)
    session.add_all([student1, student2])
    session.commit()
    session.close()


# Routes
@app.route('/books', methods=['GET'])
def get_all_books():
    session = Session()
    books = session.query(Books).all()
    book_list = [{"id": book.id, "name": book.name, "release_date": book.release_date.isoformat()} for book in books]
    session.close()
    return jsonify(book_list)


@app.route('/debtors', methods=['GET'])
def get_debtors():
    session = Session()
    debtors = session.query(ReceivingBooks).filter(ReceivingBooks.count_date_with_book > timedelta(days=14)).all()
    debtor_list = [{"student_id": debtor.student_id, "book_id": debtor.book_id} for debtor in debtors]
    session.close()
    return jsonify(debtor_list)


@app.route('/issue_book', methods=['POST'])
def issue_book():
    session = Session()
    book_id = request.json.get('book_id')
    student_id = request.json.get('student_id')
    book = session.query(Books).filter(Books.id == book_id).first()
    if book and book.count > 0:
        issuance = ReceivingBooks(book_id=book_id, student_id=student_id, date_of_issue=datetime.now().date())
        session.add(issuance)

        book.count -= 1

        session.commit()
        session.close()
        return jsonify({"message": "Book issued successfully"})
    else:
        session.close()
        return jsonify({"error": "Book not available or invalid book ID"})


@app.route('/return_book', methods=['POST'])
def return_book():
    session = Session()
    book_id = request.json.get('book_id')
    student_id = request.json.get('student_id')

    return_record = session.query(ReceivingBooks).filter(
        ReceivingBooks.book_id == book_id,
        ReceivingBooks.student_id == student_id,
        ReceivingBooks.date_of_return == None).first()

    if return_record:
        return_record.date_of_return = datetime.now().date()

        book = session.query(Books).filter(Books.id == book_id).first()
        if book:
            book.count += 1

        session.commit()
        session.close()
        return jsonify({"message": "Book returned successfully"})
    else:
        session.close()
        return jsonify({"error": "No such record found"})


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)

