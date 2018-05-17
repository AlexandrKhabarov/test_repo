import pandas as pd
import unittest
import math
from analysis_dataset.analysis_tools.calculater.calculater import DensityCalcDataFrame


class DensityCalcDataFrameTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculater = DensityCalcDataFrame()
        cls.bad_data_frame = pd.DataFrame({
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
            "RH_1": [64.78, 65.93, 65.85, 64.57, 65.90],
            "BP_1": [981.043, 980.985, 980.9854, 980.0305, 981.0222],
            "TEMP_1": [0.345, 0.123, 0.456, 0.123, 0.457]
        }).set_index("Timestamp")

    def test_calc_density(self):
        """Test calculation Density"""
        good_data_frame = pd.DataFrame({
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
            "RH_1": [64.78, 65.93, 65.85, 64.57, 65.90],
            "BP_1": [981.043, 980.985, 980.9854, 980.0305, 981.0222],
            "TEMP_1": [0.345, 0.123, 0.456, 0.123, 0.457],
            "AD_1": [1.24758, 1.24852, 1.24696, 1.24734, 1.24700],
        }).set_index("Timestamp")

        result = self.calculater.calc_density(self.bad_data_frame)
        pd.testing.assert_frame_equal(result, good_data_frame, check_like=True)


if __name__ == "__main__":
    unittest.main()
