# This is template assignment 2
import sys,os
# sys supports the commandline arguments.
import sqlite3
# sqlite3 is used to establish a database for query

# Start of program logic: check wether a local db is present at the current folder
#for item in sys.argv:
#    print item

# get current directory path
cwd = os.getcwd()
print len(sys.argv), "arguments supplied."
# Running the script alone is not supported.
if (len(sys.argv) == 1):
    print "Running this script with no argument is not supported!"
    print " In order to work with this SCM, you need to use command such as"
    print " cwd:current working dir\ninfo:about this program\nstatus:system status of this directory\nlist:list all files under this directory(non-recursively)\n"
elif (len(sys.argv)==2):
    if (sys.argv[1] == "cwd"):
        print "your are executing", os.path.abspath(sys.argv[0]), "in", cwd
# Command type 1: argc = 2
# this.py info, status
    elif (sys.argv[1] == "info"):
        print "This is an SCM script for CSC444 assignment 2"
        print "The solution is provided by Ximeng Wang and Wenzhong Zhang"
    elif (sys.argv[1] == "status"):
        try:
            with open('myDB.db'):
                print "The directory is under SCM."
        except IOError:
            print 'The directory is not under SCM. Use add command to start'
    elif (sys.argv[1] == "list"):
        # get an array of filenames in files.
        files = os.listdir(cwd)
        print "The directory contains the following files:"
        for file in files:
            print " -",file
    else:
        print sys.argv[1], "(command not reconized)"
# Command type 2: argc = 3
# this.py 
elif (len(sys.argv) == 3):
    print "3 or more arg's: Currently under development."
    if (sys.argv[1] == "add"):
        try:
            with open('myDB.db'):
                print "Adding file",sys.argv[2],"to the SCM database"
        except IOError:
            print 'Creating database.'
            try:
                with open('myDB.db'):
                    print "Opearation succeeded. Adding file into the database."
            except IOError:
                # For now it would report error.
                print 'Database creation failed. Check if you have right to the directory', cwd
    elif (sys.argv[1] == "del"):
        print "delete file",sys.argv[2],"from database"
    else:
        print sys.argv[1],"is not supported."
else:
    if (sys.argv[1]=='add'):
        print "adding "
    elif (sys.argv[2]=='del'):
        print "deleting "
    else:
        print "not supported"



# Database object. Pending. 
def myDB(object):
    pass

