from django.shortcuts import render

# Create your views her

def getin( request):
    return render( request , 'Sign/res.html')


def sign_in(request):
    return render(request , 'Sign/sign_in.html')


def sign_up(request):
    return render(request , 'Sign/sign_up.html')


def forget_pass(request):
    return render( request , 'Sign/forget_pass.html')
