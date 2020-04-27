# index的views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product
import csv


# Create your views here.


def index(request):
    # return HttpResponse("Hello world")
    # return render(request,'index.html',context={'title':'首页'},status=500)
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    title = '首页'
    return render(request, 'index.html', context=locals(), status=200)


# views.py 的mydate函数
def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# views.py的myyear函数
def myyear(request, year):
    return render(request, 'myyear.html')


# 参数为字典的URL的视图函数
def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response


def login(request):
    # 相对路径，代表首页地址
    # return redirect('/')
    # 绝对路径，完整的地址信息
    # return redirect('http://127.0.0.1:8000/')
    if request.method == 'POST':
        name = request.GET.get('name')
        #相对路径，代表首页地址
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else :
            name = 'Everyone'
        return HttpResponse('username is '+name)
class ProductList(ListView):
    #context_object_name设置HTML模板的变量名称
    context_object_name = 'type_list'
    #设定HTML
    template_name = 'index.html'
    #查询数据
    queryset = Product.objects.values('type').distinct()

    #重写get_queryset方法,对模型product进行数据筛选
    # def get_queryset(self):
    #     type_list = Product.objects.values('type').distinct()
    #     return type_list
    #添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name','type')
        return context
    def get_queryset(self):
        #获取URL变量的id
        print(self.kwargs['id'])
        #获取URL的参数name
        print(self.kwargs['name'])
        #获取请求方式
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list

