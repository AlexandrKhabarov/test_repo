import pandas as pd
import unittest
from analysis_dataset.analysis_tools.filter.filter import FilterDataFrame


class TestFilterDataFrameMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filtration = FilterDataFrame
        cls.test_data_frame = {
            "Timestamp": [
                "03.04.2017 3:25",
                "03.04.2017 3:45",
                "03.04.2017 3:55",
                "03.04.2017 4:05",
                "03.04.2017 4:15"
            ],
            "WS_1": [1, 2, 3, 4, 5],
            "WS_2": [1, 2, 3, 4, 5],
            "WS_3": [1, 2, 3, 4, 5],
            "WS_4": [1, 2, 3, 4, 5],
            "WD_1": [10, 20, 12, 123, 145],
            "WD_2": [11, 21, 12, 145, 150],
            "WD_3": [12, 32, 4, 156, 212],
            "WD_4": [19, 89, 75, 109, 178],
        }
        cls.data_frame = pd.DataFrame(cls.test_data_frame).set_index("Timestamp")

    def test_filter_by_direct(self):
        """Test filter by direct"""
        good_data_set = {
            "Timestamp": [
                "03.04.2017 4:05",
                "03.04.2017 4:15"
            ],
            "WS_1": [4, 5],
            "WS_2": [4, 5],
            "WS_3": [4, 5],
            "WS_4": [4, 5],
            "WD_1": [123, 145],
            "WD_2": [145, 150],
            "WD_3": [156, 212],
            "WD_4": [109, 178],
        }

        good_data_frame = pd.DataFrame(good_data_set).set_index("Timestamp")

        filter_df = self.filtration.filter_by_direct(
            self.data_frame,
            "WD_1",
            100,
            200
        )

        pd.testing.assert_frame_equal(filter_df, good_data_frame)

    def test_filter_by_speed(self):
        """Test filter by speed"""
        good_data_set = {
            "Timestamp": [
                "03.04.2017 3:25",
                "03.04.2017 3:45",
                "03.04.2017 3:55",
            ],
            "WS_1": [1, 2, 3],
            "WS_2": [1, 2, 3],
            "WS_3": [1, 2, 3],
            "WS_4": [1, 2, 3],
            "WD_1": [10, 20, 12],
            "WD_2": [11, 21, 12],
            "WD_3": [12, 32, 4],
            "WD_4": [19, 89, 75],
        }

        good_data_frame = pd.DataFrame(good_data_set).set_index("Timestamp")

        filter_df = self.filtration.filter_by_speed(
            self.data_frame,
            "WS_1",
            1,
            3
        )
        pd.testing.assert_frame_equal(filter_df, good_data_frame)

    def test_grouped_data_frame(self):
        good_data_sets = [
            pd.DataFrame(
                {'WS_1': {'03.04.2017 3:25': 1, '03.04.2017 3:45': 2, '03.04.2017 3:55': 3},
                 'WS_2': {'03.04.2017 3:25': 1, '03.04.2017 3:45': 2, '03.04.2017 3:55': 3},
                 'WS_3': {'03.04.2017 3:25': 1, '03.04.2017 3:45': 2, '03.04.2017 3:55': 3},
                 'WS_4': {'03.04.2017 3:25': 1, '03.04.2017 3:45': 2, '03.04.2017 3:55': 3},
                 'WD_1': {'03.04.2017 3:25': 10, '03.04.2017 3:45': 20, '03.04.2017 3:55': 12},
                 'WD_2': {'03.04.2017 3:25': 11, '03.04.2017 3:45': 21, '03.04.2017 3:55': 12},
                 'WD_3': {'03.04.2017 3:25': 12, '03.04.2017 3:45': 32, '03.04.2017 3:55': 4},
                 'WD_4': {'03.04.2017 3:25': 19, '03.04.2017 3:45': 89, '03.04.2017 3:55': 75},

                 }),
            pd.DataFrame({
                'WS_1': {'03.04.2017 4:05': 4, '03.04.2017 4:15': 5},
                'WS_2': {'03.04.2017 4:05': 4, '03.04.2017 4:15': 5},
                'WS_3': {'03.04.2017 4:05': 4, '03.04.2017 4:15': 5},
                'WS_4': {'03.04.2017 4:05': 4, '03.04.2017 4:15': 5},
                'WD_1': {'03.04.2017 4:05': 123, '03.04.2017 4:15': 145},
                'WD_2': {'03.04.2017 4:05': 145, '03.04.2017 4:15': 150},
                'WD_3': {'03.04.2017 4:05': 156, '03.04.2017 4:15': 212},
                'WD_4': {'03.04.2017 4:05': 109, '03.04.2017 4:15': 178},
            })
        ]

        grouped = self.filtration.group_data_frame(
            self.data_frame, 1, 5, 3, "WS_1"
        )

        for i, grp in enumerate(grouped.groups):
            good_data_sets[i].index.name = "Timestamp"
            pd.testing.assert_frame_equal(grouped.get_group(grp), good_data_sets[i])


if __name__ == "__main__":
    unittest.main()
