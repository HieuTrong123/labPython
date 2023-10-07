from HinhHoc import HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self,dai:float,rong:float):
        self.__rong = rong
        super().__init__(dai)

    @property
    def ChieuDai(self):
        return self._canh

    @property
    def ChieuRong(self):
        return self.__rong

    def TinhDienTich(self) -> float:
        return self.ChieuDai*self.ChieuRong
    def __str__(self) -> str:
        return f"Hình chữ nhật có chiều dài: {self.ChieuDai} chiều rộng: {self.ChieuRong} có diện tích là: {self.TinhDienTich()}"