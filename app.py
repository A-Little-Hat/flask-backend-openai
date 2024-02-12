from flask import Flask, request
from langchain.tools import DuckDuckGoSearchRun 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
search = DuckDuckGoSearchRun()


@app.route('/')
def hello_world():
    return "working"

@app.route('/qa')
def qa():
    question = request.args.get('q')
    res={"res":search.run(question)}
    return res
 
# main driver function
if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")