# political-donor-data-analysis
My implementation of the political donor data analysis exercise is in the file src/find_political_donors.py, written in the python language.

The path of the input and output file to write to are taken from the command line arguments. When the input file is opened for reading, reading continues until the line read in is '', signifying EOF.

For each line of the input file, if either one of:

1. the OTHER_ID field is empty,
2. the CMTE_ID field is empty, or
3. the transaction amount is empty,

the record is ignored, and reading moves onto the next line.

Otherwise, if the zipcode is greater than 5 characters long, CMTE_ID and the zipcode are used to create a dictionary key for a zip code dictionary, with the transaction amount being the associated value. Then, if the transaction date is not empty, the CMTE_ID and the transaction date, as a string, are used to create a dictionary key for a date dictionary, with the transaction amount being the associated value.

The zip code dictionary and the date dictionary are used to produced the required median values, by zip code and by date, for output.
