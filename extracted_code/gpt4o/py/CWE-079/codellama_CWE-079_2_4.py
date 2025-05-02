from flask import Flask, request, make_response

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return make_response('<h1>Page not found</h1>', 404)

if __name__ == '__main__':
    app.run(debug=True)
