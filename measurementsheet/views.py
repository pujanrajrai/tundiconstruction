import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from connections import sql_connection_insert, sql_connection_fetch
from googleapiclient.discovery import build
from google.oauth2 import service_account


@staff_member_required()
def project_list(request):
    context = {}
    if request.method == 'GET':
        query_set = f"select t_dsca,t_cprj from ttppdm6001111;"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    return render(request, 'measurement_sheet/project_details.html', context)


def ra_bills(request, project):
    context = {}
    if request.method == 'GET':
        query_set = f"select t_rabl, t_dsca,t_stdt,t_crdt,t_stat from ttpptc9301111 where t_cprj='{project}';"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    context['project_name'] = project
    return render(request, 'measurement_sheet/ra_bills.html', context)


def plans(request, project, rabill,rabill_date):
    context = {}
    if request.method == 'GET':
        query_set = f"select t_cpla, t_desc from ttppss0101111 where  t_cprj='{project}';"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    context['project_name'] = project
    context['rabill'] = rabill
    context['rabill_date']=rabill_date
    return render(request, 'measurement_sheet/plan.html', context)


def activity(request, project, rabill,rabill_date, plan):
    context = {}
    if request.method == 'GET':
        query_set = f"select t_cact, t_desc,t_seak,t_cuni from ttppss2001111 where t_cprj='{project}' and t_cpla='{plan}';"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    context['project_name'] = project
    context['rabill'] = rabill
    context['plan'] = plan
    context['rabill_date'] = rabill_date
    return render(request, 'measurement_sheet/activity.html', context)


def boq(request, project, rabill,rabill_date, plan, activity):
    context = {}
    if request.method == 'GET':
        query_set = f"select t_bact from ttppss9401111 where t_cact='{activity}' and t_cprj='{project}' and t_cpla='{plan}';"
        tables = sql_connection_fetch(query_set)
        print(tables)
    context['tables'] = tables
    context['project_name'] = project
    context['rabill'] = rabill
    context['plan'] = plan
    context['activity'] = activity
    context['rabill_date'] = rabill_date
    return render(request, 'measurement_sheet/boq.html', context)


@staff_member_required()
def sheet(request, boq, activity, plan, project, rabill,rabill_date):
    SERVICE_ACCOUNT_FILE = '/Users/tundi/tundiconstruction/Home/tundi-326306-f1a0d57a21e6.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1dgCnjuQXb_AuOU7_kxTIPow31jw8DeSjgbqUfdvsx8o'
    service = build('sheets', 'v4', credentials=credentials)
    SAMPLE_RANGE_NAME = 'project!A:Q'

    # Call the Sheets API
    sheet = service.spreadsheets()
    if request.method == 'POST':
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    majorDimension='ROWS',
                                    range=SAMPLE_RANGE_NAME).execute()
        data = result['values']
        for i in range(1, len(data)):

            if data[i] and data[i][0] != '':
                try:
                    seqno = float(data[i][0])
                except:
                    seqno = ''
                if data[i][0] != '' and type(seqno) == type(1.0):
                    try:
                        if data[i][1] == '':
                            data[i][1] = ' '
                    except:
                        data[i].append(' ')
                    try:
                        try:
                            float(data[i][2])
                        except:
                            data[i][2] = 0
                        if data[i][2] == '':
                            data[i][2] = 0
                    except:
                        data[i].append(0)

                    try:
                        try:
                            float(data[i][3])
                        except:
                            data[i][3] = 0
                        if data[i][3] == '':
                            data[i][3] = 0
                    except:
                        data[i].append(0)

                    try:
                        try:
                            float(data[i][4])
                        except:
                            data[i][4] = 0
                        if data[i][4] == '':
                            data[i][4] = 0
                    except:
                        data[i].append(0)

                    try:
                        try:
                            float(data[i][5])
                        except:
                            data[i][5] = 0
                        if data[i][5] == '':
                            data[i][5] = 0
                    except:
                        data[i].append(0)

                    try:
                        try:
                            float(data[i][6])
                        except:
                            data[i][6] = 0
                        if data[i][6] == '':
                            data[i][6] = 0
                    except:
                        data[i].append(0)

                    query_set=f"""
                    begin tran
                        if exists (select * from ttpptc9511111 with (updlock,serializable)
                        where t_seqn={data[i][0]} and t_cprj='{project}' and t_rabl={rabill} and t_cpla='{plan}' and t_cact='{activity}' and t_seqn='{data[i][0]}' )
                            begin
                                UPDATE ttpptc9511111 SET t_dsca='{data[i][1]}',
                                t_quan={float(data[i][6])}  WHERE t_seqn={data[i][0]} AND
                                t_cact='{activity}' AND t_cpla= '{plan}'
                                AND t_cprj= '{project}' AND t_rabl= '{rabill}';
                            end
                        else
                            begin
                                INSERT INTO ttpptc9511111 (
                                    t_cprj, t_rabl, t_cpla,
                                    t_cact, t_date, t_seqn,
                                    t_dsca, t_fdsc, t_nums,
                                    t_leng, t_brea, t_dpth, t_quan,
                                    t_rmrk, t_logn, t_ldat,
                                    t_text, t_to, t_Refcntd, t_Refcntu)
                                VALUES('{project}',	'{rabill}','{plan}',
                                '{activity}','{rabill_date}','{data[i][0]}',
                                '{data[i][1]}','0',	'{data[i][2]}',	
                                '{data[i][3]}',	'{data[i][4]}',	'{data[i][5]}',	'{data[i][6]}',
                                ' ','{request.user}','{rabill_date}','0','','0','0');
                            end
                    commit tran"""

                print(query_set)
                table = sql_connection_insert(query_set)

    context = {"boq": boq, "activity": activity, "plan": plan, "project": project, "rabill": rabill,"rabill_date":rabill_date}
    # print(context)
    query_set = f"SELECT t_seqn,t_dsca,t_nums,t_leng,t_brea,t_dpth,t_quan FROM ttpptc9511111 " \
                f"where t_cprj='{project}' and t_rabl={rabill} and t_cpla='{plan}' and t_cact='{activity}'"

    tables = sql_connection_fetch(query_set)
    rangeAll = '{0}!A1:Z'.format('project')
    body = {}
    service.spreadsheets().values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rangeAll,
                                          body=body).execute()

    sheet_data = [[
        'SNO',
        'Description',
        'NO.(B)',
        'Length',
        'Breadth',
        'Depth',
        'Quantity',
    ]]
    for table in tables:
        sheet_data.append(list(table))
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED",
                          body={"values": sheet_data}).execute()
    return render(request, 'measurement_sheet/measurement_sheet.html', context)
