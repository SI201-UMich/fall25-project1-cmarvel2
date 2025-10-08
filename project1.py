import csv
import unittest
import os

class Data_Reader:

    def __init__(self, file):
        self.file = file

        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.full_path = os.path.join(self.base_path, file)

        with open(self.full_path, 'r') as ofile:
            self.csvfile = csv.reader(ofile)
            self.csvfile = list(self.csvfile)

        self.data_dict = {
            'Ship Mode': [],
            'Segment': [],
            'Country': [],
            'City': [], 
            'State': [],
            'Postal Code': [],
            'Region': [],
            'Category': [],
            'Sub-Category': [],
            'Sales': [],
            'Quantity': [],
            'Discount': [],
            'Profit': []
        }

    def load_Datasheet(self):


        for row in self.csvfile[1:]:
            self.data_dict['Ship Mode'].append(row[0])
            self.data_dict['Segment'].append(row[1])
            self.data_dict['Country'].append(row[2])
            self.data_dict['City'].append(row[3])
            self.data_dict['State'].append(row[4])
            self.data_dict['Postal Code'].append(row[5])
            self.data_dict['Region'].append(row[6])
            self.data_dict['Category'].append(row[7])
            self.data_dict['Sub-Category'].append(row[8])
            self.data_dict['Sales'].append(row[9])
            self.data_dict['Quantity'].append(int(row[10]))
            self.data_dict['Discount'].append(float(row[11]))
            self.data_dict['Profit'].append(float(row[12]))
        
        return self.data_dict

        

    def Get_state_prices(self):
        state_dict = {}

        for state in self.data_dict['State']:
            if state not in state_dict:
                pass




    def Calculate_state_profits(self):

        pass

    def Get_product_freq(self):

        pass

    

def main():
    Storedata = Data_Reader('SampleSuperstore.csv')
    Storedata.load_Datasheet()
    Storedata.Get_state_prices()

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)