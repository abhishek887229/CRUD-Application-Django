from django.shortcuts import render, redirect, HttpResponseRedirect,get_object_or_404
from .forms import UserContact
from .models import User


# Create your views here.
def addnew(request):
    if request.method == 'POST':
        fm = UserContact(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ag = fm.cleaned_data['Age']
            pn = fm.cleaned_data['pincode']
            adds = fm.cleaned_data['Address']
            pne = fm.cleaned_data['phone']

            reg = User(name=nm, email=em, Age=ag, pincode=pn, Address=adds, phone=pne)
            reg.save()
            fm = UserContact()
    else:
        fm = UserContact()

    stud = User.objects.all()
    return render(request, 'enroll/addnew.html', {'form': fm, 'user_s': stud})


# DELETE FUNCTION THAT WILL DELETE DATA
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# UPDATE AND EDIT FUNCTION
# def addupdate(request, id):
#     if request == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = UserContact(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = UserContact(instance=pi)
#
#     return render(request, 'enroll/updatenew.html',{'form': fm})
def addupdate(request, id):
    # Get the user object to update, or 404 if not found
    user_instance = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        # If the request method is POST, process the form data and update the user
        fm = UserContact(request.POST, instance=user_instance)
        if fm.is_valid():
            fm.save()
    else:
        # If it's not a POST request, create a form with the existing user data
        fm = UserContact(instance=user_instance)

    return render(request, 'enroll/updatenew.html', {'form': fm})