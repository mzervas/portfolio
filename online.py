from flask import Flask, render_template, request
from flask.ext.mail import Message, Mail   	#Import files -- capitalization import!\
from forms import ContactForm
mail = Mail()
app = Flask(__name__)		#Initialize application


app.secret_key = 'WebDesign'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'umsiwebdesign@gmail.com'
app.config["MAIL_PASSWORD"] = '105sstate'

mail.init_app(app)


x = open("strings.txt","r")
y = x.read()

@app.route('/x')
def tryThis():
	return y


@app.route('/')				#Define route
def index():
    return render_template("index.html", name="index")

@app.route('/index')
def something():
	return render_template("index.html", name="index")

@app.route('/about')
def somethingElse():
	return render_template("about.html", name="about")

@app.route('/skills')
def somethingMore():
	return render_template("skills.html", name="skills")

@app.route('/photos')
def somethingAgain():
	return render_template("photos.html", name="photos")

@app.route('/proj')
def somethingNew():
	return render_template("project.html")

@app.route('/contact', methods=['GET','POST'])
def idk():
	form = ContactForm()

	if request.method == 'POST':
		msg = Message(form.subject.data, sender="merrizervas@gmail.com", recipients=["mzervas@umich.edu"])
		msg.body = """
			From: %s <%s>
			%s""" % (form.name.data, form.email.data, form.message.data)
		mail.send(msg)
		return render_template('contact.html', form=form, message="Thank you for sumitting your information!", name="contact")

	elif request.method == 'GET':
		return render_template("contact.html", form=form, name="contact")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', name="index"), 404

if __name__ == '__main__':	#Start the Development server
    app.run(debug=True)
