from flask import Flask, jsonify
from books import Book

# 小写的 flask 是库，大写开头的 Flask 是类
app = Flask(__name__)


# __name__ 是文件的文字，就是main
app.config['JSON_AS_ASCII'] = False

# 这个是路由，就是访问的路径
@app.route('/')
def hello_world():
    book = Book()
    data = book.get_books_infos_limit()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
