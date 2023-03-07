import os
import csv

cwd = os.getcwd()
csvpath = os.path.join(cwd,'Resources','budget_data.csv')

#determine variables
month_count = 0
prior_month = []
current_month = []
month_change = 0
monthly_change_array = []
net_income = 0
average_change = 0
max_increase = 0
max_decrease = 0
month = []

#set dataset to go through with reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header=next(csvreader)
    #loop through dataset to calculate
    for row in csvreader:
        month_count = month_count + 1
        prior_month.append(int(row[1]))
        current_month.append(int(row[1]))
        month.append(row[0])
        net_income = net_income + int(row[1])
#remove last position for prior month and first position for current month in order to calculate difference

prior_month.pop(85)
current_month.pop(0)
#print(net_income)
#zip amounts into a new list
new_month_list = zip(prior_month, current_month)

#go through new list and take the difference between current month and prior month into the month change array
for i,j in new_month_list:
    monthly_change_array.append(j-i)

#determine position of max increase as well as the amount of max increase
    #max increase
max_increase_index = monthly_change_array.index(max(monthly_change_array))+1
max_increase = monthly_change_array[max_increase_index-1]
max_increase_month = month[max_increase_index]
#print(max_increase_month)
    #max decrease
max_decrease_index = monthly_change_array.index(min(monthly_change_array))+1
max_decrease = monthly_change_array[max_decrease_index-1]
max_decrease_month = month[max_decrease_index]
#print(max_decrease_month)

#other calculations
total_change = sum(monthly_change_array)
average_change = round((total_change/(month_count-1)),2)
#print(total_change)
#create output file
output_file = os.path.join(cwd,"analysis","output.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: "+str(month_count)])
    writer.writerow(["Total: $"+str(net_income)])
    writer.writerow(["Average Change: $"+str(average_change)])
    writer.writerow(["Greatest Increase in Profits: "+max_increase_month+" ($"+str(max_increase)+")"])
    writer.writerow(["Greatest Decrease in Profits: "+max_decrease_month+" ($"+str(max_decrease)+")"])
