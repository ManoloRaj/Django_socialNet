from django.shortcuts import render,redirect
from .models import user
from .forms import userForm, connexionForm
from django.contrib import messages


# Create your views here.

def inscription(request):
    if request.method == "POST":
        user_form = userForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Successfull'))

        else :
            messages.error(request, 'Error saving')

        return redirect('/auth/connexion/')

    user_form = userForm()
    #User = user.object.all()


    return render(request, 'inscription.html', context ={'user_form' : user_form})

def connexion(request):
    if request.method == "POST":
        connexion_form = connexionForm(request.POST)

        if connexion_form.is_valid():
            temp_user_name = request.POST.get('user_name')
            temp_user_password = request.POST.get('password')
            
            User = user.objects.all()
            for ur in User :
                if temp_user_name == ur.user_name and temp_user_password == ur.password :
                    request.session['id_user'] = ur.id
                    return redirect('/auth/acceuil_membre/')
                else :
                    pass

    connexion_form = connexionForm()
    return render(request, 'connexion.html', context = {'connexion_form' : connexion_form})

def acceuil_membre(request):
    id  = request.session['id_user']
    User = user.objects.filter(id = id)
    desc = User[0].description

    return render(request, 'acceuil_membre.html', context = { 'description': desc})