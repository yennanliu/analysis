class data_store_load:

    def __init__(self):
        self.storage = ""

    def my_storage(self, my_array):
        storage = ""
        for sub_dict in my_array:
            print (sub_dict)
            if type(sub_dict) == dict:
                for key in sub_dict:
                    storage += str(key)
                    storage += "="
                    storage += str(sub_dict[key])
                    storage += ";"
                storage += "\n"
        print (storage)
        return storage


    def my_load(self):
        storage = storage
   