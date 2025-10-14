# Name: Corey Royster
# Student ID: 3620 4751
# Email: cmarvel@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Asked ChatGPT hints for debugging and suggesting the general sturcture of the code

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

        pprint.pp(profitdict)
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
        
        #for state, city in storelocations.items():
            #print(city)
            #storelocations[state] = 

        #print(storelocations)


        #for state in storelocations.values():
         #   for city in state:
          #      for row in storedata:
           #         if city == row[3]:
            #            storelocations = [row[1]]
             #           pprint.pp(state)
               
                

                
            





def main():
    Storedata = Data_Reader('SampleSuperstore.csv')
    Storedata.load_datasheet()
    Storedata.calculate_state_profits()
    Storedata.prepare_state_list()
    Storedata.state_most_products()
    

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)