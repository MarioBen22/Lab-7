# Mario Benavides
# Status - Completed
# This program will calculate the total rainfall for the year, 
# the average rainfall for the year, 
# and the months with the highest and lowest rainfall.



def main():
        num_months = 12 # set the range
        total = 0 # for math
        
        # Create a list of months.
        months = ['January', 'Febuary', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
        
        # Create an empty list to store the rainfall amounts.
        rain_amount = [0]*num_months



        
        # Use a loop to ask the user for the rainfall amount for the month 
        # and store it in the list at the appropriate index for the month.
        try:
                
                for index in range(num_months): 
                        print('Enter the rainfall for ', months[index], ': ', sep='', end='')            
                        rain_amount[index] = float(input()) # input into index
                        while rain_amount[index] < 0: # input validation
                                rain_amount[index] = float(input('Error: Each rainfall amount '
                                                        'should be a positive number: '))

                                
                        num_months+1 # count up to range

                        total += rain_amount[index] # for math
                
        except ValueError: # so it doesnt just crash and burn.
                print('Error: Please enter a rainfall amount for each month.')



                
        # display the values entered
        print() # extra space
        print('Total rainfall: ', format(total, ',.2f')) 
        
        average = total / len(months)
        print('Average rainfall: ', format(average, ',.2f')) 
        
        highest = max(rain_amount)
        which_month = months[rain_amount.index(highest)] # new variable, which month, numbers, biggest one, to the variable
        print('Highest rainfall: ', which_month)
        
        lowest = min(rain_amount)
        which_month = months[rain_amount.index(lowest)] # new variable, which month, numbers, lowest one, to the variable
        print('Lowest rainfall: ', which_month)
        
                        
# call the main function
main()
