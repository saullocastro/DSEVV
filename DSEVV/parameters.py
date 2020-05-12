# using classes
class Wing(object):
    #NOTE use __slots__ to avoid unintended mistakes
    __slots__ = ['coordroot', 'coordtip', 'span', 'sweepdeg']
    def __init__(self):
        self.coordroot = 2
        self.coordtip = 1
        self.span = 20
        self.sweepdeg = 30

class Fuselage(object):
    #NOTE use __slots__ to avoid unintended mistakes
    __slots__ = ['radius', 'length']
    def __init__(self):
        self.radius = 1.5
        self.length = 30

class Parameters(object):
    __slots__ = ['wing', 'fuselage']
    def __init__(self):
        self.wing = Wing()
        self.fuselage = Fuselage()

# using dictionaries (key: value)
wing = dict(coordroot=2, coordtip=1, span=20, sweepdeg=30)
fuselage = dict(radius=1.5, length=30)
parameters_dict = dict(wing=wing, fuselage=fuselage)

