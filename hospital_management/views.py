from django.shortcuts import render   # render() is a django shortcut that loads an html template and returns it as a response ...without render() Django woudnot know how to display html page

def home(request):   #This creates a function named home...Every django view recieves a request object
    return render(request,"home.html")  #this means- take the incoming request, find home.html , Return it to browser 