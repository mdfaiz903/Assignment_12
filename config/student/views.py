from django.shortcuts import render
from . forms import UserInformationForm
# Create your views here.
def userinfo(request):
    if request.method=='POST':

        form = UserInformationForm(request.POST)
        if form.is_valid():
            print('if block excuted')
            print("first_name : ",form.cleaned_data['first_name'])
            print("last_name : ",form.cleaned_data['last_name'])
            print("email : ",form.cleaned_data['email'])
            print("birth_date : ",form.cleaned_data['birth_date'])
            print("roll_no : ",form.cleaned_data['roll_no'])
            print("phone : ",form.cleaned_data['phone'])
            print("is_current_student : ",form.cleaned_data['is_current_student'])
            print("created_date : ",form.cleaned_data['created_date'])
            print("content : ",form.cleaned_data['content'])
            print("file : ",form.cleaned_data['file'])
    else:
        form = UserInformationForm()
        print("else block excuted")
    return render(request,'student/form.html',{'form':form})