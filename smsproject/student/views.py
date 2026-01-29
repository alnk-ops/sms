from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Student

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
        stud_object = Student()
        stud_object.full_name = name
        stud_object.username = username
        stud_object.email = email
        stud_object.password = password
        stud_object.college = college
        stud_object.branch = branch
        stud_object.age = age
        stud_object.mobile_number = mobile
        stud_object.save() # Save to database
        return redirect('display')
    return render(request, 'student/register.html')
def about(request):
    return render(request, 'student/about.html')
def display(request):
    stud_object = Student.objects.all()
    return render(request, 'student/display.html', {'students': stud_object})
def update(request, id):
    student = Student.objects.get(id=id) # Fetch the student object by ID
    if request.method == 'POST':
        student.full_name = request.POST.get('name')
        student.username = request.POST.get('username')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.college = request.POST.get('college')
        student.branch = request.POST.get('branch')
        student.age = request.POST.get('age')
        student.mobile_number = request.POST.get('mobile')
        student.save()
        return redirect('display')
    return render(request, 'student/update.html', {'student': student})
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('display')
