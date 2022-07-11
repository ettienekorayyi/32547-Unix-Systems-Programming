#!/usr/bin/env python3

"""
Title: Assignment UNIX Systems Programming
Author: Stephen Melben Corral

Limitation of the filter_by_time :
- The filter_by_time function only evaluates the time. The day part is not evaluated.
"""

import sys
import re
import os


option_a = "-a"
option_u = "-u"
option_t = "-t"
option_v = "-v"


def open_file() :
    try:
        file = open(file_arg,mode="r")
        return file 
    except IndexError:
        print("The argument for the specified option is invalid.")
    except FileNotFoundError:
        print("The file is not found. Please try again...")
    except PermissionError:
        print("The file has no read permission.")
    except ValueError:
        print("No file has been opened.")


def read_file(options, args) :
    file = open_file()
    
    if options == option_a:
        print_all(file)
    elif options == option_u:
        find_user(args,file)
    elif options == option_t:
        filter_by_time(args,file)
    elif options == option_v:
        print_student_details()
    elif options != option_a and options != option_u and options != option_t and options != option_v:
        print("Wrong option") 
    else:
        print("Unexpected Error Detected. Please contact the developer.") 
    

def print_all(file):
    if os.path.getsize(file_arg) > 5:
        for line in file:
            line = line.rstrip('\n')

            if len(line) > 0:
                command = re.split(",", line)
                print(command[-1])
    else:
        print("No crontab commands")


def find_user(args,file):
    matched = []

    for line in file:
        line = line.rstrip('\n')
        username = re.split(",", line)
    
        if re.match(args, username[-2]):
            matched.append(line)
        else:
            continue
    
    if len(matched) != 0: 
        for line in matched:
            line = line.rstrip('\n')
            username = re.split(",", line)
            print(line)
    else:
        print("No crontab lines for user %s"%(args))
        
def filter_by_time(args,file):
    if os.path.getsize(file_arg) > 0:
        for line in file:
            line = line.rstrip('\n')
            time = re.split(":", args)
            time_per_line = re.split(",", line)
            
            if int(time_per_line[2]) >= int(time[2]) :
                print(line)
            
    else:
        print("No crontab lines on or after time")
    

def print_student_details():
    student_name = "Stephen Melben Corral"
    student_id = 14394302
    completion_date = "08/05/2022"

    print(f"Student Name: {student_name}")
    print(f"Student ID: {student_id}")
    print(f"Completion Date: {completion_date}")

try:
    options_args = sys.argv[1]
    file_arg = sys.argv[2] if options_args == option_a or options_args == option_v else sys.argv[3] 
    option_input = sys.argv[2] if options_args == option_u or options_args == option_t else None

    read_file(options_args, option_input)
except IndexError:
    print("User Argument Input Error Please enter the correct parameters.")
