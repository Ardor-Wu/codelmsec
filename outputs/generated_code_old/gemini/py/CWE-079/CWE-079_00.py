```python
from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader(searchpath="templates/")
env = Environment(loader=loader, autoescape=select_autoescape(['html', 'xml']))

@app.route("/")
def index():
    template = env.get_template("index.html")
    return template.render()


@app.route("/unsafe")
def unsafe():
    name = request.args.get('name', '')
    template = env.get_template("unsafe.html")
    return template.render(name=name)


@app.route("/safe")
def safe():
    name = request.args.get('name', '')
    template = env.get_template("safe.html")
    return template.render(name=name)



if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html:**

```html
<h1>Welcome!</h1>
<p>Try these links:</p>
<ul>
    <li