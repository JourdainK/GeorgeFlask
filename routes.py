import os

from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename

from . import app, models, db
from .models import produitForm,produit
from io import BytesIO



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

@app.route('/tous_produits')
def tous_produits():
    liste_produits = models.produit.query.order_by(models.produit.id_categorie).all()
    liste_attributs = models.vue_attributs.query.all()

    return render_template('tous_produits.html', title='Nos produits', produits=liste_produits,  typeprod=type(liste_produits), attributs=liste_attributs, typeatr=type(liste_attributs))

@app.route('/ajout_produit', methods=['GET','POST'])
def ajout_produit():
    form = produitForm()

    #https://flask-wtf.readthedocs.io/en/1.0.x/form/#file-uploads
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('static/images', f.filename))
        path_photo = 'images/'+f.filename
        photo_data = f.read()
        nouveau_produit = models.produit(nom_produit=form.nom_produit.data, description=form.description.data, prix=form.prix.data, photo=path_photo, id_categorie=form.id_categorie.data)
        db.session.add(nouveau_produit)
        db.session.commit()

        return redirect(url_for('accueil'))
    return render_template('ajout_produit.html',title='Ajout d\'un produit', form=form)




@app.route('/about')
def about():
    return render_template('about.html', title='About')
