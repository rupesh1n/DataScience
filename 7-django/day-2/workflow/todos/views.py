from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import UserForm,TodoForm
from .models import ToDo,Person

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello Django!")

def another_view(request): #mysite.com/helloagain
    return HttpResponse("how are you doing?")

def html_view(request):
    return render(request,'todos/home.html')

#URL parameter
def urlparam1(request,name):
    return HttpResponse(f'welcome {name}!')

def sum(request,num1,num2):
    return HttpResponse(f'result is{num1+num2}')

#query parameter

def queryparam(request):
    return HttpResponse(f'your email is {request.GET.get("email")}')

#multiparams
def product_details(request,id,slug):
    return HttpResponse(f"prduct details:{id},{slug}")

def google(request):
    return redirect("todos:htmlview")

#redirecting
def redirect1(request):
    return redirect('home/')

#POST data
def user_details(request):
    if request.method=='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        return HttpResponse(f'you posted{name},{email},{age}')
    else:
        return HttpResponseNotAllowed(['POST'])

def submit_user_details(request):
    return render(request,'todos/userform.html')
    

#POST data using Django form
def user_details1(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']
          
        
            return HttpResponse(f'you posted- {name},{email},{age}')
    else:
        return HttpResponseNotAllowed(['POST'])

def submit_django_form(request):
    form=UserForm()
    return render(request,'todos/user_django_form.html',{'form':form})

#django templates

def template_view1(request):
    
    skillsets = ['c', 'c++', 'python', 'linux']
    skillsets_lower = [s.lower() for s in skillsets]

    context = {
        "name": "vikas",
        "age": 45,
        "skillsets": skillsets,
        "has_many_skills": len(skillsets) > 3,
        "knows_python": "python" in skillsets_lower,
    }

    return render(request,'todos/template_demo.html',context)

#create todos
def todos_view(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save()#create database instnace
            return HttpResponse("Todo successfully created")

    else: 
        form=TodoForm()
        todos=ToDo.objects.all()#reurn all the rows from the table

        return render(request,'todos/todos.html',{'form':form,'todos':todos})
    
#filter person data based on id
def person_details(request,person_id):
    person=Person.objects.filter(id==person_id).first()
    return render('todos/person_details.html',{'person':person})

def delete_todo(request,todo_id):
    todo=ToDo.objects.filter(id==todo_id).first()
    todo.delete()
    return HttpResponse('todo successfully deleted...')

def toggle_todo_done(request,todo_id):
    todo=ToDo.objects.filter(id==todo_id).first()
    todo.done=not todo.done
    todo.save()