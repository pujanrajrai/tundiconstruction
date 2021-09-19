import pyodbc


def sql_connection(query_set):
    try:
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=103.198.8.59;'
            'PORT=1433;'
            'DATABASE=erpln10db;'
            'UID=sa;'
            'PWD=Tundi@2019;')

        cursor = cnxn.cursor()
        cursor.execute(query_set)
        tables = cursor.fetchall()
        cursor.close()
        cnxn.close()
        return tables
    except pyodbc.Error as ex:
        return ex.args[1]


