#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: John O. Troon
@email: ombagi <at> promaxted.com
@blog: www.promaxted.com
@name: logminer 
@version: 1.0
@about:  Simple script to check for strings in a file and dump results in a log file.
@usage: checker -s <search string> -i <input-file> -o <output file> -v <1 for verbose, 0 for silent>
"""

import optparse
from miner import *


def main():
    print "=============================="
    print "   Log Miner (version 1.0)   "
    print "==============================\n"
    """The main function that accepts and sanitize the input options from the user and then calls the check function"""
    parser = optparse.OptionParser("%prog "+"-s <search string> -i <input-file> -o <output file> -v <1 verbose, 0 silent>")
    parser.add_option('-i', dest='inputFile', type='string',help='specify File to open (/var/log/syslog)')
    parser.add_option('-s', dest='stringx', type='string', help='specify string to search')
    parser.add_option('-o', dest='outputFile', type='string', help='specify output file (optional)')
    parser.add_option('-v', dest='verbosity', type='int', help='1 for verbose, 0 for silent (optional)')

    (options, args) = parser.parse_args()
    
    inputFile = options.inputFile
    stringx = options.stringx
    outputFile = options.outputFile
    screen = options.verbosity
    
    if (inputFile == None):
        print "Loading.. /var/log/syslog"
        inputFile = "/var/log/syslog"
        
    if (outputFile == None):
            outputFile = "data/dump.log"
    
    if (stringx == None):
        print "[-] Nothing to do! Use -h or --help for help \n"
        exit(0)
        
    try:
        inFile = open( inputFile, 'r')
        outFile = open( outputFile, 'a')
            
        if screen == 1:
            miner(stringx,inFile, outFile, 1)
            
        else:
            miner(stringx,inFile, outFile)
            
    except Exception as err:
        print err
        print "\n"
        
if __name__ == '__main__': 
     main()
     """ instantiate the main function upon run"""
