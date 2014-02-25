import sys
import string
import pandas

def mapper(input_file):
    
    with open(input_file, 'rb') as input_file:
        for line in input_file:
            line_split = line.strip().split(",")
            [x.strip() for x in line_split]
            if len(line_split) == 12 and line_split[0] != "Registrar":
                print "{0}\t{1}".format(line_split[3], line_split[8])
            

    #for line in aadhaar_data:

    #for line in sys.stdin: #cycle through lines of code
        
        #Your mapper code goes here.
        #You will also need to fill out the reducer
        #code as well before test running or else you will get an error.
        #
        #Each line will be
        #a comma-separated list of values.  The
        #header row WILL be included.  Tokenize
        #each row using the commas, and emit a key-
        #value pair containing the district and
        #Aadhaar generated, separated by a tab.
        #Make sure each row has the correct number
        #of tokens and is not the header row!
        #
        #You can see a copy of the the input aadhaar data
        #in the link below:
        #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
        
        #your code here
        
#mapper()

local_dir = "/Users/johnmorgan/datasci/unit5"
input_file = "%s/aadhaar_data.csv" % local_dir
mapper(input_file)

# Registrar
# Enrolment Agency
# State
# District
# Sub District
# Pin Code
# Gender
# Age
# Aadhaar generated
# Enrolment Rejected
# Residents providing email
# Residents providing mobile number