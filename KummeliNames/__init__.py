import logging
import azure.functions as func
import libraries.KummeliNamesLib as KummeliLib
import numbers

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    countStr = req.params.get('count')

    print(isinstance(countStr, numbers.Real))
    if not countStr:
        count = 1
    elif countStr.isdigit() == False:
        return func.HttpResponse(">:(", status_code=400)
    else:
        count = int(countStr)
    
    try:
        names_list = KummeliLib.getDefaultNamesList()

        result = KummeliLib.getNames(names_list=names_list, format="{0} {1}", count=count, allowDuplicates=None)
        resultStr = "\n".join(str(r) for r in result)
        return func.HttpResponse(resultStr)
    except:
        return func.HttpResponse("Is bork", status_code=500)
