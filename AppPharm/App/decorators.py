from django.shortcuts import redirect
from django.contrib import messages

def unauthenticate_user (view_func):
    def wrapper_func(request , *args , **kwargs):
        if (request.user.is_authenticated):
            return redirect('App:ventes')
        else:
            return view_func(request , *args , **kwargs)
    return wrapper_func



def allowed_users(allowd_roles=[]):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowd_roles :
                return view_func(request , *args , **kwargs)
            else:
                messages.error(request ,"utilisateur n'a pas la permissionss")
                return redirect('App:ventes')
        return wrapper_func
    return decorator 