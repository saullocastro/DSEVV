from numpy import pi

from .parameters import Parameters, parameters_dict

def calc_wetarea(p):
    return 2*pi*p.fuselage.radius*p.fuselage.length
