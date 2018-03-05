class Lectuer:

    def __init__ (self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_name(self, value):
        self.name = value

    def set_id(self, value):
        self.id = id

    def __str__(self):
        return "Name: %s \n id: %d" % (self.name, self.id) 
