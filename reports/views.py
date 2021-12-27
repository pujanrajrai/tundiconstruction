from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, HttpResponse

# Create your views here.
from connections import sql_connection_fetch


@staff_member_required()
def reports(request):
    context = {}

    if request.method == 'GET':
        print(request.GET)
        query_set = f"select * from ttpppc4001111;"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    context['btn_click'] = request.GET.get('btn_click')
    if request.GET.get('btn_click') == 'incl':
        return render(request, 'reports/cumulutive_incl_comm.html', context)
    elif request.GET.get('btn_click') == 'excl':
        return render(request, 'reports/cumulutive_excl_comm.html', context)
    elif request.GET.get('btn_click') == 'period':
        return render(request, 'reports/period.html', context)
    elif request.GET.get('btn_click') == 'forecast':
        return render(request, 'reports/forecast.html', context)
    else:
        return render(request, 'reports/cumulutive_incl_comm.html', context)
