# using classes
class Wing(object):
    #NOTE use __slots__ to avoid unintended mistakes
    __slots__ = ['coordroot', 'coordtip', 'span', 'sweepdeg']
    def __init__(self):
        self.coordroot = 2
        self.coordtip = 1
        self.span = 20
        self.sweepdeg = 30

class Parameters(object):
    __slots__ = ['wing']
    def __init__(self):
        self.wing = Wing()

# using dictionaries (key: value)
wing = dict(coordroot=2, coordtip=1, span=20, sweepdeg=30)
parameters_dict = dict(wing=wing)

