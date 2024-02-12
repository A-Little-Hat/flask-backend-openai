from flask import Flask, request
from langchain.tools import DuckDuckGoSearchRun 

app = Flask(__name__)
search = DuckDuckGoSearchRun()


@app.route('/')
def hello_world():
    return "working"

@app.route('/qa')
def qa():
    question = request.args.get('q')
    return search.run(question)
 
# main driver function
if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")