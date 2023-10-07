import os
import math
import random


#handle Function
#1
def TinhToan(a,b):
    print(f'a + b = {(a+b)} , a/b = {(a/b)} , a^b = {(a**b)}')
#2
def DTHinhCN(chieu_dai,chieu_rong):
    return chieu_dai * chieu_rong


#3
def KTNT(n):
    if(n<2):
        return False
    else:
        if(n==2):
            return True
        else:
            for i in range(2,n):
                if(n%i==0):
                    return False
    return True
def XuatSoNT(n):
    for i in range(n+1):
        if(KTNT(i)):
            print(i,end='\t')
#4
def KTSoFibo(n):
    for i in range(1,(n+1)):
        if(DeQuyFibo(i)==n):
            return True
    return False

#5
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1

    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
def DeQuyFibo(n):
    if(n==1 or n==2):
        return 1
    else:
        return DeQuyFibo(n-1)+DeQuyFibo(n-2)

#6
def XuatNSoFibo(n):
    for i in range(1,(n+1)):
        print(fibonacci(i),end='\t')
def TongFibo(n):
    tong=0
    for i in range(n):
        tong+=fibonacci(i)
    return tong
def TongFiboDeQuy(n):
    if(n==1):
        return fibonacci(1)
    else:
        return fibonacci(n)+TongFiboDeQuy(n-1)
#7
def Sqrtn(n):
    kq = 0
    for i in range(n):
        kq += i
    return math.sqrt(kq)
#8
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ", + (-c / b))
        return
    # tính delta
    delta = b * b - 4 * a * c
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
    else:
        print("Phương trình vô nghiệm!")
#9
def GiaiThua(n):
    return n * GiaiThua(n-1)
#10
def TamGiac(n):
    a = []

    for i in range(n):
        b = []
        for j in range(n):
            b.append(' ')
        else:
            a.append(b)
    for i in range(n):
        a[i][i]='*'
        a[i][0]='*'
        a[n-1][i]='*'
    for i in range(n):
        for j in range(n):
            print(a[i][j],end='\t')
        print('\n')
#11
def DoiGio():
    gio = 0
    phut = 0
    giay = int(input("Nhap so giay :"))
    if (giay < 60):
        print(f"Thoi gian hoat dong la {gio} gio {phut} phut {giay} giay", gio, phut, giay)
    elif (giay >= 60 and giay < 3600):
        phut = (giay - giay % 60) / 60
        giay %= 60
        print(f"Thoi gian hoat dong la {gio} gio {phut} phut {giay} giay", gio, phut, giay)

    else:
        gio = (giay - giay % 3600) / 3600
        phut = ((giay % 3600) - (giay % 3600) % 60) / 60
        giay = giay - phut * 60 - gio * 3600
        print(f"Thoi gian hoat dong la {gio} gio {phut} phut {giay} giay", gio, phut, giay)

#12
#1
def NhapTuDong(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)
    else:
        print(f'ban da nhap tu dong thanh cong {n} phan tu!')
def XuatList(a):
    for i in a:
        print(i,end=' ')
def KTSoLeKCH5(n):
    if(n%2!=0 and n%5!=0):
        return True
    return False
def XuatSoLe(a):
    for i in a:
        if(KTSoLeKCH5(i)):
            print(i,end=' ')
def XuatFibo(a):
    for i in a:
        if(KTSoFibo(i)):
            print(i,end=' ')
def SoNTMAX(a):
    for i in range(len(a)):
        if(KTNT(a[i])):
            max = a[i]
            for j in range(len(a)):
                if(KTNT(a[j])and a[j]>max):
                    max=a[j]
                else:
                    return max
    return -1
def SoFiboMin(a):
    for i in range(len(a)):
        if (KTSoFibo(a[i])):
            min = a[i]
            for j in range(len(a)):
                if (KTSoFibo(a[j]) and a[j] < min):
                    min = a[j]
                else:
                    return min
    return -1
def TBSoLe(a):
    newlist=list(filter(KTSoLe,a))
    return (sum(newlist)/len(newlist))
def KTSoLe(n):
    if (n%2!=0):
        return True
    else:
        return False
def TichSoLe(a):
    newlist=[filter(KTSoLe,a)]
    sum=1
    for i in newlist:
        sum*=i
    return sum

def Swap(i,j):
    i,j=j,i
    return (i,j)
def TimSoLonThu2(i,a):
    if(i==max(a)):
        return False
    else:
        return True
def XuatSoLonThu2(a):
    newlist = [filter(TimSoLonThu2,a)]
    for i in a:
        if(i == max(newlist)):
            print(i)

#menu
def Menu12():
    print('\n0.Thoát')
    print('\n1.Nhap list')
    print('\n2.Xem list')
    print('\n3. Xuât tất cả các số lẻ không chia hết cho 5')
    print('\n4. Xuất tất cả các số Fibonacci')
    print('\n5. Tìm số nguyên tố lớn nhất')
    print('\n6. Tìm số Fibonacci bé nhất')
    print('\n7. Tính trung bình các số lẻ')
    print('\n8. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
    print('\n9. Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
    print('\n10. Đảo ngược trật tự các phần tử của danh sách')
    print('\n11. Xuất tất cả các số lớn thứ nhì của danh sách')
    print('\n12. Tính tổng các chữ số của tất cả các số trong danh sách')
    print('\n13. Đếm số lần xuất hiện của một số trong danh sách')
    print('\n14. Xuất các số xuất hiện n lần trong danh sách')
    print('\n15. Xuất các số xuất hiện nhiều lần nhất trong danh sách')
def XuLyMenu12(a,n):
    while True:
        os.system("CLS")
        Menu12()
        l = int(input('nhap lua chon cua ban: '))
        if l == 0:
            print('\n0.Thoát chương trình')
            break
        elif l == 1:
            print('\n1.Nhap list')
            n=int(input('nhap so phan tu n: '))
            NhapTuDong(a, n)
            os.system('pause')
        elif l == 2:
            print('\n2.Xem list')
            XuatList(a)
            os.system('pause')
        elif l == 3:
            print('\n3. Xuât tất cả các số lẻ không chia hết cho 5')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print('Danh sach so le khong chia het cho 5 la: ')
            XuatSoLe(a)
            os.system('pause')
        elif l == 4:
            print('\n4. Xuất tất cả các số Fibonacci')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print('danh sach so fibo trong mang la: ')
            XuatFibo(a)
            os.system('pause')
        elif l == 5:
            print('\n5. Tìm số nguyên tố lớn nhất')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print(f'so nguyen to lon nhat la: {SoNTMAX(a)}')
            os.system('pause')
        elif l == 6:
            print('\n6. Tìm số Fibonacci bé nhất')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print(f'so fibo be nhat la: {SoFiboMin(a)}')
            os.system('pause')
        elif l == 7:
            print('\n7. Tính trung bình các số lẻ')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print(f'trung binh so le la: {TBSoLe(a)}')
            os.system('pause')
        elif l == 8:
            print('\n8. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
            print('Danh sach ban dau la: ')
            XuatList(a)
            print(f'tich so le la: {TichSoLe(a)}')
            os.system('pause')
        elif l == 9:
            print('\n9. Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
            print('Danh sach ban dau la: ')
            XuatList(a)
            i=int(input('nhap so chi phan tu dau tien: '))
            j = int(input('nhap so chi phan tu thu hai: '))
            a[i],a[j]=Swap(a[i],a[j])
            print('Danh sach sau khi hoan vi la: ')
            XuatList(a)
            os.system('pause')
        elif l == 10:
            print('\n10. Đảo ngược trật tự các phần tử của danh sách')
            print('Danh sach ban dau la: ')
            XuatList(a)
            a.reverse()
            print('Danh sach sau Dao nguoc la: ')
            XuatList(a)
            os.system('pause')
        elif l == 11:
            print('\n11. Xuất tất cả các số lớn thứ nhì của danh sách')

            os.system('pause')
        elif l == 12:
            print('\n12. Tính tổng các chữ số của tất cả các số trong danh sách')

            os.system('pause')
        elif l == 13:
            print('\n13. Đếm số lần xuất hiện của một số trong danh sách')

            os.system('pause')
        elif l == 14:
            print('\n14. Xuất các số xuất hiện n lần trong danh sách')

            os.system('pause')
        elif l == 15:
            print('\n15. Xuất các số xuất hiện nhiều lần nhất trong danh sách')

            os.system('pause')
#2

#Menu
def Menu():
    print('\n\n\t\t=========MENU=========')
    print('\n0.Thoát chương trình')
    print('\n1.(a + b), a/b, a^b')
    print('\n2. Tính diện tích hình chữ nhật khi biết bán kính')
    print('\n3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước')
    print('\n4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không')
    print('\n5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)')
    print('\n6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)')
    print('\n7. Tính tổng căn bậc 2 của n số nguyên đầu tiên')
    print('\n8. Giải phương trình bậc 2: ax2 + bx + c=0')
    print('\n9. Tính n!')
    print('\n10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)')
    print("""\n11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
ra màn hình 1:2:50.""")
    print('\n12.Cho một mảng số nguyên')
    print('\n\t\t=========END=========\n')

def XuLyMenu():
    while True:
        os.system("CLS")
        Menu()
        l=int(input('Nhập lựa chọn của bạn: '))
        if l==0:
            print('\n0.Thoát chương trình')
            break
        elif l==1:
            print('\n1.(a + b), a/b, a^b')
            a = int(input('nhap a: '))
            b = int(input('nhap b: '))
            TinhToan(a, b)
            os.system('pause')
        elif l == 2:
            print('\n2. Tính diện tích hình chữ nhật khi biết bán kính')
            chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
            chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
            DTHinhCN(chieu_dai, chieu_rong)
            os.system('pause')
        elif l == 3:
            print('\n3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước')
            n=int(input('nhập khoảng n: '))
            XuatSoNT(n)
            os.system('pause')
        elif l == 4:
            print('\n4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không')
            n = int(input('nhập n: '))
            if(KTSoFibo(n)):
                print(f"{n} la so fibo")
            else:
                print(f'{n} khong phai so fibo')
            os.system('pause')
        elif l == 5:
            print('\n5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)')
            n = int(input('nhập n: '))
            print("so fibo thu n la: ",fibonacci(n))
            os.system('pause')
        elif l == 6:
            print('\n6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)')
            n = int(input('nhập n: '))
            XuatNSoFibo(n)
            print("Tong so fibo la: ",TongFiboDeQuy(n))
            os.system('pause')
        elif l == 7:
            print('\n7. Tính tổng căn bậc 2 của n số nguyên đầu tiên')
            n = int(input('nhập n: '))
            print(Sqrtn(n))
            os.system('pause')
        elif l == 8:
            print('\n8. Giải phương trình bậc 2: ax2 + bx + c=0')
            a = float(input("Nhập hệ số bậc 2, a = "))
            b = float(input("Nhập hệ số bậc 1, b = "))
            c = float(input("Nhập hằng số tự do, c = "))
            # Gọi hàm giải phương trình bậc 2
            giaiPTBac2(a, b, c)
            os.system('pause')
        elif l == 9:
            print('\n9. Tính n!')
            n=int(input('nhập n: '))
            print(GiaiThua(n))
        elif l == 10:
            print('\n10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)')
            n = int(input('nhập n: '))
            TamGiac(n)
            os.system('pause')
        elif l == 11:
            print("""\n11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
            Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
            ra màn hình 1:2:50.""")
            DoiGio()
            os.system('pause')
        elif l == 12:
            print('\n12.Cho một mảng số nguyên')
            a = []
            n = 0
            XuLyMenu12(a,n)
            os.system('pause')



if __name__ == '__main__':
    XuLyMenu()