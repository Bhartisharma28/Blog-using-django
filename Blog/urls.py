from django.urls import path
from . import views
urlpatterns=[
path('home/',views.Home,name='home'),
path('blogs/',views.blogs,name='blogs'),
path('contact/',views.contact_page,name='contact'),
path('blogs/<int:Blog_id>/', views.detail,name='detail')

]
