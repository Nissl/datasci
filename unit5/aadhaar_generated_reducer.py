import sys
def reducer():

    word_count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        this_key, count = data
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, word_count)
            word_count = 0

        old_key = this_key
        word_count += float(count)

    if old_key != None:
        print "{0}\t{1}".format(old_key, word_count)

    #Cycle through the list of key-value pairs emitted
    #by your mapper, and print out each key once,
    #along with the total number of Aadhaar generated,
    #separated by a tab.  Assume that the list of key-
    #value pairs will be ordered by key.  Make sure
    #each key-value pair is formatted correctly!
    #Here's a sample final key-value pair: "Gujarat\t5.0"
    
    # your code here
    
reducer()