import unittest
from collections import OrderedDict
from Decorator_2 import cetak_json_data_dosen, mata_kuliah_pilihan


class Decorator_2_Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    # ========== BEGIN CETAK_JSON_DATA TEST
    def test_cetak_json_data_dosen_success_scenario(self) -> None:
        dict_data_dosen = OrderedDict()
        dict_data_dosen = {
            'nrp': '2404014',
            'nama': 'Yuniar Kurniawan',
            'sex': 'Pria'
        }
        
        data_out = cetak_json_data_dosen(dict_data_dosen)
        self.assertEqual(data_out, '{"nrp": "2404014", "nama": "Yuniar Kurniawan", "sex": "Pria", "mata_kuliah": [{"id": 1, "nama_mata_kuliah": "Pemograman Python", "sks": 4}, {"id": 3, "nama_mata_kuliah": "Pemograman OOP", "sks": 3}, {"id": 6, "nama_mata_kuliah": "Aljabar", "sks": 4}]}')
    # ========== END CETAK_JSON_DATA TEST


if __name__ == '__main__':
    unittest.main()
