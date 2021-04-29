from django.urls import path

from . import  views

app_name = 'lab'
urlpatterns = [
    path('', views.index, name = '_index_'),
    path('userlink/', views.add_user_link, name = 'add_user_link'),
    path('userlink/newlink', views.add_new_user_link, name = 'add_new_user_link'),
    path('<int:link_id>/', views.addview, name = 'addview'),
    path('user/<int:user_link_id>/', views.adduserview, name = 'adduserview'),
    path('pages/', views.allarticles, name = 'allarticles'),
    path('pages/<int:article_id>/', views.detale, name = 'detale'),
    path('pages/<int:article_id>/leve_comment', views.leve_comment, name = 'leve_comment')
]