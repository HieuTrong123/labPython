import pyodbc


# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLSinhVien;UID=sa;PWD=sa;Encrypt=no')
def get_connection():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLSinhVien;UID=sa;PWD=sa;Encrypt=no')
def close_connection(conn):
    if(conn):
        conn.close()
def get_all_class():
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="SELECT * from Lop"
        cursor.execute(select_query)
        records=cursor.fetchall()
        print(f"Danh sach cac lop la: ")
        for row in records:
            print("*"*50)
            print("Ma lop: ",row[0])
            print("Ten lop: ",row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("da co loi xay ra khi thuc thi. thong tin loi: ",error)
get_all_class()
def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor=connection.cursor()
        select_query="select * from Lop where id = ?"
        params=(class_id,)
        cursor.execute(select_query,params)
        record=cursor.fetchone()
        print(f"Thong tin lop co id = {class_id} la: ")
        print("Ma lop: ",record[0])
        print("Ten lop: ",record[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ",error)
get_class_by_id(1)

