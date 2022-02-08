#creating a class to raise exceptions
#class: grouping of elements with common characteristics. it is used to define a new type of data and the set of operations that can be performed on it. all objects of the same class will have the same attributes and the same way of iterating with the other parts of a program.

class ExamEcxception(Exception):
    pass

class CSVTimeSeriesFile():
   #defines the structure of our data. Information common to the elements of the class. Built-in function.
    def __init__(self, name):
        
        # decciding the name of the file
        self.name = name 

    #function not built in that operates within the class. Functions that operate within the class. Instead of int is the self defined int.

    def get_data(self):
            # Initialise an empty list in which I am going to save our data.
            data = []
    
            # Open the file from which to read the information
            my_file = open(self.name, 'r')

            # Lreading the file line by line
            for line in my_file:
                
                # divide each line on the comma
                elements = line.split(',')
                
                # I remove the newline element (\n) from the last element using the strip.
                elements[-1] = elements[-1].strip()
    
                # If I'm not processing the header
                if elements[0] != 'date':
                    #transform all elements from string to integer
                    elements[1] = int(elements[1])   
               # I add these items to the list 
                    data.append(elements)
            
            # I close the file
            my_file.close()
            # at the end of everything I return the data
            return data

#create a class object and open the file.
time_series_file = CSVTimeSeriesFile(name='data.csv')
#saving the result of get data in time_series
time_series = time_series_file.get_data()


#deining the new function
def compute_avg_monthly_difference(time_series, first_year, last_year):
    #starting our list
    first_year = int(first_year)
    last_year = int(last_year)
    
    #final_list = []
    #average = 0

    #number of years we want to divide to
    years_division = last_year-first_year
    #temp = []
    #sum_ = []
    years_list=[]
    #creating the list of years
    for i in range (years_division+1):
        years_list.append(first_year+i)
        #temp.append(years_list)

    #creo una lista che contiene tutti gli anni da considerare
    #for data in temp:
        #for elements in time_series:
            #elements = elements[0].split('-')
            #if int(elements[0]) == data[0]:
                #data.append(elements[1])

    #prendo elemento indice uno che corrisponde al dato dei passengeri di tutti gli elementi della lista time_series nel get_data ma solamente se l'elemento 0 corrisponde

    #creare lista di liste contenente tutti i dati dei passegeri
    #descrittore di lista
    data = [[element[1] for element in time_series if element[0].startswith(str(year))] for year in years_list]
    lista_ausiliaria = [sum([data[i+1][month] - data[i][month] for i in range(years_division)]) for month in range(12)]
    lista_finale = [x/ years_division for x in lista_ausiliaria]

    #i created a date list that contains all the passenger data of the 12 months divided by year (the list then contains different lists per year that contain the twelve months)
    # then i'll create an auxiliary list which will first do the differences of two years in two years of the same month until i reach the end of all the years. at that time with the sum operator i'll add up all these differences and then this will be my first element of the new list.
    # at this point I will increase the iterator of the month February by one and repeat the whole process
    #at the end I will get a list of twelve elements corresponding to the difference of passengers in two years added together.
    #At the end of all this I will make the final list which must be divided by the number of years considered in order to calculate the average.

    return lista_finale

#list containing as first element the year and then the number of passengers
media = compute_avg_monthly_difference(time_series, '1949', '1951')
print(media)

print('{}'.format(compute_avg_monthly_difference(time_series, '1949', '1951')))