from django.http import JsonResponse
from django.shortcuts import render
from connections import sql_connection


# Create your views here.
def tender_reports(request):
    context = {}
    if request.method == 'GET':
        query_set = f"SELECT t_trno,t_tnam,t_tdat,t_bpid,t_potr FROM ttpztr0011111"
        tables = sql_connection(query_set)

    if request.method == "POST":
        from_date = request.POST.get('form_date')
        to_date = request.POST.get('to_date')
        query_set = f"SELECT t_trno,t_tnam,t_tdat,t_bpid,t_potr FROM ttpztr0011111 where t_tdat>='{from_date}' AND t_tdat<= '{to_date}'"
        tables = sql_connection(query_set)
        context['from_date'] = from_date
        context['to_date'] = to_date
    context['tables'] = tables
    return render(request, 'project/tender_details.html', context)


def tender_details_reports(request, str):
    if request.method == 'GET':
        context = {}
        trno = str
        query_set = f"SELECT t_desc,t_sdat,t_edat,t_cprj,t_ttyp,t_docn,t_btno,t_stat FROM ttdztc9001111 where t_opty = '{trno}'"
        table = sql_connection(query_set)
        context['tables'] = table
        context['tender_no'] = trno

        return render(request, 'project/tender_report_details.html', context)
