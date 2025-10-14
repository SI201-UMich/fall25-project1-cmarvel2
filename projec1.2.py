import csv
import unittest
import os
import pprint

class Data_Reader:

    def __init__(self, file):

        self.file = file

        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.full_path = os.path.join(self.base_path, file)

    def load_datasheet(self):

        with open(self.full_path, 'r') as ofile:
            self.csvfile = csv.reader(ofile)
            self.csvfile = list(self.csvfile)

        return self.csvfile




    def calculate_state_profits(self):
        statedata = self.load_datasheet()
        profitdict = {}

        

        for row in statedata[1:]:
            if row[4] not in profitdict:
                profitdict[row[4]] = [float(row[9]), float(row[12]),] 
            else:
                profitdict[row[4]] += [float(row[9]), float(row[12])]


        #Implemented due to round(float()) returning values with 2.8999999999999 instead ot 2.90 because of 
        for key, value in profitdict.items():
            profitdict[key] = [f"Total sales: {round(value[0], 2)}", f"Total profit: {round(value[1], 2)}"]

        pprint.pp(profitdict)
        return profitdict

    def get_product_freq(self):
        productdata = self.load_datasheet()
        statelist = []

        for row in productdata[1:]:
            if row[]
        



    def state_most_products(self):
        pass




def main():
    Storedata = Data_Reader('SampleSuperstore.csv')
    Storedata.load_datasheet()
    Storedata.calculate_state_profits()
    

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)