from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template
import json

app = Flask(__name__)


@app.route('/')
def homepage():
  return render_template("basic.html",
                         titlu_pagina="dobremha-coins",
                         wallet="SAFEPAL",
                         user_is_authenticated=False)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
