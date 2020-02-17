# create hash for name, date, and publisher


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
        print("publisher is", self.publisher)
        print("Hash_name value is:", self.hash_name)
        print("Hash_date value is", self.hash_date)
        print("Hash_publisher value is", self.hash_publisher)

    def __hash__(self):
        return hash(self)


# testing
# file1 = Hashing("chris", "10feb18", "bostontimes")
# file2 = Hashing("james", "12feb19", "latimes")

# file1.show()
# file2.show()
