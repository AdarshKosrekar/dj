from django.shortcuts import render
from .forms import EmployeeForm
#from myapp.forms import StudentForm
from django.http import HttpResponse
from myapp.functions.functions import handle_uploaded_file

'''def index(request):
	student=StudentForm()
	return render(request,"index.html",{'form':student})'''

'''def index(request):
	if request.method=='POST':
		student=StudentForm(request.POST,request.FILES)
	if student.is_valid():
		handle_uploaded_file(request.FILES['file'])
		return HttpResponse("File uploaded successfully")
	else:
		student=StudentForm()
		return render(request,"index.html",{'form':student})'''
def emp(request):
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			try:
				return redirect('/')
			except:
				pass
	else:
		form=EmployeeForm()
	return render(request,'index.html',{'form':form})
