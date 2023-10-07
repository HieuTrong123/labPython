from datetime import datetime
class SinhVien:
    truong: "Đại học đà lạt"
    def __init__(self, maSo: int, hoTen:str, ngaySinh:datetime) ->None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
    @property
    def maSo(self):
        return self.__maSo
    @maSo.setter
    def maSo(self,maso:int):
        if(self.laMaSoHopLe(maso)):
            self.__maSo=maso

    @property
    def hoTen(self):
        return self.__hoTen
    @hoTen.setter
    def hoTen(self,hoTen:str):
        self.__hoTen=hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh
    @ngaySinh.setter
    def ngaySinh(self,ngaySinh:datetime):
        self.__ngaySinh=ngaySinh
    @staticmethod
    def laMaSoHopLe(maSo:int):
        return len(str(maSo)) == 7
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong=tenmoi
    def __str__(self)->str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}\n"
    def Xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
class DanhSachSV:
    def __init__(self):
        self.DSSV = []
    def ThemSinhVien(self,sv:SinhVien):
        self.DSSV.append(sv)
    def Xuat(self):
        for sv in self.DSSV:
            print(sv)
    def TimSVTheoMSSV(self,mssv: int):
        return [sv for sv in self.DSSV if sv.maSo == mssv]
    def TimVTSVTheoMSSV(self,mssv:int):
        for i in range(len(self.DSSV)):
            if self.DSSV[i].maSo == mssv:
                return i
        return -1
    def XoaSinhVienTheoMaSo(self,maSo:int) -> bool:
        vt=self.TimVTSVTheoMSSV(maSo)
        if(vt != -1):
            del self.DSSV[vt]
            return True
        else:
            return False
    def TimSVTheoTen(self,ten:str):
        return [sv for sv in self.DSSV if sv.hoTen == ten]
    def TimSinhVienSinhTruocNgay(self,ngay:datetime):
        return [sv for sv in self.DSSV if sv.ngaySinh < ngay]
    def SapXepTangTheoTen(self):
        self.DSSV.sort(key=lambda x: x.hoTen,reverse=False)

    def SapXepGiamTheoTen(self):
        self.DSSV.sort(key=lambda x: x.hoTen, reverse=True)
    def NhapTuFile(self):
        f = open("SinhVien.txt", "r")
        for x in f:
            a = x.split(',')
            maso = int(a[0])
            hoten=a[1]
            ngaySinh=datetime.strptime(a[2].strip(),"%Y/%m/%d")
            sv = SinhVien(maso,hoten,ngaySinh)
            self.DSSV.append(sv)


    def __str__(self) -> str:
        t=''
        for x in self.DSSV:
            t+=str(x)+'\t'
        return t





if __name__ == '__main__':
    ds=DanhSachSV()
    ds.NhapTuFile()
    print(ds)
    ds.SapXepTangTheoTen()
    print('danh sach sau khi sap xep')
    print(ds)
