log_file = open("um-server-01.txt")

# create a function to print the sales of the selected day
def sales_reports(log_file):
   #looping over each line of data
    for line in log_file:
        line = line.rstrip()
        #assign the variable day to 
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
