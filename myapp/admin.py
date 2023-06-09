from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import About, Teachers,News,Gallary
admin.site.unregister(Group)
admin.site.unregister(User)




class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','text','email','created_at','updated_at']
    list_editable = ['email']
    list_per_page = 10
    search_fields = ['fulname']
admin.site.register(About,AboutAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','subject','title','email','phone','telegram_link','instagram_link','facebook_link','created_at','updated_at']
    list_editable = ['subject']
    list_per_page = 10
    search_fields = ['first_name','last_name']
admin.site.register(Teachers,TeacherAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','text','date','created_at','updated_at']
    list_per_page = 10
    search_fields = ['title']
admin.site.register(News,NewsAdmin)


class GallaryAdmin(admin.ModelAdmin):
    list_display = ['title','date','maktab','dars','bayram','created_at','updated_at']
    list_per_page = 10
    search_fields = ['title']
admin.site.register(Gallary,GallaryAdmin)