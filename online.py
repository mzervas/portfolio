from flask import Flask, render_template
#from flask.ext.mail import Message, Mail   	#Import files -- capitalization import!
app = Flask(__name__)		#Initialize application
#mail = Mail()
#app.config["MAIL_SERVER"]




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

@app.route('/contact')
def somethingLast():
	return render_template("contact.html", name="contact")

@app.route('/proj')
def somethingNew():
	return render_template("project.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', name="index"), 404

if __name__ == '__main__':	#Start the Development server
    app.run(debug=True)
