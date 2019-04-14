from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import OpeData

# Create your views here.
# def index(request):
#     return HttpResponse("ThisIs'kadoumap/views.index'")
#
#
# def detail(request, opedata_id):
#     return HttpResponse("ThisIs'kadoumap/views.detail' %s." % opedata_id)
#
#
# def results(request, opedata_id):
#     response = "ThisIs'kadoumap/views.result' %s."
#     return HttpResponse(response % opedata_id)
#
#
# def vote(request, opedata_id):
#     return HttpResponse("ThisIs'kadoumap/views.vote' %s." % opedata_id)

from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import TemplateView
from django.http import HttpResponse


# from info.models import *


# Create your views here.
# class InfoListView(TemplateView):
#     template_name = "kadoumap/list.html"
#
#     def get(self, request, *arg, **kwargs):
#         context = super(InfoListView, self).get_context_data(**kwargs)
#         info_list = Info.objects.all().order_by("released").reverse()
#         context['info_list'] = info_list
#         return render(self.request, self.template_name, context)


def index(request):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT ope_datetime,ope_state,ope_machine FROM kadoumap_OpeData")
        row = cursor.fetchall()
        print('◆　１　◆◆◆◆◆◆◆◆◆◆◆◆◆')
        print(type(row))
        hoge = 'DBから取得<br>'
        for datalist in row:
            print('------')
            for datatuple in datalist:
                print(datatuple)
                hoge = hoge + datatuple + '　　'
            hoge = hoge + '<br>'
        return HttpResponse(hoge)


def all(request):
    print('views.all===============================')
    all_opedata_list = OpeData.objects.all().order_by('ope_datetime')
    print(all_opedata_list)
    # template = loader.get_template('kadoumap/all.html')
    context = {'all_opedata_list': all_opedata_list, }
    # return HttpResponse(template.render(context, request))
    return render(request, 'kadoumap/all.html', context)


def detail(request, machine):
    print('views.detail===============================' + machine)
    machine_opedata_list = get_list_or_404(OpeData, ope_machine=machine)
    return render(request, 'kadoumap/detail.html', {'machine_opedata_list': machine_opedata_list})


