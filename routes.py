from flask import render_template, redirect, url_for, request
from . import app

@app.route('/')
def accueil():
    return render_template('accueil.html', title='George Carlin Website - Accueil')

@app.route('/produits')
def catalogue_de_produits():
    return '<h2>Nos produits :</h2>'