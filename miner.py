# -*- coding: utf-8 -*-

def miner(theString,inFile, outFile, screen=0, write="off"):
    """Function to search for the user string in the specified file and
       then log the found strings in the output file"""
    data = []
       
    try:
        for line in inFile:
            if line.find(theString) != -1:
                data.append(line)
                 
                if screen == 1:                
                    print line
                    
    except IOError as err:
        print err
        print "\n"
    
    for item in data:
        try:
            outFile.write(item)
            outFile.close
        except IOError as err:
            print "Ooops! Error: "+str(err)
    
