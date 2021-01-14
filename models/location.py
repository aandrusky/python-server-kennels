class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, clinic_name, clinic_address):
        self.id = id
        self.name = clinic_name
        self.address = clinic_address