from flask import render_template, redirect, url_for, request
from . import app, models

@app.route('/')
def accueil():
    liste_categories = models.categorie.query.all()
    return render_template('accueil.html', title='George Carlin Website', liste_cat=liste_categories,typecat=type(liste_categories))

@app.route('/categorie')
def categorie():
    liste_categories = models.categorie.query.all()
    return render_template('categorie.html', title='George Carlin Website - Produits', liste_cat=liste_categories, typecat=type(liste_categories))