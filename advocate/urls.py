from django.urls import path
from .views import adv_login, adv_home,adv_case,contact,todolist,dashbord,ad_upadte_hearing_details,ad_close_case
urlpatterns = [
    path("",adv_login),
    path("home",dashbord,name="adv_dashboard"),
    path("case",adv_case,name="adv_case"),
    path("case/update/hearing/<int:id>",ad_upadte_hearing_details,name="ad_upadte_hearing_details"),
    path("case/close/<int:id>",ad_close_case,name="ad_close_case"),
    path("contact",contact,name="adv_contact"),
    path("todolist",todolist,name="adv_todo"),

]
