import random
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