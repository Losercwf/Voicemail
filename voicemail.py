#
#ITP 125 voicemail final project
#Nov 30 2014
#
import sys
import getopt
import urllib
import os

def handleNumber(phoneNum):
	phoneNum =  filter(str.isdigit, phoneNum)
	return phoneNum

#create a list including all file names of required files
def selectfile(gender,phoneNum,reason,ending):
	fileList = []
	#reason
	for ri in reason:
		fileList.append(reasonLib(gender,ri) + '.mp3')
	#number
	for ni in phoneNum:
		fileList.append(ni + '.mp3')
	#ending
	for ei in ending:
		fileList.append(endingLib(gender,ei) + '.mp3')
	return fileList



#return proper reason file name according to the reason code number
def reasonLib(gender,reasonCode):
	if gender=='m':
		if reasonCode=='0':
			return 'm-r0-cannot_come_to_phone'
		elif reasonCode=='1':
			return 'm-r1-building'
		elif reasonCode=='2':
			return 'm-r2-cracking_walnuts'
		elif reasonCode=='3':
			return 'm-r3-polishing_monocole'
		elif reasonCode=='4':
			return 'm-r4-ripping_weights'

	if gender=='f':
		if reasonCode=='0':
			return 'f-r0.1-unable_to_take_call'
		elif reasonCode=='1':
			return 'f-r0.2-she_is_busy'
		elif reasonCode=='2':
			return 'f-r1-ingesting_old_spice'
		elif reasonCode=='3':
			return 'f-r2-listening_to_reading'
		elif reasonCode=='4':
			return 'f-r3-lobster_dinner'
		elif reasonCode=='5':
			return 'f-r4-moon_kiss'
		elif reasonCode=='6':
			return 'f-r5-riding_a_horse'



#return proper ending file name according to the ending code number
def endingLib(gender,endingCode):
	if gender=='m':
		if endingCode=='1':
			return 'm-e1-horse'
		elif endingCode=='2':
			return 'm-e2-jingle'
		elif endingCode=='3':
			return 'm-e3-on_phone'
		elif endingCode=='4':
			return 'm-e4-swan_dive'
		elif endingCode=='5':
			return 'm-e5-voicemail'

	if gender=='f':
		if 	endingCode=='1':
			return 'f-e1-she_will_get_back_to_you'
		elif endingCode=='2':
			return 'f-e2-thanks_for_calling'


#output a textfile including the sequence of options and mp3 files
def outputTofile(gender,originalNum,fileList):
	if gender == 'm':
		outputline = 'male '
	elif gender == 'f':
		outputline = 'female'

	outputline += originalNum
	outputline += ' '
	outputline += ' '.join(fileList)
	outputfile = open('output.txt','w')
	outputfile.write(outputline) 

#download mp3 files in the filelist
def downloadMp3(fileList):
	for i in fileList:
		urllib.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + i , i)

#combine mp3 file
def combineMp3(fileList, outputmp3):
	#get system platform: win32/linux2/darwin
	if sys.platform=='win32':
		command = 'copy /b '
		command += '+'.join(fileList)
		command += ' '
		command += outputmp3
		os.system(command)
		for i in fileList:
			os.system('del ' + i)
	elif sys.platform=='linux2' or sys.platform=='darwin':  
		command = 'cat '
		command += ' '.join(fileList)
		command += ' > '
		command += outputmp3
		os.system(command)
		for i in fileList:
			os.system('rm ' + i)
	else:
		print 'Operating system is not supported'
		return

	


#display the list of reasons
def reasonChoice(gender):
	if gender=='m':
		reasonNumList = ['0','1','2','3','4']
	elif gender=='f':
		reasonNumList = ['0','1','2','3','4','5','6']
	
	reasonList = ['Possible Choices for Reason:']
	for i in reasonNumList:
		reasonList.append('[' + i + '] ' + reasonLib(gender,i))
	return reasonList

#display the list of endings
def endingChoice(gender):
	if gender=='m':
		endingNumList = ['1','2','3','4','5']
	elif gender=='f':
		endingNumList = ['1','2']
	
	endingList = ['Possible Choices for Ending:']
	for i in endingNumList:
		endingList.append('[' + i + '] ' + endingLib(gender,i))
	return endingList	

#check if the gender input is valid
def checkgender(gender):
	if gender!='m' and gender!='f':
		print 'Gender is not correct'
		return False
	else:
		return True

def checknumber(phoneNum):
	if len(phoneNum)!=10:
		print 'Phone number is not correct'
		return False
	else:
		return True

def checkreason(gender,reason):
	if gender=='m':
		reasonNumList = ['0','1','2','3','4']
	elif gender=='f':
		reasonNumList = ['0','1','2','3','4','5','6']

	for m in reason:
		for n in reasonNumList:
			if m==n:
				return True

	print 'Reason Code is not correct'
	return False 

def checkending(gender,ending):
	if gender=='m':
		endingNumList = ['1','2','3','4','5']
	elif gender=='f':
		endingNumList = ['1','2']

	for m in ending:
		for n in endingNumList:
			if m==n:
				return True
	
	print 'Ending Code is not correct'
	return False

def main():
	gender = None
	phoneNum = None
	reason = None
	ending = None
	outputmp3 = None

	#user input mode
	if not len(sys.argv)>1:

		confirm=False
		while confirm==False:
			while True:
				gender = raw_input('Male of Female?  (m/f)')
				if checkgender(gender):
					break

			while True:
				phoneNum = raw_input('Phone number?')
				originalNum = phoneNum
				phoneNum = handleNumber(originalNum)
				if checknumber(phoneNum):
					break

			while True:
				reason = raw_input('\n'.join(reasonChoice(gender)) + '\n')
				if checkreason(gender,reason):
					break	
		
			while True:
				ending = raw_input('\n'.join(endingChoice(gender)) + '\n')
				if checkending(gender,ending):
					break
		
			print 'Your gender: ' + gender
			print 'Your number: ' + originalNum
			print 'Your reason(s): ' + reason
			print 'Your ending(s): '  + ending

			while True:
				confirmChoice = raw_input('Confirm? (y/n)')
				if confirmChoice=='y':
					confirm=True
					break
				elif confirmChoice=='n':
					confirm=False
					break
				else:
					print 'Wrong input'

		outputmp3 = raw_input('Output file name: ')

	else:
		#command line mode
		#readin all flags and assign values to variables
		opts, args = getopt.getopt(sys.argv[1:],'g:n:r:e:o:')
		for o,a in opts:
			if o == "-g":
				gender = a
			elif o == "-n":
				phoneNum = a
			elif o == "-r":
				reason = a
			elif o == "-e":
				ending = a
			elif o == "-o":
				outputmp3 = a

		originalNum = phoneNum
		phoneNum = handleNumber(originalNum)
		if checkgender(gender)==False or checknumber(phoneNum)==False or checkreason(gender,reason)==False or checkending(gender,ending) ==False:
			sys.exit()


	fileList=selectfile(gender,phoneNum,reason,ending)
	outputTofile(gender,originalNum,fileList)
	downloadMp3(fileList)
	combineMp3(fileList,outputmp3)

if __name__ == "__main__":
	main()

