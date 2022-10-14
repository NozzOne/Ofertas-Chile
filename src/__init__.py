from gevent import monkey;monkey.patch_all()
from flask import Flask, render_template

from src.packages import Packages





packages = Packages()
app = Flask(__name__, template_folder="static")
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
log.disabled = True

def getProducts():
    return [p.getOffers() for p in packages.getAll()]


@app.route("/")
def loading():
    return render_template("loading.html")


@app.route("/ofertas")
def showOfertas():
    return render_template("index.html", timer=packages.seconds, ofertas=getProducts())


@app.route("/crearOfertas")
def createOfertas():
    getProducts()
    return ("", 204)
