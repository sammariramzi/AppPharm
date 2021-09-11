from django.urls import path
from .views import *
app_name = 'App'
urlpatterns = [
    path('', login_views , name='login'),
    path('logout/', logout_views , name='logout'),
    path('ventes/', list_vente , name='ventes'), 
    path('add_vente/<str:pk>/', add_vente , name='add_vente'),
    path('historique_vente', historique_vente , name='historique_vente'),
    path('list_product/', list_product , name='list_product'),
    path('add_product/', add_product , name='add_product'), 
    path('edit_product/<str:pk>/', edit_product , name='edit_product'), 
    path('detail_product/<str:pk>/', detail_product , name='detail_product'), 
    path('dalete_product/<str:pk>/', dalete_product , name='dalete_product'), 
    path('add_Dci/', Dci_view.add_Dci , name='add_Dci'), 
    path('add_Labo/', Labo_view.add_Labo , name='add_Labo'),
    path('add_Therapeutique/', Therapeutique_view.add_Therapeutique , name='add_Therapeutique'),
    path('add_Sous_classe/', Sous_classe_view.add_Sous_classe , name='add_Sous_classe'),
    path('dci_list/', Dci_view.as_view(), name="dci_list"), 
    path('labo_list/', Labo_view.as_view(), name="labo_list"),
    path('therapeutique_list/', Therapeutique_view.as_view(), name="therapeutique_list"),
    path('sous_classe_list/', Sous_classe_view.as_view(), name="sous_classe_list"),
    path('list_echange/', list_echange , name='list_echange'),
    path('detail_pharmaci/<str:pk>/', detail_pharmaci , name='detail_pharmaci'),
    path('add_echange/', add_echange , name='add_echange'), 
    path('add_pharmaci/', Pharmaci_view.add_pharmaci , name='add_pharmaci'), 
    path('pharmaci_list/', Pharmaci_view.as_view(), name="pharmaci_list"), 
    path('dalete_echange/<str:pk>/', dalete_echange , name='dalete_echange'),
    path('actions/', actions , name="actions"), 
    path('CreationUser/', CreationUser , name="CreationUser"), 
    path('edit_user/<str:pk>/', edit_user , name="edit_user"), 
    path('list_user/', list_user , name="list_user"), 
    path('detail_user/<str:pk>/', detail_user , name="detail_user"), 
    path('dalete_user/<str:pk>/', dalete_user , name="dalete_user"), 
]


