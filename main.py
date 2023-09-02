from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template
import json

app = Flask(__name__)

COINS = [
  {
    'id': 1,
    'description': 'Cardano',
    'coin': 'ADA',
    'price': 0.25,
    'holdings_usdt': 100,
    'holdings_asset': 2000,
    'avg_puy_price': 0.29,
    'p_l_usdt': -22,
    'p_l_proc': '22%'
  },
  {
    'id': 2,
    'description': 'Polygon',
    'coin': 'MATIC',
    'price': 5.25,
    'holdings_usdt': 200,
    'holdings_asset': 1000,
    'avg_puy_price': 5.11,
    'p_l_usdt': 11,
    'p_l_proc': '11%'
  }
]

@app.route('/')
def homepage():
  return render_template("basic.html",
                         titlu_pagina="dobremha-coins",
                         wallet="SAFEPAL",
                         coins=COINS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
