import os
from requests import get
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        print('Downloading JSON file and printing entire file:') 
        self.response = get('http://db.cs.pitt.edu/courses/cs1656/data/hours.json', verify=False) 
        print(self.response.content) 

        print('Loading as JSON and iterating one line at a time:') 
        self.hours = json.loads(self.response.content) 
        print(self.hours) 

        print('\nIterating over JSON:') 
        for line in self.hours: 
            print(line)    

    def part4(self):
        #write output to hours.csv
        with open('hours.json', 'r+') as j_file:
            j_data = json.load(j_file)

        csv_file = open('hours.csv', 'w')
        writer = csv.writer(csv_file)

        key_printed = False

        for keys in j_data:
            if key_printed is False:
                writer.writerow(keys)
                key_printed = True    
            writer.writerow(keys.values())
        
        csv_file.close()
        pass
        

    def part5(self):

        c_file = open('hours.csv', 'r')
        reader = csv.reader(c_file)
        print(reader)
        
        #write output to 'part5.txt'
        f = open('part5.txt', 'w') 
        f.writelines(str(reader))
        c_file.close()
        f.close()

    def part6(self):
        #write output to 'part6.txt'
        f = open('part6.txt', 'w') 

        c_file = open('hours.csv', 'r')
        reader = csv.reader(c_file)
        for row in reader:
            print(row)
            f.writelines(str(row)+"\n")

        c_file.close()
        f.close()
        

    def part7(self):
        #write output to 'part7.txt'
        f = open('part7.txt', 'w') 
        
        c_file = open('hours.csv', 'r')
        reader = csv.reader(c_file)
        for row in reader:
            for cell in row:
                print(cell)
                f.writelines(str(cell)+"\n")

        c_file.close()
        f.close()


if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()