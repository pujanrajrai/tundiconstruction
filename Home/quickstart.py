import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "/Users/tundi/tundiconstruction/Home/tundi-326306-f1a0d57a21e6.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tundiproject").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records
#
# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1, 2).value  # Get the value of a specific cell
# #
# insertRow = ["apple", "ball", "cat"]
# sheet.append_row(insertRow)  # Insert the list as a row at index 4
#
# sheet.update_cell(2,2, "CHANGED")  # Update one cell
#
# numRows = sheet.row_count  # Get the number of rows in the sheet
