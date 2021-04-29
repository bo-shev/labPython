from django.contrib import admin

from .models import link, user_link, Article,Comment

#admin.site.register()

class view(admin.ModelAdmin):
    list_display = ('link_name', 'link_views')



admin.site.register(link, view)

admin.site.register(user_link, view)


admin.site.register(Article)

admin.site.register(Comment)