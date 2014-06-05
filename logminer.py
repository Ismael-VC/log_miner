#!/usr/bin/env python
# coding: utf-8


# works with python 2 & 3

"""
@authors: John O. Troon, Ismael Venegas C.
@email: ombagi <at> promaxted.com
@blog: www.promaxted.com
@name: logminer
@version: 1.1
@about:  Simple script to check for strings in a file and dump results
         in a log file.
@usage: checker -s <search string> -i <input-file> -o <output file>
                -v <1 for verbose, 0 for silent>
"""


from __future__ import print_function
from textwrap import dedent as dd

import optparse
import sys


def main():
    """
    The main function that accepts and sanitize the input options from the
    user and then calls the check function
    """
    banner = dd("""\
                ===============================
                    Log Miner (version 1.1)
                ===============================""")
    print(banner)

    parser = optparse.OptionParser("%prog -s <search string> -i <input-file>"
                                   " -o <output file> -v <1 verbose, 0 silent>")

    parser.add_option('-i', dest='inputFile',
                            type='string',
                            help='specify File to open (/var/log/syslog)')

    parser.add_option('-s', dest='stringx',
                            type='string',
                            help='specify string to search')

    parser.add_option('-o', dest='outputFile',
                            type='string',
                            help='specify output file (optional)')

    parser.add_option('-v', dest='verbosity',
                            type='int',
                            help='1 for verbose, 0 for silent (optional)')

    options, args = parser.parse_args()

    inputFile = options.inputFile
    stringx = options.stringx
    outputFile = options.outputFile
    screen = options.verbosity

    if not inputFile:
        inputFile = "/var/log/syslog" # doesn't work with systemd
    print("[+] Loading.. %s" % inputFile)

    if not outputFile:
        outputFile = "data/dump.log"

    if not stringx:
        print("[-] Nothing to do! Use -h or --help for help")
        exit(0)

    try:
        with open(inputFile) as inFile: # 'r' is default
            with open(outputFile, 'a') as outFile:
                if screen:
                    miner(stringx, inFile, outFile, screen=screen)
                else:
                    miner(stringx, inFile, outFile)
    except IOError as e:
        # print to standard error stream
        print('[!] ERROR: {0}'.format(e), file=sys.stderr)


def miner(theString, inFile, outFile, screen=0): # write="off" was not used
    """
    Function to search for the user string in the specified file and
    then log the found strings in the output file
    """
    data = list()

    for line in inFile:
        if line.find(theString) != -1:
            data.append(line)
            if screen == 1:
                # why does it adds a extra newline, without the end=''? :S
                print(line, end='')

    for item in data:
        outFile.write(item)


if __name__ == '__main__':
     main()
