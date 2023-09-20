import logging
import azure.functions as func
import KummeliNamesList as Kummeli
import numbers

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    countStr = req.params.get('count')
    formatStr = req.params.get('format')

    print(isinstance(countStr, numbers.Real))
    if not countStr:
        count = 1
    elif countStr.isdigit() == False:
        return func.HttpResponse(">:(", status_code=400)
    else:
        count = int(countStr)

    if not formatStr:
        formatStr = "FirstNameLastName"

    if formatStr == "FirstNameLastName":
        format = "{0} {1}"
    elif formatStr == "LastNameFirstName":
        format = "{1} {0}"
    elif formatStr == "FirstName":
        format = "{0}"
    elif formatStr == "LastName":
        format = "{1}"
    else:
        error = ">:( Invalid format name. Supported formats are: FirstNameLastName, LastNameFirstName, FirstName, LastName"
        return func.HttpResponse(error, status_code=400)
    
    try:
        names_list = Kummeli.getDefaultNamesList()

        result = Kummeli.getNames(names_list=names_list, format=format, count=count, allowDuplicates=None)
        resultStr = "\n".join(str(r) for r in result)
        return func.HttpResponse(resultStr)
    except:
        return func.HttpResponse("Is bork", status_code=500)
