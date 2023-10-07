from tkinter import *
from App import App
from tkinter import ttk
# from openpyxl import *
# import os
#
#
# wb = load_workbook('C:\\Users\\Admin\\Desktop\\excel.xlsx')
#
# # create the sheet object
# sheet = wb.active
# def excel():
#     # resize the width of columns in
#     # excel spreadsheet
#     sheet.column_dimensions['A'].width = 30
#     sheet.column_dimensions['B'].width = 10
#     sheet.column_dimensions['C'].width = 10
#     sheet.column_dimensions['D'].width = 20
#     sheet.column_dimensions['E'].width = 20
#     sheet.column_dimensions['F'].width = 40
#     sheet.column_dimensions['G'].width = 50
#
#     # write given data to an excel spreadsheet
#     # at particular location
#     sheet.cell(row=1, column=1).value = "Name"
#     sheet.cell(row=1, column=2).value = "Course"
#     sheet.cell(row=1, column=3).value = "Semester"
#     sheet.cell(row=1, column=4).value = "Form Number"
#     sheet.cell(row=1, column=5).value = "Contact Number"
#     sheet.cell(row=1, column=6).value = "Email id"
#     sheet.cell(row=1, column=7).value = "Address"


root=Tk()
app= App(root)
header=Label(root,text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN",fg="red",bg="light green",font=("regular",20),pady=10,padx=70).grid(row=0,column=0,columnspan = 4)
lblmssv=Label(root,text="Mã số sinh viên",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=1,column=0,sticky=W)
inpmssv=Entry(root).grid(row=1,column=1,columnspan = 4,sticky=EW,padx=20)
lblhoTen=Label(root,text="Họ tên",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=2,column=0,sticky=W)
inphoTen=Entry(root).grid(row=2,column=1,columnspan = 4,sticky=EW,padx=20)
lblngaySinh=Label(root,text="Ngày sinh",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=3,column=0,sticky=W)
inpngaySinh=Entry(root).grid(row=3,column=1,columnspan = 4,sticky=EW,padx=20)
lblEmail=Label(root,text="Email",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=4,column=0,sticky=W)
inpEmail=Entry(root).grid(row=4,column=1,columnspan = 4,sticky=EW,padx=20)
lblsdt=Label(root,text="Số điện thoại",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=5,column=0,sticky=W)
inpsdt=Entry(root).grid(row=5,column=1,columnspan = 4,sticky=EW,padx=20)
lblhocKy=Label(root,text="Học kỳ",fg="#000",bg="light green",font=("regular",10),padx=10).   grid(row=6,column=0,sticky=W)
inphocKy=Entry(root).grid(row=6,column=1,columnspan = 4,sticky=EW,padx=20)
lblnamHoc=Label(root,text="Năm học",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=7,column=0,sticky=W)
cbbMonHoc=ttk.Combobox(root,values=["2022-2023", "2023-2024", "2024-2025"]).grid(row=7,column=1,columnspan = 4,sticky=EW,padx=20)
lblchonMonHoc=Label(root,text="Chọn môn học",fg="#000",bg="light green",font=("regular",10),padx=10).grid(row=8,column=0,sticky=W)

cbLTP=Checkbutton(root, text = "Lập trình Python", variable = IntVar(),onvalue = 1, offvalue = 0,bg="light green").grid(row=9,column=1,sticky=W,padx=20,pady=10)
cbCNPM=Checkbutton(root, text = "Công nghệ phần mềm", variable = IntVar(),onvalue = 1, offvalue = 0,bg="light green").grid(row=10,column=1,sticky=W,padx=20,pady=10)
cbLTJ=Checkbutton(root, text = "Lập trình Java", variable = IntVar(),onvalue = 1, offvalue = 0,bg="light green").grid(row=9,column=2,sticky=W,padx=20,pady=10)
cbPTW=Checkbutton(root, text = "phát triển ứng dụng web", variable = IntVar(),onvalue = 1, offvalue = 0,bg="light green").grid(row=10,column=2,sticky=W,padx=20,pady=10)
button=Frame(root,bg="light green")
Button(button,text='Đăng ký',bg="green").grid(row=0,column=0,padx=70)
Button(button,text='Thoát',bg="green",command=root.quit).grid(row=0,column=1,padx=70)
button.columnconfigure(1,weight=2)
button.grid(row=11,column=1,columnspan = 2,sticky=W)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.mainloop()