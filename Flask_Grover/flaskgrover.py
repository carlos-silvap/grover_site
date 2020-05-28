from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/UMA")
def UMA():
    return render_template('UMA.html', title='UMA')

@app.route("/livestream")
def livestream():
    return render_template('livestream.html', title='Live')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/concept")
def concept():
    return render_template('concept.html', title='Pruebas de concepto')

@app.route("/sim")
def sim():
    return render_template('sim.html', title='Simulación')

if __name__ == '__main__':
    app.run(debug=True)
