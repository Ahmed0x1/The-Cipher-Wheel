#!/bin/python3

OutC = [['A', 'B', 'C', 'D', 'E'],# 0 -> 5
               #0    1    2    3    4
               ['F', 'G', 'H', 'I', 'J'],# 1 -> 5
               #0    1     2    3   4
               ['K', 'L', 'M', 'N', 'O'],# 2 ->5
               #0    1     2    3     4
               ['P', 'Q', 'R', 'S', 'T'],# 3 ->5
               #0    1     2    3    4
               ['U', 'V', 'W', 'X', 'Y']# 4 -> 5
               #0     1     2     3    4
               ]# 5 -> 1
               #0
               
InnC = [['A', 'B', 'C', 'D', 'E'],# 0 -> 5
               ['F', 'G', 'H', 'I', 'J'],# 1 -> 5
               ['K', 'L', 'M', 'N', 'O'],# 2 ->5
               ['P', 'Q', 'R', 'S', 'T'],# 3 ->5
               ['U', 'V', 'W', 'X', 'Y']# 4 -> 5
               ]# 5 -> 1

EndPoint = "Z"                
PointE = OutC[0][0]
SavSecuPoint = [PointE]
#		Prepare Functions For Encryption & Decryption functions
def indexSearchSecKey(K , arr):
	if isinstance(K , str):
		for i in range(len(arr)):
		    for j in range(len(arr[i])):
		    	if arr[i][j] == K:
				    return i , j
						    
	if isinstance(K , int):
		limit = 0
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				if K == limit:
					return arr[i][j]
				limit+=1
					
def checkKey(K):
		if K <= 25:
			if K == 25:
				SavSecuPoint.append(EndPoint)
				return SavSecuPoint
			else:
				SavSecuPoint.append(indexSearchSecKey(K , InnC))
				return SavSecuPoint

def ModifyArr(K , savPoint , arr):
	ModifyArrT = []
	StanderdArr = []
	limit = K
	Restof = 26 - limit
	St = 1
	sav = 0
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			#print(arr[i][j])
			if savPoint[1] == arr[i][j]:
				sav+=1
				ModifyArrT.append(arr[i][j])
				continue
				
			if savPoint[1] != arr[i][j] and sav == 0:
				StanderdArr.append(arr[i][j])
				
			if sav <= Restof and sav == 1:
				ModifyArrT.append(arr[i][j])
	#print(StanderdArr)	
	ModifyArrT.append('Z')
	for i in range(len(StanderdArr)):
		ModifyArrT.append(StanderdArr[i])
	return ModifyArrT

def StanderdArray(Arr):
	res = []
	for i in range(len(Arr)):
		for j in range(len(Arr[i])):
			res.append(Arr[i][j])
	res.append('Z')
	return res

def ArithSearchIndex(str1):
	lest = []
	lestNumberOfIndex = []
	stand = StanderdArray(InnC)
	stand.append('Z')
	for i in range(len(str1)):
		lest.append(str1[i])

	for le in range(len(lest)):
		for searchIndex in range(len(stand)):
			if lest[le] == stand[searchIndex]:
				lestNumberOfIndex.append(searchIndex)
			else:
				continue
	return lestNumberOfIndex

#		ENCRYPTION
def SCStr(str1 , K):
	lest = []
	for i in range(len(str1)):
		if str1[i] == " ":
			continue
		else:
			lest.append(str1[i])
	Encrypt = ""
	stand = StanderdArray(OutC)
	mod = ModifyArr(K , SavSecuPoint,OutC)
	for le in range(len(lest)):
		for st in range(len(stand)):
			for mo in range(len(mod)):
				if lest[le] == stand[st] and stand.index(stand[st]) == mod.index(mod[mo]):
					Encrypt += mod[mo]
				
	return Encrypt

def SCWithArithemtic(str1Arr , K):
	lest = []
	for i in range(len(str1Arr)):
		if str1Arr[i] == " ":
			continue
		else:
			lest.append(str1Arr[i])
	Encrypt = ""
	stand = StanderdArray(OutC)
	lestNum = ArithSearchIndex(lest)
	op = 0
	sav = []
	for i in range(len(lestNum)):
		op = K + lestNum[i]
		if op > 25:
			if op == 26:
				sav.append(op - 26)
			elif op > 26:
				sav.append(op - 26)
		else:
			sav.append(op)

	for j in range(len(sav)):
		for c in range(len(stand)):
			if sav[j] == c:
				Encrypt += stand[c]

	return Encrypt
#		DECRYPTION
def SDCStr(str1 , K):
	lest = []
	for i in range(len(str1)):
		if str1[i] == " ":
			continue
		else:
			lest.append(str1[i])
		
	Dencrypt = ""
	stand = StanderdArray(OutC)
	mod = ModifyArr(K , SavSecuPoint,OutC)
	for le in range(len(lest)):
		for mo in range(len(mod)):
			for st in range(len(stand)):
				if lest[le] == mod[st] and stand.index(stand[st]) == mod.index(mod[mo]):
					Dencrypt += stand[st]
				
	return Dencrypt

def SDCWithArithemtic(str1Arr , K):#in Fix
	lest = []
	for i in range(len(str1Arr)):
		if str1Arr[i] == " ":
			continue
		else:
			lest.append(str1Arr[i])
		
	Dencrypt = ""
	stand = StanderdArray(OutC)
	lestNum = ArithSearchIndex(lest)
	op = 0
	sav = []
	for i in range(len(lestNum)):
		op = lestNum[i] - K
		if op >= 0:
			sav.append(stand[op])
		if op < 0:
			op = op + 26
			sav.append(stand[op])
			
	for j in range(len(sav)):
		Dencrypt += sav[j]
	return Dencrypt
#		STRUCTER FLOW 
def theMainList():
	print("[1] Encrypt Message (The Cipher Wheel)")
	print("[2] Decrypt Message (The Cipher Wheel)")
	print("[3] Encrypt Message (The Cipher Wheel With Arithmetic)")
	print("[4] Decrypt Message (The Cipher Wheel With Arithmetic)")
	print("[5] Exit")
	try:
		cho = int(input("choice: "))
		if isinstance(cho , int) or cho <= 4 and cho >= 1:
			return cho
	except:
		print("Error in your choice please, Don't enter string letters, Enter Integer number only..\n")
		theMainList()

def ifErr():
	while(True):
		con = theMainList()
		if con == 1:
			encryptFlow()
		elif con == 2:
			decryptFlow()
		elif con == 3:
			encryptWithArithemticFlow()
		elif con == 4:
			decryptWithArithemticFlow()
		elif con == 5:
			exit()
		else:
			print("Error in your choice please,s Choice another one between 1 to 3.\n")
			ifErr()

def decryptWithArithemticFlow():
	try:
		Key = int(input("Enter Security Key(0 to 25): "))
		if isinstance(Key , int) and Key >= 0 and Key <= 25 :
			writeM = str(input("Enter your message for decryption: "))
			print("\nYour Message Has Been Encrypted:-> " , SDCWithArithemtic(writeM.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def encryptWithArithemticFlow():
	try:
		Key = int(input("Enter Security Key(0 to 25): "))
		if isinstance(Key , int) and Key >= 0 and Key <= 25 :
			writeM = str(input("Enter your message for encryption: "))
			print("\nYour Message Has Been Encrypted:-> " , SCWithArithemtic(writeM.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def decryptFlow():
	try:
		Message = str(input("Enter The Encrypted Message: "))
		Key = int(input("Enter Message Security Key(0 to 25): "))
		if isinstance(Key , int):
			print("Security Key: " ,checkKey(Key) )
			print(ModifyArr(Key , SavSecuPoint,OutC))
			print("\nYour Message Has Been Decrypted:-> " , SDCStr(Message.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def encryptFlow():
	try:
		Key = int(input("Enter Security Key(0 to 25): "))
		if isinstance(Key , int) and Key >= 0 and Key <= 25 :
			print("Security Key: " ,checkKey(Key) )
			print(ModifyArr(Key , SavSecuPoint,OutC))
			writeM = str(input("Enter your message for encryption: "))
			print("\nYour Message Has Been Encrypted:-> " , SCStr(writeM.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def main():
	print("-----------------------------------------------------------------------------------")
	print("-----------------------------THE CIPHER WHEEL PROGRAME-----------------------------")
	print("Letters: " , StanderdArray(OutC) , " :Your Wheel")
	print("-----------------------------------------------------------------------------------")
	UsActive = input("Enter Y/y To Start (OR N/n To Exit):")
	#             START PROGRAM
	if UsActive == "Y" or UsActive == "y" or UsActive == "yes" or UsActive == "YES" or UsActive == "Yes" or UsActive == "yES" or UsActive == "yEs" or UsActive == "yeS":
		while(True):
			con = theMainList()
			if con == 1:
				encryptFlow()
			elif con == 2:
				decryptFlow()
			elif con == 3:
				encryptWithArithemticFlow()
			elif con == 4:
				decryptWithArithemticFlow()
			elif con == 5:
				exit()
			
		
	#             END PROGRAM
	elif UsActive == "N" or UsActive == "n" or UsActive == "no" or UsActive == "NO" or UsActive == "No"or UsActive == "nO":
		exit()
	
	else:
		print("Please Enter Y/y Or N/n To Know What You Want?.\n")
		main()


main()
