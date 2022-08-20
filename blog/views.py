from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Posts




def index(request):
    post_list = Posts.objects.all().values().order_by('-id')
    
    paginator = Paginator(post_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    template = loader.get_template('blog_index.html')
    context = {
    'post_list': page_obj,
    'page_obj': page_obj,
    }
    return HttpResponse(template.render(context, request))
    
def bog_details(request,id):
    post_list = Posts.objects.get(id=id)
    template = loader.get_template('blog_details.html')
    context = {
    'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))
    
   
