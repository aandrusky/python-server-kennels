class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, customer_address, email_address, login_password):
        self.id = id
        self.name = name
        self.address = customer_address
        self.email = email_address
        self.password = login_password
       