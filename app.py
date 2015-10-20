from flask import Flask
import wikipedia
app = Flask(__name__)


@app.route('/')
def hello():
    return wikipedia.summary("Wikipedia")

@app.route('/<term>')
def search_wiki(term):
    
    return wikipedia.page(term).content

if __name__ == '__main__':
    app.run()
