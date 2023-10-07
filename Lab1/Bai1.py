import os
import datetime
import platform
from math import pi
import calendar
from datetime import date
#Handle Function

#1
def PrintStringFormat():
    s = """Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""
    print(s)

#2
def python_version():
    print(platform.python_version_tuple())

#3
def datetime_now():
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
#4
def DTHinhTron():
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))
#5
def XuatTen():
    fname = input("Input your First Name : ")
    lname = input("Input your Last Name : ")
    print("Hello  " + lname + " " + fname)
#6
def seprated_numble():
    values = input("Input some comma seprated numbers : ")
    list = values.split(",")
    tuple = tuple(list)
    print('List : ', list)
    print('Tuple : ', tuple)
#7
def FileName():
    filename = input("Input the Filename: ")
    f_extns = filename.split(".")
    print("The extension of the file is : " + repr(f_extns[-1]))
#8
def LayDauCuoi():
    color_list = ["Red", "Green", "White", "Black"]
    print("%s %s" % (color_list[0], color_list[-1]))
#9
def HienThiLich():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : %i / %i / %i" % exam_st_date)
#10
def TinhToan():
    n = int(input('nhap n: '))
    print(n+n*n+n*n*n)
#11
def XuatTaiLieu():
    print(abs.__doc__)
#12
def InLich12():
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    print(calendar.month(y, m))
#13
def Bai13():
    print("""
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """)
#14
def Bai14():
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    print(delta.days)
#15
def Bai15():
    pi = 3.1415926535897931
    r = 6.0
    V = 4.0 / 3.0 * pi * r ** 3
    print('The volume of the sphere is: ', V)
#16
def Bai16():
    n = int(input('nhap n: '))
    if n <= 17:
        print(17 - n)
    else:
        print((n - 17) * 2)
#17
def near_thousand():
    n = int(input('nhap n : '))
    print((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#18
def sum_thrice():
    x=int(input('nhap x: '))
    y=int(input('nhap y: '))
    z=int(input('nhap z: '))
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    print(sum)
#19
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    print(text)
  print("Is" + text)
#20
def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   print(result)
#21
def Bai21():
    num = int(input("Enter a number: "))
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
#22
def list_count_4():
    nums = [1, 4, 6, 4, 7, 4]
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    print(count)
#23
def substring_copy(text, n):
    flen = 2
    if flen > len(text):
        flen = len(text)
    substr = text[:flen]
    result = ""
    for i in range(n):
        result = result + substr
    print(result)
#24
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
#25
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
#Menu
def Menu():
    print('\n0.exit program')
    print('\n1. Write a Python program to print the following string in a specific format')
    print('\n2.Write a Python program to find out what version of Python you are using.')
    print('\n3.Write a Python program to display the current date and time.')
    print('\n4.Write a Python program that calculates the area of a circle based on the radius entered by the user.')
    print('\n5. Write a Python program that accepts the users first and last name and prints them in reverse order with a space between them.')
    print('\n6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.')
    print('\n7. Write a Python program that accepts a filename from the user and prints the extension of the file.')
    print('\n8. Write a Python program to display the first and last colors from the following list.')
    print('\n9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).')
    print('\n10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.')
    print('\n11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).')
    print('\n12. Write a Python program that prints the calendar for a given month and year.')
    print('\n13. Write a Python program to print the following here document.')
    print('\n14. Write a Python program to calculate the number of days between two dates.')
    print('\n15. Write a Python program to get the volume of a sphere with radius six.')
    print('\n16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the')
    print('\n17. Write a Python program to test whether a number is within 100 of 1000 or 2000.')
    print('\n18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.')
    print('\n19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".')
    print('\n20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.')
    print('\n21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.')
    print('\n22. Write a Python program to count the number 4 in a given list.')
    print('\n23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string')
    print('\n24. Write a Python program to test whether a passed letter is a vowel or not.')
    print('\n25. Write a Python program that checks whether a specified value is contained within a group of values.')

def HandleMenu():
    while True:
        os.system("CLS")
        Menu()
        s = int(input('\n\nenter your selection:'))
        if s == 0:
            print('\n0.exit program')
            break;
        elif s == 1:
            print('\n1. Write a Python program to print the following string in a specific format')
            PrintStringFormat()
            os.system('pause')
        elif s == 2:
            print('\n2.Write a Python program to find out what version of Python you are using.')
            python_version()
            os.system('pause')
        elif s == 3:
            print('\n3.Write a Python program to display the current date and time.')
            datetime_now()
            os.system('pause')
        elif s == 4:
            print(
                '\n4.Write a Python program that calculates the area of a circle based on the radius entered by the user.')
            DTHinhTron()
            os.system('pause')
        elif s == 5:
            print(
                '\n5. Write a Python program that accepts the users first and last name and prints them in reverse order with a space between them.')
            XuatTen()
            os.system('pause')
        elif s == 6:
            print(
                '\n6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.')
            seprated_numble()
            os.system('pause')
        elif s == 7:
            print(
                '\n7. Write a Python program that accepts a filename from the user and prints the extension of the file.')
            FileName()
            os.system('pause')
        elif s == 8:
            print('\n8. Write a Python program to display the first and last colors from the following list.')
            LayDauCuoi()
            os.system('pause')
        elif s == 9:
            print(
                '\n9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).')
            HienThiLich()
            os.system('pause')
        elif s == 10:
            print('\n10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.')
            TinhToan()
            os.system('pause')
        elif s == 11:
            print(
                '\n11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).')
            XuatTaiLieu()
            os.system('pause')
        elif s == 12:
            print('\n12. Write a Python program that prints the calendar for a given month and year.')
            InLich12()
            os.system('pause')
        elif s == 13:
            print('\n13. Write a Python program to print the following here document.')
            Bai13()
            os.system('pause')
        elif s == 14:
            print('\n14. Write a Python program to calculate the number of days between two dates.')
            Bai14()
            os.system('pause')
        elif s == 15:
            print('\n15. Write a Python program to get the volume of a sphere with radius six.')
            Bai15()
            os.system('pause')
        elif s == 16:
            print(
                '\n16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the')
            Bai16()
            os.system('pause')
        elif s == 17:
            print('\n17. Write a Python program to test whether a number is within 100 of 1000 or 2000.')
            near_thousand()
            os.system('pause')
        elif s == 18:
            print(
                '\n18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.')
            sum_thrice()
            os.system('pause')
        elif s == 19:
            print(
                '\n19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".')
            new_string('DaBest')
            os.system('pause')
        elif s == 20:
            print(
                '\n20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.')
            larger_string('text', 3)
            os.system('pause')
        elif s == 21:
            print(
                '\n21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.')
            Bai21()
            os.system('pause')
        elif s == 22:
            print('\n22. Write a Python program to count the number 4 in a given list.')
            list_count_4()
            os.system('pause')
        elif s == 23:
            print(
                '\n23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string')
            substring_copy('text', 2)
            os.system('pause')
        elif s == 24:
            print('\n24. Write a Python program to test whether a passed letter is a vowel or not.')
            a=input('nhap ky tu de kiem tra nguyen am: ')
            is_vowel(a)
            os.system('pause')
        elif s == 25:
            print(
                '\n25. Write a Python program that checks whether a specified value is contained within a group of values.')
            print(is_group_member([1, 5, 8, 3], 3))
            os.system('pause')



#Main
if __name__ == '__main__':
    HandleMenu()