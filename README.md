
Logminer is simple tool for searching for a string in a textfile and writing out results into a separate output file written in python 2.x.
Well, from a Linux terminal this can be achieved from a single line command but while trying out the Eudyptula Challenge I realized 
I was checking the /var/log/syslog file now and then, running such a command....

#cat /var/log/syslog | grep -i hello_world >> hello.log

Who likes repeating things in Linux? So I wrote a simple python script for that. Then, why not make it fancy and share it with the world? 
At least I'll make use of git in that case and maybe make the tool better | better* >> *better*


The script accepts at-least one option i.e a string to search in a file (/var/log/syslog by default). 
To print the results on the screen, set verbose mode to true -v 1 (it's false by default). 
Specify an out-put file of results with -o (/data/logminer.log by default).


==============================
   Log Miner (version 1.0)
============================== 

Usage: logminer -s <search string> -i <input-file> -o <output file> -v <1 verbose, 0 silent>

Options:
  -h, --help     show help message and exit
  -i INPUTFILE   specify File to open (/var/log/syslog)
  -s STRINGX     specify string to search
  -o OUTPUTFILE  specify output file (optional)
  -v VERBOSITY   1 for verbose, 0 for silent (optional)


---------------------------------
Additional Support (contributor?)

Support regex search
Output xml/json data
Model a OOP version
Build GUI for mouse pushers
version a py3k version
implement a threaded search for huge files





