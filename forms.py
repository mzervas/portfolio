from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField


class ContactForm(Form):
  name = TextField("Name")
  email = EmailField("Email")
  passw = TextField("Password")

  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Submit")
