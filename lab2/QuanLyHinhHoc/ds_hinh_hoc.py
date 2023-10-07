from HinhHoc import HinhHoc
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron
from HinhVuong import HinhVuong
from LoaiHinh import LoaiHinh
class DanhSachHinhHoc:
    def __init__(self):
        self.__DSHH = []
    def ThemHinh(self,hh:HinhHoc):
        self.__DSHH.append(hh)


    def TimDienTichLonNhat(self):
        max=self.__DSHH[0].TinhDienTich()
        for e in self.__DSHH:
            if e.TinhDienTich() > max:
                max = e.TinhDienTich()
        return max
    def TimDienTichNhoNhat(self):
        min=self.__DSHH[0].TinhDienTich()
        for e in self.__DSHH:
            if e.TinhDienTich() < min:
                min = e.TinhDienTich()
        return min

    def timHinhCoDienTichLonNhat(self):
        max=self.TimDienTichLonNhat()
        return list(filter(lambda a:a.TinhDienTich() == max,self.__DSHH))
    def TimHinhCoDienTichNhoNhat(self):
        min = self.TimDienTichNhoNhat()
        return list(filter(lambda a: a.TinhDienTich() == min, self.__DSHH))
    def TimDTHinhTronNhoNhat(self):
        min = -1
        for e in self.__DSHH:
            if isinstance(e,HinhTron):

                min = e.TinhDienTich()
                for i in self.__DSHH:

                    if isinstance(i,HinhTron) and i.TinhDienTich()<min:
                        min=i.TinhDienTich()
                else:
                    break

        return min

    def TimHinhTronNhoNhat(self):
        min=self.TimDTHinhTronNhoNhat()
        return list(filter(lambda e : e.TinhDienTich() == min,self.__DSHH))
    def SapGiamTheoDienTich(self):
        self.__DSHH.sort(reverse=True, key=lambda e: e.TinhDienTich())
    def TinhTongDienTich(self):
        sum=0.0
        for i in self.__DSHH:
            sum+=i.TinhDienTich()
        return sum
    def DemSoLuongHinh(self,kieu:LoaiHinh):
        if(kieu==LoaiHinh.HinhTron):
            return len(list(filter(lambda a: isinstance(a, HinhTron), self.__DSHH)))
        elif(kieu==LoaiHinh.HinhChuNhat):
            return len(list(filter(lambda a: isinstance(a, HinhChuNhat), self.__DSHH)))
        elif (kieu==LoaiHinh.HinhVUong):
            return len(list(filter(lambda a: isinstance(a, HinhVuong), self.__DSHH)))
        else:
            return len(self.__DSHH)
    def XuatHinhTheoChieuTangGiam(self,kieu:LoaiHinh,tang:bool):
        if (kieu == LoaiHinh.HinhTron):
            l=list(filter(lambda a: isinstance(a, HinhTron), self.__DSHH))
            l.sort(reverse=tang,key=lambda e:e.TinhDienTich())

            self.XuatDSTimKiem("danh sach sau khi sap xep la: ",l)
        elif (kieu == LoaiHinh.HinhChuNhat):
            l=list(filter(lambda a: isinstance(a, HinhChuNhat), self.__DSHH))
            l.sort(reverse=tang,key=lambda e:e.TinhDienTich())

            self.XuatDSTimKiem("danh sach sau khi sap xep la: ",l)
        elif (kieu == LoaiHinh.HinhVUong):
            l=list(filter(lambda a: isinstance(a, HinhVuong), self.__DSHH))
            l.sort(reverse=tang,key=lambda e:e.TinhDienTich())

            self.XuatDSTimKiem("danh sach sau khi sap xep la: ",l)

    def Xuat(self):
        print('=' * 50)
        print("Danh sách tất cả hình:")
        print('-' * 50)
        for i in self.__DSHH:
            print(i)
        print('=' * 50)
        print('\n\n')

    @staticmethod
    def XuatDSTimKiem(title,DSHH):
        print('=' * 50)
        print(title)
        print('-' * 50)
        for i in DSHH:
            print(i)
        print('=' * 50)
        print('\n\n')