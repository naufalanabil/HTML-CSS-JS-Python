class Mahasiswa:
    def __init__(self, nama: str, npm: int, jurusan: str, no_telp: str) -> None:
        self.__nama = nama
        self.__npm = npm
        self.__jurusan = jurusan
        self.__no_telp = no_telp

    def set_nama(self, new_nama) -> None:
        self.__nama = new_nama

    def set_npm(self, new_npm) -> None:
        self.__npm = new_npm

    def set_jurusan(self, new_jurusan) -> None:
        self.__jurusan = new_jurusan

    def set_no_telepon(self, new_no_telp) -> None:
        self.__no_telp = new_no_telp

    def get_nama(self) -> str:
        return self.__nama

    def get_npm(self) -> int:
        return self.__npm

    def get_jurusan(self) -> str:
        return self.__jurusan

    def get_no_telepon(self) -> str:
        return self.__no_telp

    def show(self):
        print(f"Nama: {self.__nama}")
        print(f"NPM: {self.__npm}")
        print(f"Jurusan: {self.__jurusan}")
        print(f"Nomor Telepon: {self.__no_telp}\n")