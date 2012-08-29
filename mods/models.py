#coding: utf-8
from django.db import models


























#附件
class attach(models.Model):
    file_name = models.CharField(max_length=100)            #文件名
    file_type = models.CharField(max_length=128)            #文件类型
    file_path = models.CharField(max_length=100)            #文件路径
    upload_date = models.DateTimeField(auto_now=True)       #上传时间
    
    class Meta:
        #自定义表名   
        db_table = 'attach'