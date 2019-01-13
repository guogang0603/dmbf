from django.urls import path,include
from invitation import views
urlpatterns = [
    path('mess',views.getallmessages),
    path('add_mess',views.add_mess)

]


