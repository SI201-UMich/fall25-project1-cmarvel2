# Name: Corey Royster
# Student ID: 3620 4751
# Email: cmarvel@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Asked ChatGPT hints for debugging and methods/workaround i.e round(float(),2) to use when code wasn't performing as it should've, formatting txt file output, and Unittest cases

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
        self.nestedcsvfile = ""
        return self.csvfile
    

    def calculate_state_profits(self):
        storedata = self.load_datasheet()
        profitdict = {}

        for row in storedata[1:]:
            if row[4] not in profitdict:
                profitdict[row[4]] = [float(row[9]), float(row[12]),] 
            else:
                profitdict[row[4]] += [float(row[9]), float(row[12])]

        #Implemented due to round(float()) returning values with 2.8999999999999 instead ot 2.90 because of 
        for key, value in profitdict.items():
            Valcheck = 0
            Losscheck = False
            if round(value[1], 2) < Valcheck:
                Losscheck = True

            profitdict[key] = [f"Total sales: {round(value[0], 2)}", f"Total profit: {round(value[1], 2)}", f"Sales Profit Difference: {round(abs(value[0]) - abs(value[1]), 2)}", f"Was there a loss: {Losscheck}"]

        
        return profitdict
    

    def prepare_state_list(self):
        storedata = self.load_datasheet()
        statelist = []
        statedict = {}
        temp = []
        
        for row in storedata[1:]:
            if row[4] not in statelist:
                statelist.append(row[4])
        
        for state in statelist:
            templist = []
            for row in storedata[1:]:
                if row[4] == state:
                    
                    templist.append({row[3]:[]})

                    newtemplist = []
                    for temp in templist:
                        if temp not in newtemplist:
                            newtemplist.append(temp)
            statedict[state] = newtemplist

        
        return statedict


    def state_most_products(self):
        storedata = self.load_datasheet()
        storelocations = self.prepare_state_list()
        
        for state, city in storelocations.items():
            for d in city:
                for k in d:
                    countsegment = {}
                    countcategory = {}
                    for row in storedata[1:]:
                        if row[3] == k and row[4] == state:
                            if row[1] in countsegment:
                                countsegment[row[1]] += 1
                            else:
                                countsegment[row[1]] = 1
                            if row[7] in countcategory:
                                countcategory[row[7]] += 1
                            else:
                                countcategory[row[7]] = 1
                    
                    Maxcat = ""
                    Maxcatd = 0
                    for kk, v in countcategory.items():
                        if v > Maxcatd:
                            Maxcat = kk
                            Maxcatd = v

                    Maxseg = ""
                    Maxsegd = 0
                    for kk, v in countsegment.items():
                        if v > Maxsegd:
                            Maxseg = kk
                            Maxsegd = v

                    d[k] = [{Maxseg:Maxsegd}, {Maxcat:Maxcatd}]
        
        return storelocations
                    
                
    def generate_store_analysis(self):
        profitdata = self.calculate_state_profits()
        itemsdata = self.state_most_products()
        with open("analysis.txt", "w") as ofile:
            ofile.write("State Profit Analysis\n\n")
            pprint.pprint(profitdata, stream=ofile,)

            ofile.write("\n\nState Most Sold Products\n\n")
            pprint.pprint(itemsdata, stream=ofile,)
                
class project1_2(unittest.TestCase):
    def setUp(self):
        self.Teststoredata = Data_Reader('SampleSuperstore.csv')

    #State profits test    
    
    def test_calculate_state_profits_type(self):
        result = self.Teststoredata.calculate_state_profits()
        self.assertIsInstance(result, dict)

    def test_calculate_state_profits_has_state(self):
        result = self.Teststoredata.calculate_state_profits()
        # Normal case: should contain some known state
        self.assertIn("California", result)

    def test_calculate_state_profits_structure(self):
        result = self.Teststoredata.calculate_state_profits()
        # Each value should be a list of 4 formatted strings
        first_key = next(iter(result))
        self.assertEqual(len(result[first_key]), 4)

    def test_calculate_state_profits_losscheck(self):
        result = self.Teststoredata.calculate_state_profits()
        # Edge case: check that the loss boolean is included
        first_key = next(iter(result))
        self.assertTrue(any("Was there a loss" in s for s in result[first_key]))

    #Most frequent product check
    
    def test_state_most_products_type(self):
        result = self.Teststoredata.state_most_products()
        self.assertIsInstance(result, dict)

    def test_state_most_products_nested_structure(self):
        result = self.Teststoredata.state_most_products()
        first_state = next(iter(result))
        self.assertIsInstance(result[first_state][0], dict)

    def test_state_most_products_keys_exist(self):
        result = self.Teststoredata.state_most_products()
        first_state = next(iter(result))
        first_city = next(iter(result[first_state][0]))
        self.assertIsInstance(first_city, str)

    def test_state_most_products_counts_positive(self):
        result = self.Teststoredata.state_most_products()
        first_state = next(iter(result))
        first_city = next(iter(result[first_state][0]))
        counts = result[first_state][0][first_city]
        # Edge case: counts should be a list with 2 dicts (segment + category)
        self.assertEqual(len(counts), 2)

    

def main():
    Storedata = Data_Reader('SampleSuperstore.csv')
    Storedata.load_datasheet()
    Storedata.calculate_state_profits()
    Storedata.prepare_state_list()
    Storedata.state_most_products()
    Storedata.generate_store_analysis()
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()