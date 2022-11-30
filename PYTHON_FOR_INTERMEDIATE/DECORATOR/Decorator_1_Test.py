import unittest
from Decorator_1 import cetak_nama, list_bilangan, cetak_nama_siswa

class Decorator_1_Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    # ========== BEGIN CETAK_NAMA TEST
    def test_cetak_nama_success_scenario(self) -> None:
        nama = 'Yuniar'
        result_cetak_nama = cetak_nama(nama)
        self.assertEqual(result_cetak_nama, f'Nama saya adalah Yuniar. Lahir di kota Bandung')

    def test_cetak_nama_fail_scenario(self) -> None:
        nama = 'Yuniar'
        result_cetak_nama = cetak_nama(nama)
        self.assertNotEqual(result_cetak_nama, f'Nama saya adalah Lain')
    # ========== END CETAK_NAMA TEST

    # ========== BEGIN CETAK_BILANGAN_GENAP TEST
    def test_cetak_bilangan_genap_success_scenario(self) -> None:
        list_data = [1, 2, 3, 4, 5, 6, 7, 8]
        result_list_bilangan_genap = list_bilangan(list_data)
        self.assertEqual(result_list_bilangan_genap, [2, 4, 6, 8])

    def test_cetak_bilangan_genap_fail_scenario(self) -> None:
        list_data = [1, 2, 3, 4, 5, 6, 7, 8]
        result_list_bilangan_genap = list_bilangan(list_data)
        self.assertNotEqual(result_list_bilangan_genap, [2, 4, 6, 7])
    # ========== END CETAK_BILANGAN_GENAP TEST

    # ========== BEGIN NAMA_SISWA TEST
    def test_cetak_nama_lengkap_success_scenario(self) -> None:
        
        nama = 'Yuniar'
        data_out = cetak_nama_siswa(nama)
        self.assertEqual(data_out, 'Nama : Yuniar Kurniawan')

    def test_cetak_nama_lengkap_fail_scenario(self) -> None:
        nama = 'Yuniar'
        data_out = cetak_nama_siswa(nama)
        self.assertNotEqual(data_out, 'Nama : Yuniar')
    # ========== END NAMA_SISWA TEST


if __name__ == '__main__':
    unittest.main()
