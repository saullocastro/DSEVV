from numpy import deg2rad, cos

from .parameters import Parameters, parameters_dict


def calc_area(p):
    return (p.wing.coordroot + p.wing.coordtip)*p.wing.span*cos(deg2rad(p.wing.sweepdeg))/2


def calc_area_dict(pd):
    cr = pd['wing']['coordroot']
    ct = pd['wing']['coordtip']
    span = pd['wing']['span']
    sweepdeg = pd['wing']['sweepdeg']

    return (cr + ct)*span*cos(deg2rad(sweepdeg))/2

