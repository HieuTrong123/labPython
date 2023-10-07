from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc

connectionString = '''DRIVER={ODBC Driver 17 for SQL Server}; 
                        SERVER=.;DATABASE=QLMonAn;UID=sa;PWD=sa;Encrypt=no'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn


def close_connection(conn):
    if conn:
        conn.close()


def get_all_food_category():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''Select * from NhomMonAn'''
        cursor.execute(select_query)

        records = cursor.fetchall()
        close_connection(connection)
        return records

    except(Exception, pyodbc.Error) as error:
        print('Co loi', error)


def get_food_by_category(catName):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''select *
                            from NhomMonAn
                            where TenNhom like ?'''
        params = (catName)
        cursor.execute(select_query, params)
        category = cursor.fetchone()

        select_query = '''select *
                            from MonAn
                            where Nhom = ?'''
        params = (category[0])
        cursor.execute(select_query, params)
        records = cursor.fetchall()

        close_connection(connection)
        return records

    except(Exception, pyodbc.Error) as error:
        print('Co loi', error)


def get_all_food():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''Select * from MonAn'''
        cursor.execute(select_query)

        records = cursor.fetchall()
        close_connection(connection)
        return records

    except(Exception, pyodbc.Error) as error:
        print('Co loi', error)


def delete_food_by_id(foodId):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''delete from MonAn where MaMonAn=?'''
        params = (foodId,)
        cursor.execute(select_query, params)
        connection.commit()

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi', error)


def insert_food(data):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (?, ?, ?, ?, ?)'''
        params = (data[0], data[1], data[2], data[3], data[4])
        cursor.execute(select_query, params)
        connection.commit()

        close_connection(connection)
        return 1
    except(Exception, pyodbc.Error) as error:
        print("co loi", error)
        return 0


def update_food(data):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''update MonAn
                            set TenMonAn=?, DonViTinh=?, DonGia=?, Nhom=?
                            where MaMonAn=?'''
        params = (data[1], data[2], data[3], data[4], data[0])
        cursor.execute(select_query, params)
        connection.commit()

        close_connection(connection)
        return 1
    except(Exception, pyodbc.Error) as error:
        print("co loi", error)
        return 0


def insert_treeview(rows: tuple):
    tv_dsma.delete(*tv_dsma.get_children())
    for row in rows:
        row = tuple(row)
        tv_dsma.insert("", "end", values=row)


if __name__ == '__main__':
    root = Tk()
    root.title('Quan ly mon an')
    root.geometry('500x400')

    lbl_nhom_MA = Label(root, text="Nhóm món ăn", width=10, font=('bold', 10))
    lbl_nhom_MA.grid(row=0, column=0, padx=20)

    nhom_MA = get_all_food_category()
    options = [nhom[1] for nhom in nhom_MA]

    selected_nhom = StringVar()
    cbb_nhom_MA = ttk.Combobox(root, state="readonly", values=options, textvariable=selected_nhom)
    cbb_nhom_MA.current(0)
    cbb_nhom_MA.grid(row=0, column=1)

    tv_dsma = ttk.Treeview(root)

    tv_dsma['columns'] = ('MaMonAn', 'TenMonAn', 'DVT', 'Gia', 'Nhom')
    tv_dsma.column('#0', width=0, stretch=NO)
    tv_dsma.column('MaMonAn', anchor=CENTER, width=70)
    tv_dsma.column('TenMonAn', anchor=CENTER, width=160)
    tv_dsma.column('DVT', anchor=CENTER, width=50)
    tv_dsma.column('Gia', anchor=CENTER, width=100)
    tv_dsma.column('Nhom', anchor=CENTER, width=100)

    tv_dsma.heading('#0', text='', anchor=CENTER)
    tv_dsma.heading('MaMonAn', text='Ma mon an', anchor=CENTER)
    tv_dsma.heading('TenMonAn', text='Ten mon an', anchor=CENTER)
    tv_dsma.heading('DVT', text='DVT', anchor=CENTER)
    tv_dsma.heading('Gia', text='Gia', anchor=CENTER)
    tv_dsma.heading('Nhom', text='Nhom', anchor=CENTER)

    dsma = get_all_food()
    insert_treeview(dsma)

    tv_dsma.grid(row=2, column=0, columnspan=3, pady=10, padx=10)


    def food_category_changed(event):
        catName = selected_nhom.get()
        foods_by_catName = get_food_by_category(catName)

        insert_treeview(foods_by_catName)


    cbb_nhom_MA.bind('<<ComboboxSelected>>', food_category_changed)


    def selectItem():
        selectedItem = tv_dsma.selection()[0]
        return tv_dsma.item(selectedItem)['values']


    def handle_add_food():
        pass


    def handle_upd_food():
        pass


    def delFood():
        current_item = selectItem()
        foodId = current_item[0]
        delete_food_by_id(foodId)
        dsma = get_all_food()
        insert_treeview(dsma)


    addBtn = Button(root, text="Them mon an", command=handle_add_food)
    addBtn.grid(row=3, column=0)
    updBtn = Button(root, text="Chinh sua mon an", command=handle_upd_food)
    updBtn.grid(row=3, column=1)

    delBtn = Button(root, text="Xoa mon an", command=delFood)
    delBtn.grid(row=3, column=2)

    root.mainloop()