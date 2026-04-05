"""
Free API Template
Replace with your actual API implementation
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/joke')
def joke():
    return jsonify({
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "category": "programming"
    })

@app.route('/api/anime/<name>')
def anime(name):
    return jsonify({
        "name": name,
        "status": "Coming soon",
        "message": "API under development"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
