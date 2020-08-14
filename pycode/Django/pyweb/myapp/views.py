from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def hello(request):
    return HttpResponse('hello world')


def index(request):
    user_index = models.User.objects.all()
    obj = models.User.objects.filter(mid=request.GET.get('mid', ''))
    obj2 = models.User.objects.filter(level=request.GET.get('level', ''))
    context = {
        'user_index': user_index,

    }
    if request.GET.get('mid', ''):
        context = {
            'user_index': obj
        }
        return render(request, 'index.html', context)
    if request.GET.get('level', ''):
        context = {
            'user_index': obj2
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)


@csrf_exempt
def add_data(request):
    data = dict(request.POST)
    if data['mid'] and data['name']:
        obj = models.User(mid=data['mid'][0], name=data['name'][0],
                          sign=data['sign'][0], level=data['level'][0])
        obj.save()
        return HttpResponse('添加成功！')
    else:
        return HttpResponse('添加失败！')
