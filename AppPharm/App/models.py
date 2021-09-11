from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator 
import uuid

# Create your models here.
class Dci (models.Model):
    Id=models.UUIDField(default=uuid.uuid4, editable=False)
    Nom=models.TextField(max_length=20 ,primary_key=True,verbose_name='DCI ')

    def __str__(self):
        return self.Nom

class Laboratoire(models.Model):
    Id=models.UUIDField(default=uuid.uuid4, editable=False)
    Nom_labo=models.CharField(max_length=20 ,primary_key=True, verbose_name='Laboratoire ')
    Tel=models.CharField(max_length=8 , null=True,verbose_name='Téléphone ')
    Adresse=models.CharField(max_length=50 , null=True)

    def __str__(self):
        return self.Nom_labo

class Classe_thérapeutique(models.Model):
    Id=models.UUIDField(default=uuid.uuid4, editable=False)
    Nom_thérapeutique=models.CharField(max_length=20 , primary_key=True,  verbose_name='Classe Thérapeutique ')

    def __str__(self):
        return self.Nom_thérapeutique

class Sous_classe(models.Model):
    Id=models.UUIDField(default=uuid.uuid4, editable=False)
    Nom_classe=models.CharField(max_length=20 , primary_key=True, verbose_name='Sous Classe ')

    def __str__(self):
        return self.Nom_classe

class Product (models.Model): 
    Nom_C=models.CharField(primary_key=True,max_length=20,verbose_name='Nom commercial ')
    N_Lot=models.CharField(max_length=20 , null=True, default='None',verbose_name='Numéro de lot ') 
    Dosage=models.CharField(max_length=20 , null=True,verbose_name='Dosage ')
    Forme=models.CharField(max_length=20 , null=True,verbose_name='Forme ')
    Présentation=models.CharField(max_length = 150, null=True,verbose_name='Présentation ')
    Dci_Nom=models.ForeignKey(Dci, on_delete=models.CASCADE ,verbose_name='DCI ')
    Labo=models.ForeignKey(Laboratoire, on_delete=models.CASCADE, verbose_name='Laboratoire ')
    Classe_thérapeutique_Nom=models.ForeignKey(Classe_thérapeutique, on_delete=models.CASCADE, verbose_name='Classe Thérapeutique ')
    Sous_classe_Nom=models.ForeignKey(Sous_classe, on_delete=models.CASCADE, verbose_name='Sous Classe ')
    Conditionnement=models.CharField(max_length=20 , null=True,verbose_name='Conditionnement ')
    Spécification=models.CharField(max_length=20 , null=True,verbose_name='Spécification ')
    Tableau=models.CharField(max_length=20 , null=True,verbose_name='Tableau ')
    Durée_conservation=models.CharField(max_length=20 , null=True,verbose_name='Durée Conservation ')
    Price=models.DecimalField(max_digits=20, decimal_places=3 , null=True,verbose_name='Price ')
    Qte=models.PositiveIntegerField(null=True,validators=[MinValueValidator(1)],verbose_name='Quantité ')
    

    def __str__(self): 
        return self.Nom_C

    def Is_Active (self):
        if self.Qte == 0 :
            return False
        else:
            return True

class Product_added(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    Nom_C=models.ForeignKey(Product, on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_C.Nom_C

class Product_edit(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    Nom_C=models.ForeignKey(Product, on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_C.Nom_C

class Dalete_product(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(null=True,max_length=20,verbose_name='Nom utilisateur ')
    Nom_C=models.CharField(null=True,max_length=20,verbose_name='Nom commercial ')
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_C.Nom_C

class Pharmaci(models.Model):
    Id=models.UUIDField(default=uuid.uuid4, editable=False)
    Nom_Ph = models.CharField(max_length = 20 , primary_key=True,verbose_name='Pharmaci ')
    Numéro_Inscription=models.CharField(max_length=50 ,null=True,verbose_name='Numéro Inscription ')
    Tel=models.CharField(max_length=8,null=True,verbose_name='Téléphone ')
    Adresse = models.CharField(max_length = 50, null=True,verbose_name='Adresse ')

    def __str__(self):        
        return self.Nom_Ph

class Echange (models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nom_Ph=models.ForeignKey(Pharmaci, on_delete=models.CASCADE)   
    Nom_C=models.ForeignKey(Product, on_delete=models.CASCADE)
    Qte=models.PositiveIntegerField(null=True,validators=[MinValueValidator(1)], verbose_name='Quantité ')
    
    def __str__(self):        
        return self.Nom_Ph.Nom_Ph 
    
class Echange_added(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    Nom_C=models.ForeignKey(Product, on_delete=models.CASCADE)
    Nom_Ph = models.ForeignKey(Pharmaci, on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_Ph.Nom_Ph

class Dalete_echange(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(null=True,max_length=20,verbose_name='Nom utilisateur ')
    Nom_C=models.CharField(null=True,max_length=20,verbose_name='Nom commercial ')
    Nom_Ph = models.CharField(null=True,max_length = 20 ,verbose_name='Pharmaci ')
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_C

class Vente(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nom_C=models.CharField(null=True,max_length=20,verbose_name='Nom commercial ')
    Qte=models.PositiveIntegerField(null=True,validators=[MinValueValidator(1)] ,verbose_name='Quantité')
    Date=models.DateTimeField(auto_now_add=True)

    def Price_total(self):
        return self.Qte*self.Nom_C.Price

    def __str__(self):        
        return self.Nom_C.Nom_C
  
class Vente_added(models.Model):
    Id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    Nom_C=models.ForeignKey(Product, on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_C.Nom_C


