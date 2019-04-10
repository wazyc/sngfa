# from django.shortcuts import render
# from django.http import HttpResponse

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
        cursor.execute("SELECT ope_date,ope_time,ope_state,ope_machine FROM kadoumap_OpeData")
        row = cursor.fetchone()
        print('◆　１　◆◆◆◆◆◆◆◆◆◆◆◆◆')
        print(row)
        print(type(row))
        print('◆　２　◆◆◆◆◆◆◆◆◆◆◆◆◆')
        return HttpResponse(row)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
