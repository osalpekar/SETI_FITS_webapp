'''
Webapp to query people on data from FITS files for RFI identification
'''

from flask import Flask
#from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("jumbotron_narrow.html")


if __name__ == "__main__":
    app.run(debug=True)
