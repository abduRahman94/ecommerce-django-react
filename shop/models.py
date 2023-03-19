from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    libelle = models.CharField(max_length=200)


class Produit(models.Model):
    libelle = models.CharField(max_length=200)
    prix = models.FloatField(null=True)
    description = models.TextField(null=True)
    quantite_stock = models.IntegerField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)


class Client(User):
    
    def passer_commande(self):
        pass
    
    def annuler_commande(self):
        pass
    
    def modifier_commande(self):
        pass

class Commande(models.Model):
    class StatusCommande(models.IntegerChoices):
        VALIDE = 1
        ANNULE = 2
        ATTENTE = 3
    
    code_commande = models.CharField(max_length=200)
    client = models.ForeignKey(Client)
    produit = models.ForeignKey(Produit)
    statut_commande = models.IntegerField(choices=StatusCommande.choices)
    