class Pet:
    def __init__(self, nama: str, jenis: str, umur: int) -> None:
        self.__nama = nama
        self.__jenis = jenis
        self.__umur = umur

    def set_nama(self, nama: str):
        self.__nama = nama

    def set_jenis(self, jenis: str):
        self.__jenis = jenis

    def set_umur(self, umur: int):
        self.__umur = umur

    def get_nama(self) -> str:
        return self.__nama

    def get_jenis(self) -> str:
        return self.__jenis

    def get_umur(self) -> int:
        return self.__umur