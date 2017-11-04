# Insight Data Engineering programming challeng
# Xiao-Bo Li.
import sys # for redirecting standard out to file
import scipy as sp
'''
for arg in sys.argv:
	print arg
'''

f_by_zip  = file(sys.argv[2], 'w')
f_by_date = file(sys.argv[3], 'w')

f_in = open(sys.argv[1], 'r')

zipdict ={}
datedict ={}

#sys.stdout = open("output/medianvals_by_zip.txt", 'w') # print by zip info first
while True:
	line = f_in.readline()

	
	if line=='' or len(line)<1:
		break
	line = line.rstrip("\n")	
	line = line.split("|")
	#print "other ", line[15]
	#print "Len line[15] "+str(len(line[15]))
	cmte_id = line[0]
	other 	= line[15]
	tx_amt  = line[14]
	
	# Ignore current record if: OTHER_ID is not empty, or CMTE_ID is empty, or TRANSACTION_AMT is empty
	if not other =='' or cmte_id == '' or tx_amt == '': 
		continue
	
	
	tx_amt = float(tx_amt)
	

	if len(line[10])>=5: # zip code must be longer than 5 digits
		zipcode = line[10][0:5]
		zipkey = cmte_id+"-"+zipcode

		if not zipkey in zipdict:
			zipdict[zipkey]= [tx_amt]
		else:
			zipdict[zipkey].append(tx_amt)

		median_byzip = sum(zipdict[zipkey])/len(zipdict[zipkey])
		#print "zip key "+zipkey
		zipstring = cmte_id+"|"+zipcode+"|"+str(int(round(median_byzip)))+"|"+str(len(zipdict[zipkey]))+"|"+str(int(sum(zipdict[zipkey])))
		f_by_zip.write(zipstring+"\n")
		#print zipstring
		#print "by zip string: "+zipstring

	
	
	tx_date = line[13]

	if not tx_date=="": # date is required to be not empty
		datekey = cmte_id+"-"+tx_date
	

		if not datekey in datedict:
			datedict[datekey]= [tx_amt]
		else:
			datedict[datekey].append(tx_amt)
	
		#print "date key "+str(datekey)

	#print "other "+other+" cmte_id "+cmte_id+" tx_amt "+str(tx_amt)+ "tx_date "+tx_date
datekey_L=[] # keep date keys for sorting
for key in datedict:
	datekey_L.append(key)
# sorting keys will allow cmte_id's to be in alphabetical order, and date in chronological order
datekey_L.sort()

# Finished reading all files, now find median by date
#sys.stdout = open("output/medianvals_by_date.txt", 'w') # print to by date file
for datekey in datekey_L:
	datekeysplit = datekey.split("-")
	cmte_id = datekeysplit[0]
	tx_date = datekeysplit[1]
	median_bydate = sp.median(datedict[datekey])
	datestring = cmte_id+"|"+tx_date+"|"+str(int(round(median_bydate)))+"|"+str(len(datedict[datekey]))+"|"+str(int(sum(datedict[datekey])))

	#print "by date string: "+datestring+" datedict[datekey] "+str(datedict[datekey])

	f_by_date.write(datestring+"\n")
	#print datestring


#close input file
f_in.close()
# close output files
f_by_zip.close()
f_by_date.close()
