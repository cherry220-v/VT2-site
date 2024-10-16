from flask import Flask, render_template, send_file
import os, zipfile

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=["GET"])
def updatePlugins():
    if os.path.isfile("plugins.zip"): os.remove("plugins.zip")
    zipf = zipfile.ZipFile("plugins.zip", "w")
    for f in os.listdir("plugins"):
        zipf.write(os.path.join("plugins", f))
    zipf.close()
    return send_file("plugins.zip")

@app.route('/docs/<string:doc>')
def func_name(doc):
    return render_template('expression')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 