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


if __name__ == '__main__':
    unittest.main()
