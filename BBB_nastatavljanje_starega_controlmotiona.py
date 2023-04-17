import subprocess
import time
import colorama
from colorama import Fore

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
pwd='temppwd'
cmd='ls'

for x in range(16):
	print(" ")
print(Fore.GREEN +"           to je avtomatska skripta za nastavljanje Beaglebone Black " + Fore.WHITE )
for x in range(6):
	print(" ")
input("                            press Enter to continue" + "\n" + "\n" + "\n" + "\n" + "\n" + "\n")
for x in range(10):
	print(" ")

print("         zapiši zadnje štiri številke serijske številke enote, primer:          ")
print("             FLOW-46P1-FS-2022-" + Fore.GREEN + "1250" + Fore.WHITE + "     ==>          XXXX=1250")
for x in range(10):
	print(" ")

while True:
	try:
		XXXX = int(input(Fore.GREEN + "XXXX (0-9999)=" + Fore.WHITE))
		print(" ")
		if(XXXX<0 or XXXX>9999):
			print(Fore.GREEN +"vrednost napačna, vpiši vrednost med 0 in 9999" + Fore.WHITE)
			print(" ")
		else:
			break
	except ValueError:
		print(Fore.GREEN +"vpiši število z številkami med 0-9999"+ Fore.WHITE)
		print(" ")
		continue
	
XXXX = str(XXXX)
if len(XXXX)<4:
    for x in range(4-len(XXXX)):
        XXXX= "0" + XXXX

bashCommand = []
bashCommand.append('echo {} | sudo -S {}'.format(pwd,cmd))
bashCommand.append("sudo apt-get update")
bashCommand.append("sudo apt install linux-headers-$(uname -r)")
bashCommand.append("git clone https://github.com/zevnikmatic/aten_driver.git")
bashCommand.append("make all -C aten_driver")
bashCommand.append("sudo xz aten_driver/pl2303.ko")
bashCommand.append("sudo cp aten_driver/pl2303.ko.xz /lib/modules/$(uname -r)/kernel/drivers/usb/serial")
bashCommand.append("sudo sed -i '4 apl2303' /etc/modules")
bashCommand.append("sudo sed -i 's/beaglebone/{}-beaglebone/g'  /etc/hostname".format(XXXX))
bashCommand.append("sudo apt install snapd -y")
bashCommand.append("sudo snap install core")
bashCommand.append("sudo snap install aten_driver/controlmotion_1.1.63_armhf.snap --dangerous --devmode")
bashCommand.append("sudo snap install aten_driver/controlmotion_1.1.63.4_armhf.snap --dangerous --devmode")
bashCommand.append("connmanctl config $(connmanctl services | grep Wired | awk -F' ' '{ print $3 }') ipv4 manual 172.25.128.4 255.255.255.240 172.25.128.1")
bashCommand.append("sudo rm aten_driver/controlmotion_1.1.63_armhf.snap")
bashCommand.append("sudo rm aten_driver/controlmotion_1.1.63.4_armhf.snap")
bashCommand.append("connmanctl config $(connmanctl services | grep Wired | awk -F' ' '{ print $3 }') --nameservers 8.8.8.8 172.25.128.1")
bashCommand.append("sudo sed -i 's/localhost/beaglebone/g' /etc/hosts")
bashCommand.append("sudo sed -i 's/beaglebone/{}-beaglebone/g' /etc/hosts".format(XXXX))
bashCommand.append("sudo reboot")

#subprocess.call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True, stdout=subprocess.PIPE)

for x in range(10):

	process = subprocess.Popen(bashCommand[x], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	y=0
	data = process.poll()
	while data != 0:
		if x>0:
			if len(bashCommand[x])>40:
				print("executing dommand: " + bashCommand[x][:35] + "...   ", end="")
			else:
				print("executing dommand: " + bashCommand[x] +  "   ", end="")
		if y==0:
			print("|")
			y=1
		elif y==1:
			print("/")
			y=2
		elif y==2:
			print("-")
			y=3
		elif y==3:
			print("\\")
			y=4
		elif y==4:
			print("|")
			y=5
		elif y==5:
			print("/")
			y=6
		elif y==6:
			print("-")
			y=7
		else:
			print("\\")
			y=0	
		time.sleep(1)
		print(LINE_UP + "\r", end=LINE_CLEAR)
		data = process.poll()
	
	if x>0:
		if len(bashCommand[x])>40:
			print(bashCommand[x][:35] +Fore.GREEN + "......complete" + Fore.WHITE)
		else:
			print(bashCommand[x] +Fore.GREEN + "......complete" + Fore.WHITE)
			
			
for x in range(10,12):
	process = subprocess.Popen(bashCommand[x], shell=True)
	data = process.poll()
	if len(bashCommand[x])>40:
		print("executing dommand in new: " + bashCommand[x][:35] + "...   ")
	else:
		print("executing dommand in new: " + bashCommand[x] +  "   ")
	while data != 0:
		time.sleep(1)
		data = process.poll()
	if x>0:
		if len(bashCommand[x])>40:
			print(bashCommand[x][:35] +Fore.GREEN + "......complete" + Fore.WHITE)
		else:
			print(bashCommand[x] +Fore.GREEN + "......complete" + Fore.WHITE)

print(" ")
print(" ")
print(Fore.GREEN +"              nastavi začetne parametre v first time config: ")
print(" ")
print(" ")
print(Fore.GREEN +"                 odpri link: http://192.168.7.2:3853/  ")
print(" ")
print(Fore.RED +"    pazi da ne pritisneš CTRL+C samo označi link in se avtomatsko kopira")
print(" ")
print(" ")
print(Fore.GREEN +"              ko končaš zapri browser in sledi novodilom")
time.sleep(10)

input(Fore.GREEN +"                         press ENTER to continue")
print(Fore.WHITE +" ")
print(" ")

for x in range (12,19):
	process = subprocess.Popen(bashCommand[x], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	y=0
	data = process.poll()
	while data != 0:
		if len(bashCommand[x])>40:
			print("executing dommand: " + bashCommand[x][:35] + "...   ", end="")	
		else:
			print("executing dommand: " + bashCommand[x] + "   ", end="")
		if y==0:
			print("|")
			y=1
		elif y==1:
			print("/")
			y=2
		elif y==2:
			print("-")
			y=3
		elif y==3:
			print("\\")
			y=4
		elif y==4:
			print("|")
			y=5
		elif y==5:
			print("/")
			y=6
		elif y==6:
			print("-")
			y=7
		else:
			print("\\")
			y=0	
		time.sleep(1)
		print(LINE_UP + "\r", end=LINE_CLEAR)
		data = process.poll()
	
	
	if x>0:
		if len(bashCommand[x])>40:
			print(bashCommand[x][:35] +Fore.GREEN + "......complete" + Fore.WHITE)
		else:
			print(bashCommand[x] +Fore.GREEN + "......complete" + Fore.WHITE)
			
process = subprocess.Popen(bashCommand[20], shell=True)

print(Fore.GREEN +"uspešo zaključno počakaj da se beaglebone resetira in preglej če vse dela kot mora" + Fore.WHITE)