
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


# # CREATE RECORD
# new_book = Book(id=333, title="sdf asdasd", author="J. K. asdasd", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

all_books = [{
    "name": "Harry Potter",
    "author": "J. K. Rowling",
    "rate": 9,
}]


class booksss:
    def __init__(self, name, author, rate):
        self.name = name
        self.author = author
        self.rate = rate


@app.route('/')
def home():
    dat = Book.query.all()
    print(dat)
    return render_template('index.html', books=dat)


@app.route('/edit/<int:id>')
def edit(id):

    # book = Book.query.get(id)
    return render_template('edit.html', id=id)


@app.route('/editor<int:id>', methods=['POST'])
def editAdd(id):
    print('>>>>>>>>>>>>>>>>>', id)
    book = Book.query.get(id)
    book.title = request.form['title']
    book.author = request.form['auth']
    book.rating = request.form['rate']
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete/<int:id>")
def delete(id):

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/abook')
def add_book():
    return render_template('add.html')


@app.route("/add", methods=['POST'])
def add():

        # CREATE RECORD
    new_book = Book(
        title=request.form["name"],
        author=request.form["auth"],
        rating=request.form["rate"]
    )
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('home'))
    # return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
