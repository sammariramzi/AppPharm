from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dci)
admin.site.register(Laboratoire)
admin.site.register(Classe_thérapeutique)
admin.site.register(Sous_classe)
admin.site.register(Product)
admin.site.register(Pharmaci)
admin.site.register(Echange)
admin.site.register(Vente)
admin.site.register(Product_edit)
admin.site.register(Product_added)
admin.site.register(Echange_added)
admin.site.register(Dalete_echange)
admin.site.register(Vente_added)