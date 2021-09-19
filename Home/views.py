from django.shortcuts import render, HttpResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


# Get a list of all records


def home(request):
    return render(request, 'home/home.html')


def sheet(request):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "/Users/tundi/tundiconstruction/Home/tundi-326306-f1a0d57a21e6.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("tundiproject").sheet1  # Open the spreadhseet

    data = sheet.get_all_values()

    for i in range(1, len(data)):
        print(data[i])
    return render(request, 'test.html')
