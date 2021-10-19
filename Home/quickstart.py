from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/Users/tundi/tundiconstruction/Home/tundi-326306-f1a0d57a21e6.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = None
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1dgCnjuQXb_AuOU7_kxTIPow31jw8DeSjgbqUfdvsx8o'

service = build('sheets', 'v4', credentials=credentials)
SAMPLE_RANGE_NAME = 'project'

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
import pdb;pdb.set_trace()

print(result)
# values = result.get('values', [])
#
# if not values:
#     print('No data found.')
# else:
#     print('Name, Major:')
#     for row in values:
#         # Print columns A and E, which correspond to indices 0 and 4.
#         print('%s, %s' % (row[0], row[4]))

