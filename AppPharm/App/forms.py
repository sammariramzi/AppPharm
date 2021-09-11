from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type='date'

class Edit_Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields = (
            'N_Lot',
            'Dosage',
            'Forme',
            'Présentation',
            'Dci_Nom',
            'Labo',
            'Classe_thérapeutique_Nom',
            'Sous_classe_Nom',
            'Conditionnement',
            'Spécification',
            'Tableau',
            'Durée_conservation',
            'Price',
            'Qte',
        )

class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields = (
            'Nom_C',
            'N_Lot',
            'Dosage',
            'Forme',
            'Présentation',
            'Conditionnement',
            'Spécification',
            'Tableau',
            'Durée_conservation',
            'Price',
            'Qte',
        )

class DciForm(forms.ModelForm):
    class Meta:
        model=Dci
        fields='__all__'

class LaboratoireForm(forms.ModelForm):
    class Meta:
        model=Laboratoire
        fields='__all__'

class Classe_thérapeutiqueForm(forms.ModelForm):
    class Meta:
        model=Classe_thérapeutique
        fields='__all__'

class Sous_classeForm(forms.ModelForm):
    class Meta:
        model=Sous_classe
        fields='__all__'

class PharmaciForm(forms.ModelForm):
    class Meta:
        model=Pharmaci
        fields='__all__'

class EchangeForm(forms.ModelForm):
    class Meta:
        model=Echange
        fields=['Nom_C','Qte']
        labels={
            'Nom_C':'Nom commercial ',
        }
        
class VenteForm(forms.ModelForm):
    class Meta:
        model=Vente
        fields=['Qte']
        labels ={
            'Qte':'',
        }

class New_user(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','groups']
        labels ={
            'username':'Nom Utilisateur',
            'password1':'Mot De Passe',
            'password2':'Confirmation Mot De Passe',
            'first_name':'Nom',
            'last_name':'Prenom',
            'email':'Email',
            'groups':'groupe',
        }

class Update_user(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','groups','is_active']
        labels ={
            'username':'Nom Utilisateur',
            'first_name':'Nom',
            'last_name':'Prenom',
            'email':'Email',
            'groups':'groupe',
        }
