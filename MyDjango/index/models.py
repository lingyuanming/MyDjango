from django.db import models

# Create your models here.
# class Product(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     type = models.CharField(max_length=20)
# #创建产品分类表
class Type(models.Model):


    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)
class Product(models.Model):


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20,default="191g")
    size = models.CharField(max_length=20,default="161mm*76mm")
    type = models.ForeignKey(Type,on_delete=models.CASCADE)


class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)


class Performer_info(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.OneToOneField(Performer,on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)


class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    #performer = models.ForeignKey(Performer,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)


class Province(models.Model):
    name = models.CharField(max_length=10)


class City(models.Model):
    name = models.CharField(max_length=5)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=10)
    living = models.ForeignKey(City,on_delete=models.CASCADE)





 


