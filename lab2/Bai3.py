import math
import functools
class PhanSo:
    def __init__(self,tuSo=1,mauSo=1)->None:
        self.tuSo=tuSo
        self.mauSo=mauSo
    def RutGon(self):
        gcd = math.gcd(self.tuSo, self.mauSo)
        self.tuSo = self.tuSo // gcd
        self.mauSo = self.mauSo // gcd
    def __add__(self, other):
        tu_so_moi = self.tuSo * other.mauSo + other.tuSo * self.mauSo
        mau_so_moi = self.mauSo * other.mauSo
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.RutGon()
        return result
    def __sub__(self, other):
        tu_so_moi = self.tuSo * other.mauSo - other.tuSo * self.mauSo
        mau_so_moi = self.mauSo * other.mauSo
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.RutGon()
        return result
    def __mul__(self, other):
        tu_so_moi = self.tuSo * other.tuSo
        mau_so_moi = self.mauSo * other.mauSo
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.RutGon()
        return result
    def __truediv__(self, other):
        tu_so_moi = self.tuSo * other.mauSo
        mau_so_moi = self.mauSo * other.tuSo
        result = PhanSo(tu_so_moi, mau_so_moi)
        result.RutGon()
        return result

    def __str__(self) -> str:
        return f"{self.tuSo}/{self.mauSo}"
class DanhSachPhanSo:
    def __init__(self) -> None:
        self.DSSV = [PhanSo(1,2),PhanSo(1,4),PhanSo(1,2),PhanSo(2,3),PhanSo(2,3),PhanSo(5,4),PhanSo(2,3),PhanSo(3,4),PhanSo(-2,3),PhanSo(2,-3)]
    def DemPSAm(self):
        return len((list(filter(lambda x: (x.tuSo * x.mauSo < 0), self.DSSV))))
    def TimDuongNN(self):
        m=list(filter(lambda x:(x.tuSo/x.mauSo)>0,self.DSSV))
        a=[]
        for i in m:
            if(i!=None):
                a.append((i.tuSo/i.mauSo))
        mina=min(a)
        return min(list(filter(lambda x:(x.tuSo/x.mauSo)==mina,self.DSSV)))
    def TimVTx(self,x:PhanSo):
        # kq=list(filter(lambda e:(e.tuSo/e.mauSo)==(x.tuSo/x.mauSo),self.DSSV))
        for i in range(self.DSSV.__len__()):
            if((self.DSSV[i].tuSo/self.DSSV[i].mauSo)==(x.tuSo/x.mauSo)):
                print(i)
    def TongPSAm(self):
        l = list(filter(lambda x: (x.tuSo / x.mauSo) < 0, self.DSSV))
        sum=l[0]
        for i in range(1, len(l)):
            sum+=l[i]
        return sum
    def XoaX(self,x:PhanSo):
        self.DSSV = list(filter(lambda e:(e.tuSo/e.mauSo!=(x.tuSo/x.mauSo)),self.DSSV))
    def XoaPSTuX(self,x:int):
        self.DSSV = list(filter(lambda e:e.tuSo!=x,self.DSSV))
    def Xuat(self):
        for i in self.DSSV:
            print(i)
    def SapXepTangTheoTu(self):
        self.DSSV.sort(reverse=False,key=lambda e:e.tuSo)



if __name__ == '__main__':
    a = PhanSo(3, 5)
    b = PhanSo(2, 3)
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    ds=DanhSachPhanSo()
    print(ds.DemPSAm())
    print(ds.TimDuongNN())
    print("vi tri x")
    ds.TimVTx(PhanSo(2,3))
    print("Tong PS am la")
    print(ds.TongPSAm())
    print("ds ban dau la")
    ds.Xuat()
    ds.XoaX(PhanSo(2,3))
    print("ds sau khi xoa 2/3 la")
    ds.Xuat()
    print(ds.TongPSAm())
    print("ds ban dau la")
    ds.Xuat()
    ds.XoaPSTuX(1)
    print("ds sau khi xoa ps co tu so 1 la")
    ds.Xuat()
    print("ds sau khi sap xep")
    ds.SapXepTangTheoTu()
    ds.Xuat()

