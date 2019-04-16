from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import OpeData


# Create your views here.

def alldata(request):
    print('views.all===============================')
    all_opedata_list = OpeData.objects.all().order_by('ope_datetime')
    print(type(all_opedata_list))
    print(all_opedata_list)
    # template = loader.get_template('kadoumap/alldata.html')
    context = {'all_opedata_list': all_opedata_list, }
    # return HttpResponse(template.render(context, request))
    return render(request, 'kadoumap/alldata.html', context)


def detail(request, machine):
    print('views.detail===============================' + machine)
    machine_opedata_list = get_list_or_404(OpeData, ope_machine=machine)
    print(type(machine_opedata_list))
    print(machine_opedata_list)
    return render(request, 'kadoumap/detail.html', {'machine_opedata_list': machine_opedata_list})


def map(request):
    print('views.map===============================')
    from django.db import connection
    with connection.cursor() as c:
        c.execute('''
            SELECT main.ope_datetime,main.ope_machine,sub.ope_state
            FROM 
            (SELECT MAX(ope_datetime) AS ope_datetime , ope_machine
            FROM kadoumap_OpeData
            GROUP BY ope_machine) AS main
            LEFT JOIN kadoumap_OpeData AS sub
            ON main.ope_datetime = sub.ope_datetime
            AND main.ope_machine = sub.ope_machine 
            ORDER BY main.ope_machine ASC 
            ''')
        # c.execute('''
        #     SELECT ope_datetime , ope_state , ope_machine
        #     FROM kadoumap_OpeData
        #     ORDER BY ope_datetime DESC
        #     LIMIT 1
        #     ''')
        opedata_list = c.fetchall()
    print(type(opedata_list))
    print(opedata_list)
    context = {'opedata_list': opedata_list}
    return render(request, 'kadoumap/map.html', {'opedata_list': opedata_list})
