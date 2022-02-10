#Author: David Gadiaga
#Course: Artficial Intelligence and Data analytics
#Exam: Computer Programmig laboratory

#importing datetime from datetime library
from datetime import datetime

#creating a class to raise exceptions
#class: grouping of elements with common characteristics. it is used to define a new type of data and the set of operations that can be performed on it. All objects of the same class will have the same attributes and the same way of iterating with the other parts of a program.

class ExamException(Exception):
    pass

class CSVFile():
     #defines the structure of our data. Information common to the elements of the class. Built-in function.
    def __init__(self, name):
        
        # decide the name of the file
        self.name = name

        #various exceptions 
        if not isinstance(self.name, str):
            raise ExamException('the name of the file is not string')

        #check if the file is not empty
        if self.__count_lines__() < 1:
            raise ExamException('the file is empty')

    #outside function that checks if the file is not empty
    def __count_lines__(self):
        my_file = open(self.name, 'r')
        lines_file = [1 for k, line in enumerate(my_file) if k>=0 and line != '\n']
        my_file.close
        total_lines = sum(lines_file)
        return total_lines


    def get_data(self):

        # Open the file from which to read the information
        try:
            my_file = open(self.name, 'r')
            my_file.close()
        except:
            raise ExamException('error on either opening or closing the file')

        #reopen the file after closing it for checking
        my_file = open(self.name, 'r')

        # Initialise an empty list in which to save our data.
        data = []
    
        # read the file line by line
        for line in my_file:
                
            # divide each line on the comma
            elements = line.split(',')
                
            # remove the newline element (\n) from the last element using the strip.
            elements[-1] = elements[-1].strip()
    
            # If I'm not processing the header
            if elements[0] != 'date':
                #skip over the parts of the list which have less than 2 arguments
                if len(elements)<2:
                    continue
                #remove excess spaces
                elements[0] = elements[0].strip()
                elements[1] = elements[1].strip()

                #check if elements[0] can be converted into datetime
                try:
                    date_time = datetime.strptime(elements[0], '%Y-%m')
                except:
                    continue

                #transform all elements from string to integer
                try:
                    elements[1] = int(elements[1])
                except:
                    elements[1] = None 
                #if i'm not able to put none instead
  
                #Add these items to the list and in case we have more than two elements add just the first two 
                data.append(elements[:2])
            
        #Close the file
        my_file.close()
        # at the end of everything return data list
        return data

class CSVTimeSeriesFile(CSVFile):
    #since it's not the parential class the __init__ will be inherited from the upper-class
    #not built in function that operates within the class. Instead of int is the self defined int. 
    def get_data(self):
         
        #call back get_data from file CSV
        copy_data = super().get_data()
    
        #check if all the dates are in ascending order and if there are any duplicates
        date_1= copy_data[0][0]

        for elements in copy_data[1:]:
            if date_1 >= elements[0]:
                raise ExamException('The timestamps are not in the correct order')
            date_1 = elements[0]

        return copy_data

#create a class object and open the file.
time_series_file = CSVTimeSeriesFile(name='data.csv')
#save the result of get data in time_series
time_series = time_series_file.get_data()

#define the new function
def compute_avg_monthly_difference(time_series, first_year, last_year):

    if not isinstance(first_year, str) and not(last_year , str):
        raise ExamException('entered data are not strings!')
    #check that first_year and last_year are not empty
    if first_year == '' :
        raise ExamException('The first interval is an empty string!')
    if last_year == '' :
        raise ExamException('The second interval is an empty string!')
    #Check that the strig is an integer number and does not have any other element
    if not first_year.isdigit() and not last_year.isdigit():
        raise ExamException('Strings do not contain numbers!')
    #Check that the final year is not less than the first year:
    if int(last_year) < int(first_year):
        raise ExamException('The initial year is greater than the final year!')
    # Check that the starting year is greater than or equal to 1949
    if int(first_year) < 1949 :
        raise ExamException('The data range considered does not starts in 1949')
    #Check that the final year is less than or equal to 1960
    if int(last_year) > 1960 :
        raise ExamException('The data range considered goes up to 1960')
    #Check that the content of time series is a list
    if not isinstance(time_series, list):
        raise ExamException('time_series is not a list')
    # Check that the list is not empty (since it's an outside function) (the list must have at least one arguments for confrontation) 
    if len(time_series) < 2:
        raise ExamException('The time_series list has not elements!')


    #convert into integers first_year and lats_year
    first_year = int(first_year)
    last_year = int(last_year)
    
    #interval of years we want to divide our average for
    years_interval = last_year-first_year

    #create a list of lists (of the passengers data) which contains as many other lists as the number of years taken into consideration
    # a list that containes as many None lists as the number of the years I am considering
    passengers_list = []
    for years in range(years_interval+1):
        null_list = [None, None, None, None, None, None, None, None, None, None, None, None]
        #adds years at the end of the list. In means that each list will have its corrispondig year
        null_list.append(first_year+ years)
        passengers_list.append(null_list)

    #fill up the list with all the data of the passengers
    #check all the elements of the passengers list
    for arguments in passengers_list:
        #check all the elements of the time series coming from the old get_data
        for elements in time_series:
            #split the first arguemnt (year-mount) by the hyphen
            data = elements[0].split('-')
            #since we divided the month from the year we compare the year(data) to the one on the passengers_list
            if int(data[0]) == arguments[-1]:
                #whenever the year of the split data is the same as the one in the passengers list we put the value of the passenger in the corrisponding index
                #elem[1] corrisponds to the months with the index minus one
                arguments[int(data[1])-1] = elements[1]

    #start summing up all the differences between the years and in case of a none set the difference straight to zero
    #declare the variables needed for the next iteration
    ending_list = []
    months = 0  
    sum_ = 0 

    #make the sum of all the differences between different years for the same month and in the eventuality of a none argument set the difference to zero
    while months < 12:
        for years in range(years_interval):
            if passengers_list[years+1][months] == None or passengers_list[years][months] == None:
                difference = 0
            else:
                difference = passengers_list[years+1][months] - passengers_list[years][months]

            sum_ += difference
        ending_list.append(sum_)
        sum_ = 0
        months+=1
    
    #divide all the endling_list for the years_interval in order to find the average
    ending_list = [x /years_interval for x in ending_list]

    return ending_list

    #I created a date list that contains all the passenger data of the 12 months divided by year (the list then contains different lists per year that contain the twelve months)
    # then i'll create an auxiliary list which will first do the differences of two years in two years of the same month until i reach the end of all the years. at that time with the sum operator i'll add up all these differences and then this will be my first element of the new list.
    # at this point I will increase the iterator of the month February by one and repeat the whole process
    #at the end I will get a list of twelve elements corresponding to the difference of passengers in two years added together.
    #At the end of all this I will make the final list which must be divided by the number of years considered in order to calculate the average.




