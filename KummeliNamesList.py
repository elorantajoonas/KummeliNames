import csv
import argparse
import random
import re
import sys

def getDefaultNamesList():
    names_list = [['Matti', 'Näsä'], ['Sakari', 'Östermalm'], ['Pertti', 'Keinonen'], ['Mauno', 'Ahonen'], ['Pertti', 'Pasanen'], ['Harri', 'Soikkeli'], ['Esko', 'Mörkö'], ['Kalervo', 'Jankko'], ['Juha', 'Koistinen'], ['Eero', 'Kakko'], ['Ari', 'Zwang'], ['Patrik', 'Sjöberg'], ['Aas', 'Weckström'], ['Reino', 'Kinnula'], ['Rauno', 'Kinnula'], ['Markku', 'Lindell'], ['Martti', 'Meikäläinen'], ['Aimo', 'Nivaska'], ['B.B.', 'Korhonen'], ['Timo', 'Silakka'], ['Raimo', 'Vormisto'], ['Erik', 'Loka'], ['Rauno', 'Mäkynen'], ['Jaakko', 'Parantainen'], ['Hessu', 'Mälli'], ['JukkaEmil', 'Vanaja'], ['Volmari', 'Kuulapää'], ['Walton', 'Strömber'], ['Johan', 'Lind'], ['Iso', 'Pebe'], ['Pikku', 'Henry'], ['Arttu', 'Puukko'], ['Raimo', 'Helminen'], ['Mönkijä', 'Jätkä'], ['Kumi', 'Keijo'], ['Niko', 'Ström'], ['Roy Elvis', 'Jaatinen'], ['Carlos', 'Santana'], ['Pertti', 'Järvelä'], ['Pasi', 'Jaatinen'], ['Anssi', 'Suutarinen'], ['Maija', 'Karvinen'], ['Janne-Petteri', 'Broman'], ['Elmeri', 'Hautamäki'], ['Mr.', 'Beginning'], ['Jönssi', 'Kagelberg'], ['Dille', 'Kagelberg'], ['Kyrpä-Jooseppi', 'Hautamäki'], ['Pentti', 'Köyri'], ['Jari','Avanto'], ['Pasi', 'Veinä'], ['Seppo', 'Sillantaus'], ['Pertti', 'Mela']]
    return names_list

def getNames(names_list: any, format: str, count: int, allowDuplicates: any):
    i = 0
    outputList = []
    
    # Get random names from input list.
    while i < count:
    
        # Input list doesn't contain anymore names. We can break the loop.
        if len(names_list) == 0:
            break
            
        # Get random name from list and save it to Output list
        r = random.randint(0, len(names_list)-1)
        try:
            name = format.format(names_list[r][0],names_list[r][1])
            outputList.append(name)
            
            # Remove picked name from list if allowduplicates flag was not provided.
            if allowDuplicates != True:
                names_list.pop(r)
            i += 1
        
        except:
            error = "\n*********************\n"
            error +="ERROR >:(\n"
            error +="Parsing row: {0} failed!\n"
            error +="Format was: {1}.\n"
            error +="*********************\n"
            print(error.format(names_list[r], format))
            sys.exit(1)

    return(outputList)

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
    names_list = getDefaultNamesList()
    
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
    
    outputList = getNames(names_list=names_list, format=format, count=args.count, allowDuplicates=args.allowduplicates)
    
    # Print names if output filename was not provided. Otherwise write the results to file.
    if args.output == "":
        for name in outputList:
            print(name)
    else:
        with open(args.output, 'w') as output:
            for name in outputList:
                output.write(name)
                output.write("\n")
            output.close()