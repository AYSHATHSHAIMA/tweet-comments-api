from flask import Flask, jsonify
from flask_cors import CORS
from comments import comments

app = Flask(__name__)
CORS(app)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

@app.route('/api/hide', methods=['POST'])
def hide_comments():
    return jsonify({"message": "All red flag comments hidden successfully!"})

if __name__ == '__main__':
    app.run(debug=True)