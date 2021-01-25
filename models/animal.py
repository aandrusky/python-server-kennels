class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, breed, status, location_id, customer_id, unique_id):
        self.id = unique_id
        self.name = name
        self.breed = breed
        self.status = status
        self.locationid = location_id
        self.customerid = customer_id
        self.location = None
        self.customer = None