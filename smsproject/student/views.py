from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'student/index.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        college = request.POST.get('college')
        branch = request.POST.get('branch')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        address = request.POST.get('address')

        context = {
            'name': name,
            'username': username,
            'email': email,
            'password': password,
            'college': college,
            'branch': branch,
            'age': age,
            'mobile': mobile,
            'gender': gender,
            'course': course,
            'address': address,
        }
        # Here, you would typically save the data to the database
        return render(request, 'student/display.html',context)
    return render(request, 'student/register.html')
def about(request):
    return render(request, 'student/about.html')
def display(request):
    return render(request, 'student/display.html')
