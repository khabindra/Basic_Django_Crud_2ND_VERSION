from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from .models import Registration
from django.contrib import messages 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.
def Home(request):
    return render(request,'home.html')
def Form(request):
    return render(request,'form.html')
def Register(request):
    if request.method == 'POST':
        N = request.POST['name']
        E = request.POST['email']
        P = request.POST['password']
        data = Registration(name=N,email=E,password=P)
        data.save()
        messages.success(request,'Your successfully posted data is here in the show_data page down below  !!!')
        return redirect('showdata')
    return render(request,'registration.html')

def show_data(request):
    data = Registration.objects.all()
    context = {
        'details':data,
    }
    return render(request,'show_data.html',context)

def delete_data(request,pk):
    data = Registration.objects.get(id=pk)
    data.delete()
    return redirect('showdata')


class edit_data(UpdateView):
    model = Registration
    fields = ['name','email','password']
    template_name = 'edit.html'
    success_url = reverse_lazy('showdata')
