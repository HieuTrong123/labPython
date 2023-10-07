from Sinh_Vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from datetime import datetime
class DanhSachSV:
    def __init__(self)->None:
        self.dssv = []
    def ThemSV(self,sv:SinhVien):
        self.dssv.append((sv))
    def Xuat(self):
        for sv in self.dssv:
            print(sv)
    def TimSvTheoMs(self,ms:str):
        for i in range(len(self.dssv)):
            if(self.dssv[i].maSo==ms):
                return i
        else:
            return -1
    def TimSvTheoLoai(self,loai: str):
        if(loai=="chinhquy"):
            return [sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv,SinhVienPhiCQ)]
    def TimSinhVienDRL80(self):
        return list(filter(lambda x:(isinstance(x,SinhVienChinhQuy) and x.diemRL==80),self.dssv))
    def TimSvCaoDang(self):
        return list(filter(lambda x:(isinstance(x,SinhVienPhiCQ) and (x.trinhdo=="Cao đẳng") and (x.ngaySinh <= datetime.strptime("15/8/1999","%d/%m/%Y")))))