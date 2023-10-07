from datetime import datetime
class SinhVien:
    truong="Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten: str):
        self.__hoTen = hoten

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def hoTen(self, ms: int):
        if (self.ktMsHopLe(ms)):
            self.__maSo = ms
    @staticmethod
    def ktMsHopLe(ms:int):
        return len(str(ms))==7
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
