from Sinh_Vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from datetime import datetime
from DanhSachSV import DanhSachSV

sv1 = SinhVienChinhQuy(1957690,"Trần văn A",datetime.strptime("23/6/1999","%d/%m/%Y"),80)
sv2 = SinhVienChinhQuy(1957691,"Nguyễn Văn C",datetime.strptime("5/12/1999","%d/%m/%Y"),90)
sv3 = SinhVienPhiCQ(1957692,"Thái Thị thu",datetime.strptime("15/8/1998","%d/%m/%Y"),"Cao đẳng",2)
sv4 = SinhVienPhiCQ(1957693,"Trần Thanh Tam",datetime.strptime("27/8/2000","%d/%m/%Y"),"Trung cấp",2.5)
sv5 = SinhVienChinhQuy(1957694,"Nguyen thanh tra",datetime.strptime("17/5/2000","%d/%m/%Y"),60)

ds =DanhSachSV()
ds.ThemSV(sv1)
ds.ThemSV(sv2)
ds.ThemSV(sv3)
ds.ThemSV(sv4)
ds.ThemSV(sv5)
ds.Xuat()
print("Sinh vien DRL 80")
for i in ds.TimSinhVienDRL80():
    print(i)
print("Sinh Vien Cao dang ")
for i in ds.TimSvCaoDang():
    print(i)
