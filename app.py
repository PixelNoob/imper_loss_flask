from flask import Flask, request as r, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=["GET",'POST'])
def telos():
    if r.method == "POST" and r.form['asset1']:
        try:
            asset1 = float(r.form['asset1'])
            asset1 = asset1 / 100
            asset2 = float(r.form['asset2'])
            asset2 = asset2 / 100
            calc = (1.0 + asset1) / (1.0 + asset2)
            il = 1 - (calc ** 0.5) / (0.5 * calc + 0.5)
            il = round(il * 100, 2)
            return render_template("index.html", il = '{}%'.format(il))
        except:
            return render_template("index.html", il = 'Please insert a valid number from 0-100')
    else:
        return render_template("index.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
