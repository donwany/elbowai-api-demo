from flask import Flask, jsonify, request
from book_store import books

app = Flask(__name__)


@app.route("/api/v1/books", methods=['GET'])
def get_books():
    return jsonify({'data': books})


@app.route("/api/v1/books", methods=['POST'])
def create_book():
    # get the data from the user
    data = request.get_json()

    # get book_title
    title = data.get("book_title")
    author = data.get("book_author")
    publisher = data.get("publisher")
    description = data.get("description")

    book = {
        "id": len(books) + 1,
        "book_title": title,
        "book_author": author,
        "publisher": publisher,
        "description": description
    }
    books.append(book)

    return jsonify(books)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=1957, debug=True)
