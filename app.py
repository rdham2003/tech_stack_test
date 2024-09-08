from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from backend.functions import factorial

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')
CORS(app)

num = -1

@app.route('/')
def main():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_data():
    data = {
        'num': num
    }
    print(data['num'])
    return jsonify(data)

@app.route('/getFact', methods=["POST"])
def fact():
    intnum = int(request.form.get('fact'))
    global num
    num = factorial(intnum)
    print(num)
    return jsonify({'num': num})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)