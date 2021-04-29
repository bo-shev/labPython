from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import link, Article, user_link

def index(request):
    all_links = link.objects.all()
    all_user_links = user_link.objects.all()
    return render(request, 'lab/list.html', {'all_links': all_links, 'all_user_links':all_user_links})

def add_user_link(request):
    user_links = user_link.objects.all()
    return render(request, 'lab/add-user-link.html', {'user_links': user_links})

def allarticles(request):
    all_articles = Article.objects.all()
    return render(request, 'lab/articles.html', {'all_articles': all_articles})

def detale(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("page not found")
    comm = a.comment_set.order_by('id')
    return render(request, 'lab/detale.html', {'article': a, 'comments': comm})



def addview(request, link_id):
    curr_link = link.objects.get(id = link_id)
    curr_link.link_views = curr_link.link_views + 1;
    curr_link.save()

    return render(request, 'lab/addview.html', {'curr_link': curr_link})
def adduserview(request, user_link_id):
    curr_link = user_link.objects.get(id = user_link_id)
    curr_link.link_views = curr_link.link_views + 1;
    curr_link.save()

    return render(request, 'lab/addview.html', {'curr_link': curr_link})

def leve_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("page not found")

    a.comment_set.create(author_name= request.POST['name'], comment_text= request.POST['text'])

    return HttpResponseRedirect(reverse('lab:detale', args = (a.id,)))

def add_new_user_link(request):
    u = user_link(link_author= request.POST['author'], link_name=request.POST['name'], link_url=request.POST['url'], link_views=0)
    u.save()

    user_links = user_link.objects.all()
    return render(request, 'lab/add-user-link.html', {'user_links': user_links})
