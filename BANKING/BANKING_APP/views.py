from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'sign_up.html')
def about(request):
     return render(request,'about.html')
def login_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('about')
		else:
			return redirect('signup')
	else:
		return redirect('signup')
	

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login')
    else:
        return render(request,'signup_page.html')
def profile(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        dob=request.POST['date']
        age=request.POST['age']
        img=request.FILES.get('img')
        scontact=request.POST['cnumber']
        querys=request.POST['query']
        return render(request,'profile.html',{'name':uname,'email':email,'dob':dob,'age':age,'img':img,'phone':scontact,'query':querys})
    
