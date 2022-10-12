from flask import Flask, make_response, render_template, jsonify, request


from src.packages import Packages
from src.settings.Config import Config

packages = Packages()
app = Flask(__name__, template_folder="static")


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
    return True
