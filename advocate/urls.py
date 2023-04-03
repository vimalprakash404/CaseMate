from django.urls import path
from .views import login, home,case,contact,todolist
urlpatterns = [
    path("",login),
    path("home",home),
    path("case",case,name="adv_case"),
    path("contact",contact,name="adv_contact"),
    path("todolist",todolist,name="adv_todo")
]
