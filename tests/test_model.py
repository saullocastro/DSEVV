import sys
sys.path.append('..')

from numpy import isclose

from DSEVV.parameters import parameters_dict, Parameters
from DSEVV.model import calc_area, calc_area_dict

def test_calc_area():
    p = Parameters()
    area = calc_area(p)
    assert isclose(area, 25.9807)
    area = calc_area_dict(parameters_dict)
    assert isclose(area, 25.9807)

