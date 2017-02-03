import requests as re #importing requests for making get calls to web API
import time

#Intialising a list to store unique IPs
IPs = []

#Input File
inputFile = 'ip_raw.csv'

#Output File
outputFile = 'final_ip2.csv'

#Opening the input file to read and output file to write
with open(outputFile, 'wb') as outfile, open(inputFile, 'r') as infile:
	for line in infile:
		ip = line.strip() #Removing the spaces
		#Checking whether the IP is previously checked or not
		if ip not in IPs:
			#Storing the IP in the unique IP list
			IPs.append(ip)
			#Try-Catch error in case of API failure
			try:
				#Fetching the info from API and 
				resp = re.get('http://ip-api.com/json/'+ip).json()
				if resp['status'] == 'success':
					#Writing the result in file in case of success
					outfile.write(','.join([resp['query'],resp['country'],resp['city'],resp['regionName'],resp['query']])+'\n')
					print 'success'
					time.sleep(4)
				else:
					outfile.write(','.join(["Invalid IP","Invalid IP",ip])+'\n')
			except:
				print 'API call failed'
				print ip
print 'Number of unique IP look-ups: '+ str(len(IPs))