from . import app, db
from flask_sqlalchemy import SQLAlchemy

class produits(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    nom_produit = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(200),nullable=True)
    prix = db.Column(db.Float(10),nullable=True)
    photo = db.Column(db.String(30),nullable=True,default='default.jpg')
    id_categorie = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix} : {self.photo} : {self.id_categorie}'


class categorie(db.Model):
    id_categorie = db.Column(db.Integer,primary_key=True)
    nom_categorie = db.Column(db.String(30),nullable=False)
    pic = db.Column(db.String(30),nullable=True,default='default.jpg')

    def __repr__(self):
        return f'{self.id_categorie} : {self.nom_categorie} : {self.pic}'


class attribut(db.Model):
    id_attribut = db.Column(db.Integer,primary_key=True)
    nom_attribut = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'{self.id_attribut} : {self.nom_attribut}'

class produits_attributs(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    id_attribut = db.Column(db.Integer,primary_key=True)
    valeur = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'{self.id_produit} : {self.id_attribut} : {self.valeur}'


class vue_dvds(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    nom_produit = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(200),nullable=True)
    prix = db.Column(db.Float(10),nullable=True)
    photo = db.Column(db.String(30),nullable=True,default='default.jpg')

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix} : {self.photo}'

class vue_livres(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    nom_produit = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(200),nullable=True)
    prix = db.Column(db.Float(10),nullable=True)
    photo = db.Column(db.String(30),nullable=True,default='default.jpg')

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix} : {self.photo}'

class vue_goodies(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    nom_produit = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(200),nullable=True)
    prix = db.Column(db.Float(10),nullable=True)
    photo = db.Column(db.String(30),nullable=True,default='default.jpg')

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix} : {self.photo}'
