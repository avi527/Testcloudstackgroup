from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import UserSignup
import hashlib 
# Create your views here.
def signup(request):
	msg=""
	if request.method=='POST':
		f_name=request.POST['fname']
		l_name=request.POST['lname']
		profile_pic=request.FILES['photo']
		email_id=request.POST['email']
		first_pass=request.POST['fpass']
		confrm_pass=request.POST['spass']
		if first_pass == confrm_pass:
			try:
				result = hashlib.md5(first_pass.encode()) 
				saveInDb=UserSignup(First_Name=f_name,Last_Name=l_name,Email=email_id,Password=result.hexdigest(),Profile_Image=profile_pic)
				saveInDb.save()
				return redirect('signup')
			except:
				msg="user already register !!!"
		else:
			msg="password not match"

	return render(request,'signup.html',{"msg":msg})
def login(request):
	msg=""
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		result_pass = hashlib.md5(password.encode() ) 
		try:
			userValidate=UserSignup.objects.filter(Email=email).values('Email','Password')
			if userValidate[0]['Email'] == email and userValidate[0]['Password'] == result_pass.hexdigest():
				request.session['username']= userValidate[0]['Email']
				return redirect('profile')
		except:
			msg="Somthing went wrong please check it"

	return render(request,'login.html',{"msg":msg})
def profile(request):
	try:
		if request.session['username'] is not None:
			session_id=request.session['username']
			retriveRecord=UserSignup.objects.filter(Email=session_id)
		#return render(request,'profile.html',{'session_id':session_id,"retriveRecord":retriveRecord})
	except:
		return redirect("login")
	return render(request,'profile.html',{'session_id':session_id,"retriveRecord":retriveRecord})
def logout(request):
	del request.session['username']
	return redirect("login")