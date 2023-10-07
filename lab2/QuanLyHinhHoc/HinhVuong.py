from HinhChuNhat import HinhChuNhat
class HinhVuong(HinhChuNhat):
    def __init__(self,canh:float):
        super().__init__(canh,canh)

    def __str__(self) -> str:
        return f"Hình vuông cạnh: {self.ChieuRong} có diện tích là: {self.TinhDienTich()}"