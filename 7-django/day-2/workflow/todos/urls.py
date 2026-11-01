from django.urls import path
from . import views

app_name='todos'
urlpatterns=[
    path('',views.hello_world,name='helloworld'),#default endpoint
    path('helloagain/',views.another_view,name='another view'),#another endpoint
    #rendering html views
    path('home/',views.html_view,name='htmlview'),
    path('urlparam/<str:name>',views.urlparam1,name='urlparam1'),
    path('addparam/<int:num1>/<int:num2>',views.sum,name='addmultipleparams'),
    path('queryparam',views.queryparam,name='queryparam1'),
    path('product/<int:id>/<slug:slug>',views.product_details,name="mulitparam"),
    path('redirect-to-google',views.google,name='redirectview'),
    path('redirect-to-home',views.redirect1,name='redirectdemo'),
    #post data
    path('submituserdata',views.submit_user_details,name='submituserinfo'),
    path('userdata',views.user_details,name='postuserdetails'),
    
    #django form

    path('djangoform',views.submit_django_form,name='djnagoformdemo'),

    #django templates
    path('templateview',views.template_view1,name="tempview1"),

    #django model
    path('todos',views.todos_view,name='todoviews'),
   # path('delete_todos/<int:todo_id>',views.delete_todo,name='delete_todos'),
   # path('toggle_todos/<int:todo_id>',views.toggle_todo_done,name='toggle_todos'),
    #find person details based on person id
    path('person/<int:person_id>',views.person_details,name='persondetails'),
    
]