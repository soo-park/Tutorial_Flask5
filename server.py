from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2

app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/application-form")
def form():
    first = request.form.get('first')
    last = request.form.get('last')
    salary = request.form.get('salary')
    job = request.form.get('job')

    return render_template("application-form.html", 
                           first=first, last=last, salary=salary,
                           job=job)


@app.route("/application-success")
def show_post():

    return render_template('application-response.html')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
