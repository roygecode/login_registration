from django.shortcuts import render, HttpResponse, redirect
import bcrypt

from models import * #REMEMBER THIS

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def login(request):
    try:
        query = User.objects.get(email=request.POST['email'])
        if query:
            if bcrypt.checkpw(request.POST['password'].encode(), query.password.encode()):
                print "The password matches, you may enter"
                return redirect('/')
    except query.DoesNotExist:
        return HttpResponse("Email does not exist")
    return redirect('/')

def register(request):
    try:
        if User.objects.get(email=request.POST['email']):
            return HttpResponse("Email already exists")
    
    except User.DoesNotExist:

        if request.POST["password"] != request.POST["c_password"]:
            return HttpResponse("passwords do not match")
        
        hash1=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1)

        return redirect('/')

