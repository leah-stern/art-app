from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	# app.run(host='0.0.0.0')
	app.run(debug=True)