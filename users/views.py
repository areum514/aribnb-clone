from django.views import View
from django.shortcuts import render
from . import forms
class LoginView(View):

    def get(self,request):
        form = forms.LoginForm()
        return render(request,"users/login.html",{"form":form})

    def post(self,request):
        form=forms.LoginForm(request.POST)
        print(form)


""" 
두개 같은거임
class LoginView(View):

    def get(self,request):
        pass
    def post(self,request):
        pass


def login_view(request):
    if request.method=="GET"
        pass
    elif request.method="POST"
        pass """