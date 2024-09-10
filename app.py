from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from backend.functions import factorial, add_comment
import sqlite3
import os

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')
CORS(app)

comDB = sqlite3.connect("database/comments.db")
comCur = comDB.cursor()

with open('database/create_table.sql', 'r') as query:
        comCur.execute(query.read())
        comDB.commit()

num = -1

comCur.execute("SELECT * FROM comments")
comments = comCur.fetchall()[::-1]
print(comments)
comDB.commit()

@app.route('/')
def main():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_data():
    data = {
        'num': num,
        'comments': comments
    }
    print(data['num'])
    return jsonify(data)

@app.route('/getFact', methods=["POST"])
def fact():
    intnum = int(request.form.get('fact'))
    global num
    num = factorial(intnum)
    print(num)
    global comments
    return jsonify({'num': num, 'comments': comments})

@app.route('/comment', methods=["GET", "POST"])
def comment():
    name = request.form.get('username')
    comment = request.form.get('comment')
    tup = [name, comment]
    add_comment(tup)
    
    global comments
    comDB = sqlite3.connect("database/comments.db")
    comCur = comDB.cursor()
    comCur.execute("SELECT * FROM comments")
    comments = comCur.fetchall()[::-1]
    print(comments)
    return jsonify({'num': num, 'comments': comments})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)