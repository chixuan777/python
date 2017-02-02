##pip install flask-bootstrap
from flask import Flask,render_template,session,url_for,redirect,flash
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('User Name',validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ni cai'
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    nameForm = NameForm()

    if nameForm.validate_on_submit():
        newName = nameForm.name.data

        if newName == session.get('name'):
            session['name'] = nameForm.name.data
            nameForm.name.data = ''
            return redirect(url_for('index'))
        else:
            flash('Warning! Bad Name')


    return render_template('index.html',form=nameForm,name=session.get('name'))

if __name__ == '__main__':
    app.run('0.0.0.0', 10086)