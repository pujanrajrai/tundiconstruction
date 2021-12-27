from django.contrib import auth
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from connections import sql_connection_insert, sql_connection_fetch
from googleapiclient.discovery import build
from google.oauth2 import service_account


@staff_member_required()
def home(request):
    return render(request, 'home/home.html')


@staff_member_required()
def project_report_details(request, t_bcod, t_cact, t_cpla, t_cprj, t_rabl):
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
                # print(type(seqno),type(1.0))
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
                    try:
                        try:
                            float(data[i][7])
                        except:
                            data[i][7] = 0
                        if data[i][7] == '':
                            data[i][7] = 0
                    except:
                        data[i].append(0)
                    try:
                        try:
                            float(data[i][8])
                        except:
                            data[i][8] = 0
                        if data[i][8] == '':
                            data[i][8] = 0
                    except:
                        data[i].append(0)
                    try:
                        try:
                            float(data[i][9])
                        except:
                            data[i][9] = 0
                        if data[i][9] == '':
                            data[i][9] = 0
                    except:
                        data[i].append(0)
                    try:
                        try:
                            float(data[i][10])
                        except:
                            data[i][10] = 0
                        if data[i][10] == '':
                            data[i][10] = 0
                    except:
                        data[i].append(0)
                    try:
                        try:
                            float(data[i][11])
                        except:
                            data[i][11] = 0
                        if data[i][11] == '':
                            data[i][11] = 0
                    except:
                        data[i].append(0)
                    try:
                        try:
                            float(data[i][12])
                        except:
                            data[i][12] = 0
                        if data[i][12] == '':
                            data[i][12] = 0

                    except:
                        data[i].append(0)
                    # print(data[i][12])
                    # try:
                    #     try:
                    #         float(data[i][13])
                    #     except:
                    #         data[i][13] = 0
                    #     if data[i][13] == '':
                    #         data[i][13] = 0
                    # except:
                    #     data[i].append(0)

                    query_set = f"""begin tran
            if exists (select * from ttpztc1161111 with (updlock,serializable) where t_seqn={data[i][0]} AND t_bcod='{t_bcod}' 
               AND t_cact='{t_cact}' AND t_cpla= '{t_cpla}' 
               AND t_cprj= '{t_cprj}' AND t_rabl= '{t_rabl}')
            begin
               UPDATE ttpztc1161111 SET t_desc='{data[i][1]}', 
               t_col1={float(data[i][2])}, t_col2={float(data[i][3])}, 
               t_col3={float(data[i][4])}, t_col4={float(data[i][5])}, 
               t_col5={float(data[i][6])}, t_col6={float(data[i][7])}, 
               t_col7={float(data[i][8])}, t_col8={float(data[i][9])}, 
               t_col9={float(data[i][10])}, t_co10={float(data[i][11])}, 
               t_totq={float(data[i][12])} WHERE t_seqn={data[i][0]} AND t_bcod='{t_bcod}' 
               AND t_cact='{t_cact}' AND t_cpla= '{t_cpla}' 
               AND t_cprj= '{t_cprj}' AND t_rabl= '{t_rabl}';
            end
            else
            begin
               INSERT INTO ttpztc1161111
            (t_desc, t_col1, t_col2, t_col3, t_col4,
            t_col5,t_col6, t_col7, t_col8,
            t_col9, t_co10, t_totq,
            t_bcod, t_cact, t_cpla, t_cprj, t_date,
            t_rabl, t_seqn,t_Refcntd,t_Refcntu)
            VALUES
            ('{data[i][1]}', {float(data[i][2])}, {float(data[i][3])} ,{float(data[i][4])},{float(data[i][5])},
            {float(data[i][6])},{float(data[i][7])},{float(data[i][8])},{float(data[i][9])},
            {float(data[i][10])},{float(data[i][11])},{float(data[i][12])},
            '{t_bcod}', '{t_cact}','{t_cpla}', '{t_cprj}',
            '2021-09-20','{t_rabl}',{float(data[i][0])},0,0);
            end
            commit tran"""
                    print(query_set)
                    table = sql_connection_insert(query_set)

    context = {"t_bcod": t_bcod, "t_cact": t_cact, "t_cpla": t_cpla, "t_cprj": t_cprj, "t_rabl": t_rabl}
    # print(context)
    query_set = f"SELECT t_seqn,t_desc, t_col1, t_col2,t_col3,t_col4,t_col5,t_col6,t_col7,t_col8,t_col9,t_co10,t_totq FROM ttpztc1161111 " \
                f"where     t_bcod='{t_bcod}' AND t_cact='{t_cact}' AND t_cpla= '{t_cpla}' AND t_cprj= '{t_cprj}' AND t_rabl= '{t_rabl}'"

    tables = sql_connection_fetch(query_set)
    rangeAll = '{0}!A1:Z'.format('project')
    body = {}
    service.spreadsheets().values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=rangeAll,
                                                        body=body).execute()

    sheet_data = [[
        'SNO',
        'Description',
        'Chainage(A)',
        'No.(B)',
        'Length(C)',
        'Width(D)',
        'Height(E)',
        'Thickness(F)',
        'Diameter(G)',
        'Area 1(H)',
        'Area 2 (I)',
        'Unit Weight (J)',
        'Quantity',
        '',
    ]]
    for table in tables:
        sheet_data.append(list(table))
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED",
                          body={"values": sheet_data}).execute()
    return render(request, 'test.html', context)


@staff_member_required()
def project_report(request):
    context = {}
    if request.method == 'GET':
        query_set = f"SELECT DISTINCT t_bcod, t_cact, t_cpla,t_cpla, t_cprj, t_rabl FROM ttpztc1161111;"
        tables = sql_connection_fetch(query_set)
    context['tables'] = tables
    return render(request, 'project/project_details.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home:home')
