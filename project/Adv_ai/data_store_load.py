class data_store_load:
    """
    : input  : array of dict
      e.g. : [{"a": 1, "b":2}, {"c":3}, {"d":4, "e":5}]

    : output : str
      e.g. : 'a=1;b=2;\nc=3;\nd=4;e=5;\n'
    """

    def __init__(self):
        self.storage = ""

    def to_storage(self, my_array):
        for sub_dict in my_array:
            print (sub_dict)
            if type(sub_dict) == dict:
                for key in sub_dict:
                    self.storage += str(key)
                    self.storage += "="
                    self.storage += str(sub_dict[key])
                    self.storage += ";"
                self.storage += "\n"
        print (self.storage)
        return self.storage

    def to_load(self):
        storage = self.storage
        print (storage)
        return storage
