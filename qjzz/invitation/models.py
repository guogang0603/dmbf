from django.db import models
import datetime
# Create your models here.
class Temps(models.Model):
    title = models.CharField(max_length=128,verbose_name='标题')
    style = models.ForeignKey('Styles', verbose_name='风格',on_delete=False)
    price = models.FloatField(max_length=10,verbose_name='价格')
    price_old = models.FloatField(max_length=10,verbose_name='原价')
    date_tm = models.DateTimeField(verbose_name='时间')
    edit_url = models.CharField(max_length=128,verbose_name='编辑模板')
    view_url = models.CharField(max_length=128,verbose_name='预览模板')
    use = models.IntegerField(verbose_name='使用次数')
    class Meta:
        verbose_name_plural = '模板' #显示表名Temps，把Temps改成模板
    def __str__(self):
        return self.title

class Styles(models.Model):
    style = models.CharField(max_length=128,verbose_name='风格名称',unique=True) #名称唯一

    class Meta:
        verbose_name_plural = '风格'
    def __str__(self):
        return self.style

#TODO:用户信息
class User_profile(models.Model):
     subscribe_choices=(
          (0,'未关注公众号'),
          (1,'已关注公众号'),
     )
     subscribe=models.IntegerField(choices=subscribe_choices,blank=True,null=True,default=0)

     openid=models.CharField(unique=True,max_length=100,blank=True,null=True,)
     nickname=models.CharField(max_length=64,verbose_name='昵称',blank=True,null=True,)
     headimg = models.CharField(max_length=640, verbose_name='头像路径',blank=True,null=True,)
     sex_choices=(
          ('1', '男'),
          ('2', '女')
     )
     sex=models.CharField(choices=sex_choices,max_length=34,verbose_name='性别')
     province=models.CharField(max_length=64,blank=True,null=True,verbose_name='省份')
     city=models.CharField(max_length=64,verbose_name='城市',blank=True,null=True,)
     country=models.CharField(max_length=64,verbose_name='国家',blank=True,null=True,)
     phone=models.CharField(max_length=11,verbose_name='手机号',blank=True,null=True)
     use = models.IntegerField(verbose_name='使用次数')
     update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

     def __str__(self):
          return self.nickname
     class Meta:
          verbose_name_plural='用户信息'

#TODO:酒店信息
class Hotelmessages(models.Model):
    man_name = models.CharField(max_length=64, verbose_name='新郎姓名', blank=True,null=True)
    wman_name = models.CharField(max_length=64, verbose_name='新娘姓名', blank=True,null=True)
    marry_tm = models.CharField(max_length=64,verbose_name='婚礼日期', blank=True,null=True)
    hotel_name = models.CharField(max_length=64, verbose_name='酒店名称', blank=True,null=True)
    hotel_map = models.CharField(max_length=128, verbose_name='酒店地址', blank=True,null=True)
    phone = models.CharField(max_length=11,verbose_name='联系电话', blank=True,null=True)
    link = models.CharField(max_length=64,verbose_name='生成链接', blank=True,null=True)
    data_time = models.DateTimeField(verbose_name='创建时间',auto_now=True)
    use_content = models.ForeignKey('User_profile', on_delete=False, verbose_name='用户连接')
    def __str__(self):
        return self.man_name
    class Meta:
        verbose_name_plural = '酒店信息'

#TODO:模板上传图片

