from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
from django.utils.decorators import method_decorator

from .decorators import unauthenticate_user, allowed_users
from .models import *
from .forms import *


@unauthenticate_user
def login_views(request):
    if (request.method == 'POST'):
        username= request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username , password=password)
        if (user is not None):
            login(request , user)
            messages.success(request, f'Connexion réussie pour {username}' )
            return redirect('App:ventes')
        else:
            messages.error(request ,'Nom utilisateur ou mot de passe incorrect, réessayez !')
    
    context={
        'loginform' : AuthenticationForm
    }
    return render(request, 'App/login.html',context) 

@login_required(login_url='App:login')
def logout_views (request):
    logout(request)
    messages.info(request, 'déconnecté avec succès')
    return redirect('App:login')

@login_required(login_url='App:login')
def list_vente(request):
    product=Product.objects.all()
    context={
       'product':product, 
       'venteForm':VenteForm
    }
    return render(request ,'App/vente_list.html' , context)

@login_required(login_url='App:login')
def historique_vente(request):
    vente=Vente.objects.all()
    context={
        'vente':vente,
    }
    return render(request ,'App/historique_vente.html', context)

@login_required(login_url='App:login')
def add_vente(request,pk):
    product=Product.objects.get(Nom_C=pk)
    vente=Vente()
    form=VenteForm(request.POST)
    if (request.method == 'POST'):
        if form.is_valid():
            if form.cleaned_data['Qte']>product.Qte :
                messages.error(request,f'Quantité disponible est {product.Qte}')
            else:
                vente.Nom_C=product
                vente.Qte=form.cleaned_data['Qte']
                vente.save()

                total_qte=product.Qte
                qte_vente=form.cleaned_data['Qte']
                Product.objects.filter(Nom_C=pk).update(Qte=total_qte-qte_vente)

                vente_added=Vente_added()
                vente_added.username=User.objects.get(username=request.user.username)
                vente_added.Nom_C=Product.objects.get(Nom_C=pk)
                vente_added.save()

                messages.success(request,'vente Ajouté avec succès')
        return redirect('App:ventes')
        
@login_required(login_url='App:login')
def list_product(request):
    product=Product.objects.all()
    context={
        'product':product,
    }
    return render(request ,'App/list_product.html', context)
    
@login_required(login_url='App:login')
def add_product(request):
    if (request.method == 'POST'):
        form=Productform(request.POST)
        product=Product()
        if form.is_valid():
            product.Dci_Nom=Dci.objects.get(Id=request.POST['dci'])     
            product.Labo=Laboratoire.objects.get(Id=request.POST['Laboratoire'])     
            product.Classe_thérapeutique_Nom=Classe_thérapeutique.objects.get(Id=request.POST['Classe_Therapeutique'])       
            product.Sous_classe_Nom=Sous_classe.objects.get(Id=request.POST['Sous_Classe'])
            product.Nom_C=form.cleaned_data['Nom_C']
            product.N_Lot=form.cleaned_data['N_Lot']
            product.Dosage=form.cleaned_data['Dosage']
            product.Forme=form.cleaned_data['Forme']
            product.Présentation=form.cleaned_data['Présentation']
            product.Conditionnement=form.cleaned_data['Conditionnement']
            product.Spécification=form.cleaned_data['Spécification']
            product.Tableau=form.cleaned_data['Tableau']
            product.Durée_conservation=form.cleaned_data['Durée_conservation']
            product.Price=form.cleaned_data['Price']
            product.Qte=form.cleaned_data['Qte']
            product.save()

            edit=Product_added()
            edit.username=User.objects.get(username=request.user.username)
            edit.Nom_C=Product.objects.get(Nom_C=form.cleaned_data['Nom_C'])
            edit.save()

            messages.success(request,'Médicament ajouté avec succès')
                 

    context={
        'productform':Productform,
        'DciForm':DciForm,
        'LaboratoireForm':LaboratoireForm,
        'Classe_thérapeutiqueForm':Classe_thérapeutiqueForm,
        'Sous_classeForm':Sous_classeForm,
    }
    return render(request, 'App/add_product.html',context )

@login_required(login_url='App:login')
def edit_product(request , pk):
    product=Product.objects.get(Nom_C=pk)
    form=Edit_Productform(instance=product)
    if (request.method == 'POST'):
        form=Edit_Productform(request.POST, instance=product)
        if form.is_valid() and form.changed_data:
            form.save()

            edit=Product_edit()
            edit.username=User.objects.get(username=request.user.username)
            edit.Nom_C=Product.objects.get(Nom_C=pk)
            edit.save()

            messages.success(request,'Médicament mis à jour avec succès')
            return redirect('App:list_product')

    context={
        'Edit_Productform':form,
    }
    return render(request, 'App/edit_product.html', context )

@login_required(login_url='App:login')
def detail_product(request , pk):
    product=Product.objects.get(Nom_C=pk)
    context={
        'product':product
    }
    return render(request, 'App/detail_product.html', context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def dalete_product(request ,pk):
    product=Product.objects.get(Nom_C=pk)
    if (request.method == 'POST'):
        dalete=Dalete_product()
        dalete.username=request.user.username
        dalete.Nom_C=pk
        dalete.save()
        product.delete()
        messages.success(request,'Médicament supprimé avec succès')
        return redirect('App:list_product')

    context={
        'product':product
    }
    return render(request, 'App/dalete_product.html', context )

@method_decorator(login_required(login_url='App:login') , name='dispatch')
class Dci_view (View):
    def get(self,request, *args, **kwargs):
        if request.is_ajax():
            dci = Dci.objects.all()
            dci=serializers.serialize('json',dci)
            return JsonResponse({'data':dci},safe=False)
        else:
            return HttpResponse('hhhhhhh')
    
    def add_Dci(request, *args, **kwargs):
        if request.is_ajax():
            nom=request.POST['nom']
            nom=nom.strip()
            dci=Dci()
            dci.Nom=nom
            dci.save()
            return HttpResponse('error in add_Dci')

@method_decorator(login_required(login_url='App:login') , name='dispatch')
class Labo_view(View):
    def get(self,request, *args, **kwargs):
        if request.is_ajax():
            laboratoire = Laboratoire.objects.all()
            laboratoire=serializers.serialize('json',laboratoire)
            return JsonResponse({'data':laboratoire},safe=False)

    def add_Labo(request, *args, **kwargs):
        if request.is_ajax():
            nom=request.POST['nom']
            tel=request.POST['tel']
            adresse=request.POST['adresse']
            Labo=Laboratoire()
            Labo.Nom_labo=nom
            Labo.Tel=tel
            Labo.Adresse=adresse
            Labo.save()
            return HttpResponse('error in add_Dci')

@method_decorator(login_required(login_url='App:login') , name='dispatch')
class Therapeutique_view(View):
    def get(self,request, *args, **kwargs):
        if request.is_ajax():
            classe_thérapeutique = Classe_thérapeutique.objects.all()
            classe_thérapeutique=serializers.serialize('json',classe_thérapeutique)
            return JsonResponse({'data':classe_thérapeutique},safe=False)

    def add_Therapeutique(request, *args, **kwargs):
        if request.is_ajax():
            nom=request.POST['nom']
            thérapeutique=Classe_thérapeutique()
            thérapeutique.Nom_thérapeutique=nom
            thérapeutique.save()
            return HttpResponse('error in add_Therapeutique')

@method_decorator(login_required(login_url='App:login') , name='dispatch')
class Sous_classe_view(View):
    def get(self,request, *args, **kwargs):
        if request.is_ajax():
            sous_classe = Sous_classe.objects.all()
            sous_classe=serializers.serialize('json',sous_classe)
            return JsonResponse({'data':sous_classe},safe=False)

    def add_Sous_classe(request, *args, **kwargs):
        if request.is_ajax():
            nom=request.POST['nom']
            sous_classe=Sous_classe()
            sous_classe.Nom_classe=nom
            sous_classe.save()
            return HttpResponse('error in add_Sous_classe')

@login_required(login_url='App:login')
def list_echange(request):
    echange=Echange.objects.all()
    context={
        'echange':echange,
    }
    return render(request ,'App/list_echange.html', context)

@login_required(login_url='App:login')
def detail_pharmaci(request , pk):
    pharmaci=Pharmaci.objects.get(Nom_Ph=pk)
    context={
        'pharmaci':pharmaci
    }
    return render(request, 'App/detail_pharmaci.html', context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def add_echange(request):
    if (request.method == 'POST'):
        form=EchangeForm(request.POST)
        echange=Echange()
        if form.is_valid():
            echange.Nom_Ph=Pharmaci.objects.get(Id=request.POST['Pharmaci'])
            echange.Nom_C = Product.objects.get(Nom_C=form.cleaned_data['Nom_C'])
            echange.Qte=form.cleaned_data['Qte']
            echange.save()

            echange_added=Echange_added()
            echange_added.username=User.objects.get(username=request.user.username)
            echange_added.Nom_C=Product.objects.get(Nom_C=form.cleaned_data['Nom_C'])
            echange_added.Nom_Ph=Pharmaci.objects.get(Id=request.POST['Pharmaci'])
            echange_added.save()

            messages.success(request,'échange ajouté avec succès')
        

    context={
        'pharmaciForm':PharmaciForm,
        'echangeForm':EchangeForm,
    }
    return render(request, 'App/add_echange.html',context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def dalete_echange(request ,pk):
    echange=Echange.objects.get(Id=pk)
    if (request.method == 'POST'):
        dalete_echange=Dalete_echange()
        dalete_echange.username=User.objects.get(username=request.user.username)
        dalete_echange.Nom_C=echange.Nom_C
        dalete_echange.Nom_Ph=echange.Nom_Ph
        dalete_echange.save()
        echange.delete()
        messages.success(request,' échange supprimé avec succès')
        return redirect('App:list_echange')

    context={
        'echange':echange
    }
    return render(request, 'App/dalete_echange.html', context )

@method_decorator(login_required(login_url='App:login') , name='dispatch')
class Pharmaci_view (View):
    def get(self,request, *args, **kwargs):
        if request.is_ajax():
            pharmaci = Pharmaci.objects.all()
            pharmaci=serializers.serialize('json',pharmaci)
            return JsonResponse({'data':pharmaci},safe=False)
        
    def add_pharmaci(request, *args, **kwargs):
        if request.is_ajax():
            pharmaci=Pharmaci()
            pharmaci.Nom_Ph=request.POST['nom']
            pharmaci.Tel=request.POST['tel']
            pharmaci.Adresse=request.POST['adresse']
            pharmaci.save()
            return HttpResponse('add_pharmaci')

@login_required(login_url='App:login')
def actions(request):
    product_added=Product_added.objects.all()
    product_edit=Product_edit.objects.all()
    dalete_product=Dalete_product.objects.all()
    echange_added=Echange_added.objects.all()
    dalete_echange=Dalete_echange.objects.all()
    vente_added=Vente_added.objects.all()
    context={
        'product_added':product_added,
        'product_edit':product_edit,
        'dalete_product':dalete_product,
        'echange_added':echange_added,
        'dalete_echange':dalete_echange,
        'vente_added':vente_added,
    }
    return render(request, 'App/actions.html',context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def CreationUser(request):
    if (request.method == 'POST'):
        form=New_user(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='employé')
            user.groups.add(group)
            messages.success(request,'Utilisateur ajouter avec succès')
            return redirect('App:list_user')

    context={
        'New_user':New_user
    }
    return render(request, 'App/add_user.html',context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def edit_user(request , pk):
    user=User.objects.get(id=pk)
    form=Update_user(instance=user)
    if (request.method == 'POST'):    
        form=Update_user(request.POST, instance=user)
        if form.is_valid() and form.changed_data:
            form.save()
            group=form.cleaned_data['groups'].values()
            if group[0]['name'] == 'gerant':
                user.is_staff=True
                user.save()
            elif group[0]['name'] == 'employé':
                user.is_staff=False
                user.save()
            messages.success(request,'Utilisateur mis à jour avec succès')
            return redirect('App:list_user')
        return redirect('App:list_user')
    context={
        'edit_user':form,
        'user':user
    }
    return render(request, 'App/edit_user.html', context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def list_user(request):
    user=User.objects.all()
    context={
        'user':user,
    }
    return render(request ,'App/list_user.html', context)

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def detail_user(request , pk):
    user=User.objects.get(id=pk)
    context={
        'user':user,
    }
    return render(request, 'App/detail_user.html', context )

@login_required(login_url='App:login')
@allowed_users(allowd_roles=['gerant'])
def dalete_user(request ,pk):
    user=User.objects.get(id=pk)
    if user.username == request.user.username :
        messages.error(request,'utilisateur connecté ne peut pas être supprimé')
        return redirect('App:list_user')
    elif(request.method == 'POST'):
        user.delete()
        messages.success(request,' Utilisateur supprimé avec succès')
        return redirect('App:list_user')

    context={
        'user_dalete':user
    }
    return render(request, 'App/dalete_user.html', context )