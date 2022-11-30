import unittest
from ListFunction import ListFunction


class ListFunctionTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    # ========== BEGIN APPEND TEST
    def test_append_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR']
        objListFuction = ListFunction(data_list_awal)
        data_append = 'Procolharum'
        result_append = objListFuction.append_function(data_append)
        self.assertEqual(result_append, ['The Beatles', 'CCR', 'Procolharum'])

    def test_append_fail_scenario(self) -> None:
        data_list_awal = ['Serang', 'Jakarta']
        objListFuction = ListFunction(data_list_awal)
        data_append = 'Bandung'
        result_append = objListFuction.append_function(data_append)
        self.assertNotEqual(result_append, ['Jakarta'])
    # ========== END APPEND TEST

    # ========== BEGIN INSERT TEST
    def test_insert_success_scenario(self) -> None:
        data_list_awal = ['Banda Aceh', 'Medan']
        objListFuction = ListFunction(data_list_awal)

        data_indeks = 2
        data_insert = 'Riau'
        result_insert = objListFuction.insert_function(
                data_indeks, data_insert)
        self.assertEqual(result_insert,
                         ['Banda Aceh', 'Medan', 'Riau'])

    def test_insert_fail_scenario(self) -> None:
        data_list_awal = ['Serang', 'Bandung']
        objListFuction = ListFunction(data_list_awal)

        data_indeks = 1
        data_insert = 'Jakarta'
        result_insert = objListFuction.insert_function(
            data_indeks, data_insert)
        self.assertNotEqual(result_insert,
                            ['Serang', 'Bandung', 'Jakarta'])
    # ========== END INSERT TEST

    # ========== BEGIN EXTEND TEST
    def test_extend_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        data_extend = ['Procolharum']
        result_extend = objListFuction.extend_function(data_extend)
        self.assertEqual(result_extend, ['The Beatles', 'CCR', 'Procolharum'])

    def test_extend_fail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        data_extend = ['Procolharum']
        result_extend = objListFuction.extend_function(data_extend)
        self.assertNotEqual(result_extend,
                            ['The Beatles', 'CCR', 'The Rolling Store'])
    # ========== END EXTEND TEST

    # ========== BEGIN LEN TEST
    def test_len_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        result_min = objListFuction.len_function()
        self.assertEqual(result_min, 2)

    def test_len_fail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        result_min = objListFuction.len_function()
        self.assertNotEqual(result_min, 3)
    # ========== END LEN TEST

    # ========== BEGIN MAX TEST
    def test_max_success_scenario(self) -> None:
        data_list_awal = [80, 78, 34]
        objListFuction = ListFunction(data_list_awal)

        result_max = objListFuction.max_function()
        self.assertEqual(result_max, 80)

    def test_max_fail_scenario(self) -> None:
        data_list_awal = [80, 78, 34]
        objListFuction = ListFunction(data_list_awal)

        result_max = objListFuction.max_function()
        self.assertNotEqual(result_max, 3)
    # ========== END MAX TEST

    # ========== BEGIN MIN TEST
    def test_min_success_scenario(self) -> None:
        data_list_awal = [80, 78, 34]
        objListFuction = ListFunction(data_list_awal)

        result_min = objListFuction.min_function()
        self.assertEqual(result_min, 34)

    def test_min_fail_scenario(self) -> None:
        data_list_awal = [80, 78, 34]
        objListFuction = ListFunction(data_list_awal)

        result_min = objListFuction.min_function()
        self.assertNotEqual(result_min, 3)
    # ========== END MAX TEST

    # ========== BEGIN REMOVE TEST
    def test_remove_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum']
        objListFuction = ListFunction(data_list_awal)

        data_remove = 'Procolharum'
        result_remove = objListFuction.remove_function(data_remove)
        self.assertEqual(result_remove, ['The Beatles', 'CCR'])

    def test_remove_fail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum']
        objListFuction = ListFunction(data_list_awal)

        data_remove = 'Procolharum'
        result_remove = objListFuction.remove_function(data_remove)
        self.assertNotEqual(result_remove, ['The Beatles',
                            'The Rolling Stones'])
    # ========== END REMOVE TEST

    # ========== BEGIN DISCARD TEST
    def test_pop_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum']
        objListFuction = ListFunction(data_list_awal)

        indeks_pop = 2
        result_remove = objListFuction.pop_function(indeks_pop)
        self.assertEqual(result_remove, ['The Beatles', 'CCR'])

    def test_pop_fail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum']
        objListFuction = ListFunction(data_list_awal)

        indeks_pop = 2
        result_remove = objListFuction.pop_function(indeks_pop)
        self.assertNotEqual(result_remove, ['The Beatles',
                            'The Rolling Stones'])
    # ========== END DISCARD TEST

    # ========== BEGIN FILTERING EVEN ODD TEST
    def test_even_odd_success_scenario(self) -> None:
        data_list_awal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        objListFuction = ListFunction(data_list_awal)

        result_even = objListFuction.filter_even_odd_function(True)
        self.assertEqual(result_even, [2, 4, 6, 8, 10])

        result_odd = objListFuction.filter_even_odd_function(False)
        self.assertEqual(result_odd, [1, 3, 5, 7, 9])

    def test_even_odd_fail_scenario(self) -> None:
        data_list_awal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        objListFuction = ListFunction(data_list_awal)

        result_even = objListFuction.filter_even_odd_function(False)
        self.assertNotEqual(result_even, [2, 4, 6, 8, 10])

        result_odd = objListFuction.filter_even_odd_function(True)
        self.assertNotEqual(result_odd, [1, 3, 5, 7, 9])
    # ========== BEGIN FILTERING EVEN ODD TEST

    # ========== BEGIN ASCENDING/DESCENDING TEST
    def test_sort_ascending_descending_success_scenario(self) -> None:
        data_list_awal = [3, 7, 6, 10, 1, 5, 9, 8, 2, 4]
        objListFuction = ListFunction(data_list_awal)

        sort_result_ascending = objListFuction\
            .sort_ascending_descending_function(True)
        self.assertEqual(sort_result_ascending,
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        sort_result_descending = objListFuction\
            .sort_ascending_descending_function(False)
        self.assertEqual(sort_result_descending,
                         [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_sort_ascending_descending_fail_scenario(self) -> None:
        data_list_awal = [3, 7, 6, 10, 1, 5, 9, 8, 2, 4]
        objListFuction = ListFunction(data_list_awal)

        sort_result_ascending = objListFuction\
            .sort_ascending_descending_function(True)
        self.assertNotEqual(sort_result_ascending,
                            [1, 2, 3, 4, 5, 6, 7, 10, 9, 8])

        sort_result_descending = objListFuction\
            .sort_ascending_descending_function(False)
        self.assertNotEqual(sort_result_descending,
                            [1, 9, 8, 7, 6, 5, 4, 3, 2, 10])
    # ========== END ASCENDING/DESCENDING TEST

    # ========== BEGIN REMOVE DUPLICATE ELEMENT LIST TEST
    def test_duplicate_element_remove_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        result_duplicate_element = objListFuction\
            .duplicate_element_remove_function()
        self.assertEqual(result_duplicate_element, result_duplicate_element)

    def test_duplicate_element_remove_rail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        result_duplicate_element = objListFuction\
            .duplicate_element_remove_function()
        self.assertNotEqual(result_duplicate_element, ['The Beatles'])
    # ========== END REMOVE DUPLICATE ELEMENT LIST TEST

    # ========== BEGIN COUNT ELEMENT LIST TEST
    def test_count_element_success_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        data_element = 'CCR'
        result_count = objListFuction.count_function(data_element)
        self.assertEqual(result_count, 2)

    def test_count_element_fail_scenario(self) -> None:
        data_list_awal = ['The Beatles', 'CCR', 'Procolharum', 'CCR']
        objListFuction = ListFunction(data_list_awal)

        data_element = 'CCR'
        result_count = objListFuction.count_function(data_element)
        self.assertNotEqual(result_count, 3)
    # ========== END COUNT ELEMENT LIST TEST


if __name__ == '__main__':
    unittest.main()
