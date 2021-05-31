from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


todos = ["1.Present Yourself - who you are! ", "2.Present a Project/Achievement", "Present Snyk", "Slides on Snyk", "Technical Demo Snyk"]



class TodoForm(FlaskForm):
    todo = StringField("Todo")
    submit = SubmitField("Add Todo")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'todo' in request.form:
        todos.append(request.form['todo'])     
    return render_template('index.html', todos=todos, template_form=TodoForm())