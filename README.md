# KummeliNames
Small Python script for getting list of random Kummeli character names 

Use --help flag to display available command line arguments. Currently available commands are:

| Parameter             | Description                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------|
| -h, --help            | Show this help message and exit.                                                                         |
| --input INPUT         | Name of the file containing all possible names. If parameter is not provided, default list will be used. |
| --output OUTPUT       | Name of the file containing the output. If file is not provided, result will be printed to console.      |
| --count COUNT         | Amount of names to be returned.                                                                          |
| --format FORMAT       | Output name format. Supported formats are: FirstNameLastName,LastNameFirstName,FirstName,LastName.       |
| --allowduplicates     | If flag is present output might contain duplicate values.                                                |
| --prefix PREFIX       | Prefix that will be added to start of every line.                                                        |
| --separator SEPARATOR | Separator will be added between first and last name.                                                     |
| --suffix SUFFIX       | Suffix will be added to end of every line.                                                               |
