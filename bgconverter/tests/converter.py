from django.test import TestCase

from bgconverter.views.converter import convert_mg_per_dl_to_mmol_per_l, convert_mmol_per_l_to_mg_per_dl


class ConverterTestCase(TestCase):
    def test_conversion_from_mmol_per_l(self):
        """Test that conversions to mg/dL is 18 times smaller than mmol/L"""
        mmol_per_l = 180.0
        result = convert_mmol_per_l_to_mg_per_dl(mmol_per_l)
        self.assertAlmostEqual(mmol_per_l / 18.0, result)

    def test_conversion_from_mg_per_dl(self):
        """Test that conversions to mmol/L is 18 times larger than mg/dL"""
        mg_per_dl = 10.0
        result = convert_mg_per_dl_to_mmol_per_l(mg_per_dl)
        self.assertAlmostEqual(mg_per_dl * 18.0, result)

    def test_conversion_from_mmol_per_l_as_int(self):
        """Test that conversion to mmol/L from an int works fine """
        mmol_per_l = int(180)
        result = convert_mmol_per_l_to_mg_per_dl(mmol_per_l)
        self.assertAlmostEqual(float(mmol_per_l) / 18.0, result)

    def test_conversion_from_mg_per_dl_as_int(self):
        """Test that conversion to mg/dL from an int works fine """
        mg_per_dl = int(10)
        result = convert_mg_per_dl_to_mmol_per_l(mg_per_dl)
        self.assertAlmostEqual(float(mg_per_dl) * 18.0, result)
