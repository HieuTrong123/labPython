import math
from HinhHoc import HinhHoc
class HinhTron(HinhHoc):
    def __init__(self,banKinh:float):
        self.__banKinh=banKinh
    @property
    def BsnKinh(self):
        return self.__banKinh
    def TinhDienTich(self) -> float:
        return math.pi*(self.__banKinh**2)
    def __str__(self) -> str:
        return f"Hinh tron co ban kinh R: {self.__banKinh} diện tích: {round(self.TinhDienTich())}"