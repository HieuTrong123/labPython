from HinhHoc import HinhHoc
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron
from HinhVuong import HinhVuong
from ds_hinh_hoc import DanhSachHinhHoc
from LoaiHinh import LoaiHinh
hh1=HinhVuong(5)
hh2=HinhTron(5)
hh3=HinhChuNhat(5,7)
hh4=HinhTron(4)
ds=DanhSachHinhHoc()
ds.ThemHinh(hh1)
ds.ThemHinh(hh2)
ds.ThemHinh(hh3)
ds.ThemHinh(hh4)
ds.Xuat()
ds.XuatDSTimKiem("danh sach hinh co dien tich lon nhat la: ",ds.timHinhCoDienTichLonNhat())
ds.XuatDSTimKiem("danh sach hinh co dien tich nho nhat la: ",ds.TimHinhCoDienTichNhoNhat())
ds.XuatDSTimKiem("Danh sach hinh tron nho nhat la: ",ds.TimHinhTronNhoNhat())
ds.SapGiamTheoDienTich()
print("Danh sách sau khi sắp giảm theo diện tích")
ds.Xuat()
print(f"Tổng diện tích là: {round(ds.TinhTongDienTich())}")
print(f"số hình là: {ds.DemSoLuongHinh(LoaiHinh.Tatca)}")
print(f"số hình tròn là: {ds.DemSoLuongHinh(LoaiHinh.HinhTron)}")
print(f"số hình chữ nhật là: {ds.DemSoLuongHinh(LoaiHinh.HinhChuNhat)}")
print(f"số hình vuông là: {ds.DemSoLuongHinh(LoaiHinh.HinhVUong)}")
ds.XuatHinhTheoChieuTangGiam(LoaiHinh.HinhTron,False)
