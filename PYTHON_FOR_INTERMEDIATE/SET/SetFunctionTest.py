import unittest
from SetFunction import SetFunction


class SetFunctionTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    # ========== BEGIN INTERSECTION TEST
    def test_set_intersection_success_scenario(self) -> None:
        set_satu = {1, 2, 3, 4, 5}
        set_dua = {3, 4, 5, 6, 7}
        set_function = SetFunction(set_satu, set_dua)
        result_intersection = set_function.intersection_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_intersection)
        list_result.sort()
        self.assertEqual(list_result, [3, 4, 5])

    def test_set_intersection_fail_scenario(self) -> None:
        set_satu = {1, 2, 3, 4, 5}
        set_dua = {3, 4, 5, 6, 7}
        set_function = SetFunction(set_satu, set_dua)
        result_intersection = set_function.intersection_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_intersection)
        list_result.sort()
        self.assertNotEqual(list_result, [1, 3, 8])
    # ========== END INTERSECTION TEST

    # ========== BEGIN UNION TEST
    def test_set_union_success_scenario(self) -> None:
        set_satu = {1, 2}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_union = set_function.union_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_union)
        list_result.sort()
        self.assertEqual(list_result, [1, 2, 3, 4])

    def test_set_union_fail_scenario(self) -> None:
        set_satu = {1, 2}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_union = set_function.union_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_union)
        list_result.sort()
        self.assertNotEqual(list_result, [4, 5, 6, 7])
    # ========== END UNION TEST

    # ========== BEGIN DIFFERENCE TEST
    def test_set_difference_success_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4, 5}
        set_function = SetFunction(set_satu, set_dua)
        result_difference = set_function.difference_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_difference)
        list_result.sort()
        self.assertEqual(list_result, [1, 2])

    def test_set_difference_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_difference = set_function.difference_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_difference)
        list_result.sort()
        self.assertNotEqual(list_result, [4, 5])
    # ========== END DIFFERENCE TEST

    # ========== BEGIN SYMMETRICT_DIFFERENCE TEST
    def test_set_symmetric_difference_success_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4, 5}
        set_function = SetFunction(set_satu, set_dua)
        result_symmetric_difference = set_function.\
            symmetric_difference_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_symmetric_difference)
        list_result.sort()
        self.assertEqual(list_result, [1, 2, 4, 5])

    def test_set_symmetric_difference_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_symmetric_difference = set_function.\
            symmetric_difference_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_symmetric_difference)
        list_result.sort()
        self.assertNotEqual(list_result, [1, 4, 5])
    # ========== END SYMMETRICT_DIFFERENCE TEST

    # ========== BEGIN COPY TEST
    def test_set_copy_success_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_function = SetFunction(set_satu, set())
        result_copy = set_function.\
            copy_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_copy)
        list_result.sort()
        self.assertEqual(list_result, [1, 2, 3])

    def test_set_copy_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_function = SetFunction(set_satu, set())
        result_copy = set_function.\
            symmetric_difference_function()

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_copy)
        list_result.sort()
        self.assertNotEqual(list_result, [1, 4, 5])
    # ========== END COPY TEST

    # ========== BEGIN DISCARD TEST
    def test_set_discard_success_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_function = SetFunction(set_satu, set())
        elemen_hapus = 1
        result_discard = set_function.\
            discard_function(elemen_hapus)

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_discard)
        list_result.sort()
        self.assertEqual(list_result, [2, 3])

    def test_set_discard_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_function = SetFunction(set_satu, set())
        elemen_hapus = 1
        result_discard = set_function.\
            discard_function(elemen_hapus)

        # set adalah unordered maka harus dirubah menjadi list terlebih dahulu
        list_result = list(result_discard)
        list_result.sort()
        self.assertNotEqual(list_result, [1, 4, 5])
    # ========== END DISCARD TEST

    # ========== BEGIN ISDISJOINT TEST
    def test_set_isdisjoint_success_scenario(self) -> None:
        set_satu = {1, 2}
        set_dua = {3, 4, 5}
        set_function = SetFunction(set_satu, set_dua)
        result_isdisjoint = set_function.\
            isdisjoint_function()

        self.assertEqual(result_isdisjoint, True)

    def test_set_isdisjoint_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_isdisjoint = set_function.\
            isdisjoint_function()

        self.assertNotEqual(result_isdisjoint, True)
    # ========== END ISDISJOINT TEST

    # ========== BEGIN ISSUBSET TEST
    def test_set_issubset_success_scenario(self) -> None:
        set_satu = {1, 2, 4}
        set_dua = {3, 4, 5, 1, 2}
        set_function = SetFunction(set_satu, set_dua)
        result_issubset = set_function.\
            issubset_function()

        self.assertEqual(result_issubset, True)

    def test_set_issubset_fail_scenario(self) -> None:
        set_satu = {1, 2, 3}
        set_dua = {3, 4}
        set_function = SetFunction(set_satu, set_dua)
        result_issubset = set_function.\
            issubset_function()

        self.assertNotEqual(result_issubset, True)
    # ========== END ISSUBSET TEST

    # ========== BEGIN ISSUPERSET TEST
    def test_set_issuperset_success_scenario(self) -> None:
        set_satu = {1, 2, 3, 4, 5, 6}
        set_dua = {1, 2, 3}
        set_function = SetFunction(set_satu, set_dua)
        result_issuperset = set_function.\
            issuperset_function()

        self.assertEqual(result_issuperset, True)

    def test_set_issuperset_fail_scenario(self) -> None:
        set_satu = {1, 2, 3, 4, 5, 6}
        set_dua = {1, 2, 3}
        set_function = SetFunction(set_satu, set_dua)
        result_issuperset = set_function.\
            issubset_function()

        self.assertNotEqual(result_issuperset, True)
    # ========== END ISSUPERSET TEST


if __name__ == '__main__':
    unittest.main()
