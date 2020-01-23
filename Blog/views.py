from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import contact,Blogs
# Create your views here.

def Home(request):
    return render(request,'Blog/home.html')

def blogs(request):
    var_1=Blogs.objects.all()
    return render(request,'Blog/blog.html',{'var_1':var_1})

def detail(request,Blog_id):
    detail_page=get_object_or_404(Blogs,pk=Blog_id)
    return render(request,'Blog/detail.html',{'detail':detail_page})

def contact_page(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Subject=request.POST.get('subject')
        Your_Message=request.POST.get('message')

        var_contact=contact(name=Name, email=Email, subject=Subject, message=Your_Message)
        var_contact.save()
        return render(request, 'Blog/thanks.html')
    else:
        return render(request,'Blog/contact.html')
