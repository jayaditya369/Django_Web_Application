from django.urls import include, path
from myapp import views
from .views import IndexView, DetailView
app_name = 'myapp'

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'about/', views.about, name='about'),
    path(r'<int:topic_id>', DetailView.as_view(), name='topic detail'),
    path(r'findcourses/', views.findcourses, name='findcourses'),
    path(r'place_order/', views.place_order, name='place_order'),
    path(r'review/', views.review, name='review'),
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'myaccount/', views.my_account, name='my_account'),
    path(r'register/', views.register, name='register'),
    path(r'myorders/', views.myorders, name='myorders'),
    ]
