from django.contrib import admin
from invitation import models
# Register your models here.
admin.site.site_header = '请柬制作后台'
admin.site.site_title = '请柬制作'

class Tempadmin(admin.ModelAdmin):
    list_display = ('title','style','date_tm','price','use')
admin.site.register(models.Temps,Tempadmin)

class Stylesadmin(admin.ModelAdmin):
    list_display = ('style',)
admin.site.register(models.Styles,Stylesadmin)

admin.site.register(models.User_profile)
class Hoteladmin(admin.ModelAdmin):
    list_display = ('man_name', 'wman_name','marry_tm','hotel_name','phone','data_time')
admin.site.register(models.Hotelmessages,Hoteladmin)