import csv
import json
import argparse
import random
import re
import sys

import libraries.KummeliNamesLib as KummeliLib

if __name__ == "__main__":
    # Declare command line arguments using argparse.
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="", help="Name of the file containing all possible names.")
    parser.add_argument("--output", type=str, default="", help="Name of the file containing the output. If file is not provided, result will be printed to console.")
    parser.add_argument("--count", type=int, default=1, help="Amount of names to be returned.")
    parser.add_argument("--format", type=str, default="FirstNameLastName", choices=["FirstNameLastName", "LastNameFirstName", "FirstName", "LastName"], help="Output name format.")
    parser.add_argument("--allowduplicates", action=argparse.BooleanOptionalAction, help="If flag is present output might contain duplicate values.")
    parser.add_argument("--prefix", type=str, default="", help="Prefix that will be added to start of every line.")
    parser.add_argument("--separator", type=str, default=" ", help="Separator will be added between first and last name.")
    parser.add_argument("--suffix", type=str, default="", help="Suffix will be added to end of every line.")
    args = parser.parse_args()
    
    # Default name list. This will be overwritten if --input argument is used.
    names_list = KummeliLib.getDefaultNamesList()
    
    # If input file is provided, read names and save them to names_list.
    if(args.input != ""):
        with open(args.input, 'r', encoding='UTF-8') as csv_file:
            reader = csv.reader(csv_file)
            names_list = []
            
            for row in reader:
                names_list.append(row)
        
    # Regex magic to escape '{' and '}' in prefix, suffix and separator
    args.prefix = re.sub("[{]", "{{", args.prefix)
    args.prefix = re.sub("[}]", "}}", args.prefix)
    args.suffix = re.sub("[{]", "{{", args.suffix)
    args.suffix = re.sub("[}]", "}}", args.suffix)
    args.separator = re.sub("[{]", "{{", args.separator)
    args.separator = re.sub("[}]", "}}", args.separator)
    
    # Set correct output format based on command line argument.
    if args.format == "LastNameFirstName":
        format = "{1}"+args.separator+"{0}"
    elif args.format == "FirstName":
        format = "{0}"
    elif args.format == "LastName":
        format = "{1}"
    else:
        format = "{0}"+args.separator+"{1}"
    
    format = args.prefix +  format + args.suffix
    
    outputList = KummeliLib.getNames(names_list=names_list, format=format, count=args.count, allowDuplicates=args.allowduplicates)
    
    # Print names if output filename was not provided. Otherwise write the results to file.
    if args.output == "":
        for name in outputList:
            print(name)
    elif args.output == "azure":
        sys.exit(outputList)
    else:
        with open(args.output, 'w') as output:
            for name in outputList:
                output.write(name)
                output.write("\n")
            output.close()