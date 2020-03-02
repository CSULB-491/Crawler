# create hash for name, date, and publishers


class Hashing:

    # init method or constructor 
    def __init__(self, name, date, publisher):
        self.name = name
        self.date = date
        self.publisher = publisher
        self.hash_name = hash(name)
        self.hash_date = hash(date)
        self.hash_publisher = hash(publisher)

    def show(self):
        print("name is", self.name)
        print("date is", self.date)
        print("publishers is", self.publisher)
        print("Hash_name value is:", self.hash_name)
        print("Hash_date value is", self.hash_date)
        print("Hash_publisher value is", self.hash_publisher)

    def __hash__(self):
        return hash(self)

    def get_name(self):
        return self.name

    def set_name(self):
        self.name = self

    def get_date(self):
        return self.date

    def set_date(self):
        self.date = self

    def get_publisher(self):
        return self.publisher

    def set_publisher(self):
        self.publisher = self

# testing
# file1 = Hashing("chris", "10feb18", "bostontimes")
# file2 = Hashing("james", "12feb19", "latimes")

# file1.show()
# file2.show()
