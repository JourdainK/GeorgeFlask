from flask import render_template, redirect, url_for, request
from . import app, models


@app.route('/')
def accueil():
    liste_categories = models.categorie.query.all()
    return render_template('accueil.html', title='George Carlin Website', liste_cat=liste_categories, typecat=type(liste_categories))




@app.route('/produits_categorie')
def produits_categorie():
    id_categ = request.args.get('id_categorie')
    liste_produits = models.vue_produits_categories.query.filter_by(id_categorie=id_categ).all()
    liste_attributs = models.vue_attributs.query.all()

    return render_template('produits_categorie.html', title='Nos produits', produits=liste_produits,  typeprod=type(liste_produits) , attributs=liste_attributs, typeatr=type(liste_attributs))


