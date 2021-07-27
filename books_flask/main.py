from flask import Flask, jsonify
from books import Book
from flask_cors import *

# 小写的 flask 是库，大写开头的 Flask 是类
app = Flask(__name__)
CORS(app, supports_credentials=True) 


# __name__ 是文件的文字，就是main
app.config['JSON_AS_ASCII'] = False

@app.route('/books_cates', methods=['GET'])
def get_books_cates():
    resData = {
        'resCode':0,
        'data':[
            {"id":0, "text":'首页', "url":'/'},
            {"id":1, "text":'玄幻', "url":'/xuanhuan'},
            {"id":2, "text":'修真', "url":'/xiuzhen'},
            {"id":3, "text":'都市', "url":'/dushi'},
            {"id":4, "text":'历史', "url":'/lishi'},
            {"id":5, "text":'网游', "url":'/wangyou'},
            {"id":6, "text":'科幻', "url":'/kehuan'},
            {"id":7, "text":'言情', "url":'/yanqing'},
            {"id":8, "text":'其他', "url":'/qita'},
            {"id":9, "text":'完本', "url":'/wanben'}
        ],
        'message': '对本次请求的说明'
    }
    return jsonify(resData)

# 这个是路由，就是访问的路径
@app.route('/')
def hello_world():
    book = Book()
    data = book.get_books_infos_limit()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
