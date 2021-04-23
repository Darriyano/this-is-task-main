import sys

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/list_prof/<list_prof>')
def login(list_prof):
    li = ["штурман", "киберинженер", "астрогеолог", "пилот", "пилот дронов", "климатолог", "оператор марсохода", "метеоролог", "гляциолог"]
    return render_template('login.html', title='Professions', lp=list_prof, li=li)





if __name__ == '__main__':
    # au = []
    # for x in sys.stdin:
    #     au.append(x.rstrip())
    app.run(host='127.0.0.1', port=8080)
