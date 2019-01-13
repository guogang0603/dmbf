# Generated by Django 2.1.4 on 2019-01-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotelmessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='新郎姓名')),
                ('wman_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='新娘姓名')),
                ('marry_tm', models.CharField(blank=True, max_length=64, null=True, verbose_name='婚礼日期')),
                ('hotel_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='酒店名称')),
                ('hotel_map', models.CharField(blank=True, max_length=128, null=True, verbose_name='酒店地址')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='联系电话')),
                ('link', models.CharField(blank=True, max_length=64, null=True, verbose_name='生成链接')),
                ('data_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '酒店信息',
            },
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=128, unique=True, verbose_name='风格名称')),
            ],
            options={
                'verbose_name_plural': '风格',
            },
        ),
        migrations.CreateModel(
            name='Temps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('price', models.FloatField(max_length=10, verbose_name='价格')),
                ('price_old', models.FloatField(max_length=10, verbose_name='原价')),
                ('date_tm', models.DateTimeField(verbose_name='时间')),
                ('edit_url', models.CharField(max_length=128, verbose_name='编辑模板')),
                ('view_url', models.CharField(max_length=128, verbose_name='预览模板')),
                ('use', models.IntegerField(verbose_name='使用次数')),
                ('style', models.ForeignKey(on_delete=False, to='invitation.Styles', verbose_name='风格')),
            ],
            options={
                'verbose_name_plural': '模板',
            },
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.IntegerField(blank=True, choices=[(0, '未关注公众号'), (1, '已关注公众号')], default=0, null=True)),
                ('openid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=64, null=True, verbose_name='昵称')),
                ('headimg', models.CharField(blank=True, max_length=640, null=True, verbose_name='头像路径')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=34, verbose_name='性别')),
                ('province', models.CharField(blank=True, max_length=64, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='城市')),
                ('country', models.CharField(blank=True, max_length=64, null=True, verbose_name='国家')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('use', models.IntegerField(verbose_name='使用次数')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='hotelmessages',
            name='use_content',
            field=models.ForeignKey(on_delete=False, to='invitation.User_profile', verbose_name='用户连接'),
        ),
    ]