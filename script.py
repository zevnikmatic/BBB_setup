import subprocess
import time

print(" ")
print(" ")
print(" ")
print("   to je avtomatska skripta za nastavljanje Beaglebone Black za projekt Skyss    				  FLOW-15L1-WM-2022              				                     					  avtor: Matic Zevnik")
time.sleep(1)
print(" ")
print(" ")

print("zapiši zadnje štiri številke serijske številke enote primer:")
print("FLOW-15L1-WM-2022-1250 ==>  XXXX=1250")

while True:
	try:
		XXXX = int(input("XXXX (1250-1321)="))
		if(XXXX<1250 or XXXX>1321):
			print("vrednost napačna, vpiši vrednost med 1250 in 1321")
		else:
			break
	except ValueError:
		print("dej ne se zajebavat pa vpiš številko(1250-1321)")
		continue

YYY = XXXX - 1122

XXXX = str(XXXX)
YYY= str(YYY)
bashCommand = []
bashCommand.append("sudo apt-get update")
bashCommand.append("sudo apt install linux-headers-$(uname -r)")
bashCommand.append("git clone https://github.com/zevnikmatic/aten_driver.git")
bashCommand.append("make all -C aten_driver")
bashCommand.append("sudo xz aten_driver/pl2303.ko")
bashCommand.append("sudo cp aten_driver/pl2303.ko.xz /lib/modules/$(uname -r)/kernel/drivers/usb/serial")
bashCommand.append("sudo sed -i '4 apl2303' /etc/modules")
bashCommand.append("sudo apt install snapd -y")
bashCommand.append("sudo snap install core")
bashCommand.append("wget https://control.infinitus-outdoor.com/Drivers/controlmotion_1.1.63_armhf.snap")
bashCommand.append("sudo snap install controlmotion_1.1.63_armhf.snap --dangerous --devmode")
bashCommand.append("connmanctl config $(connmanctl services | grep Wired | awk -F' ' '{ print $3 }') ipv4 manual 10.188."+str(YYY)+".4 255.255.255.0 10.188."+str(YYY)+".1")
bashCommand.append("sudo sed -i 's/beaglebone/{}-beaglebone/g'  /etc/hostname".format(XXXX))
bashCommand.append("sudo sed -i 's/localhost/beaglebone/g' /etc/hosts")
bashCommand.append("sudo sed -i 's/beaglebone/{}-beaglebone/g' /etc/hosts".format(XXXX))
bashCommand.append("connmanctl config $(connmanctl services | grep Wired | awk -F' ' '{ print $3 }') --nameservers 10.224.9.10 10.224.9.11")
bashCommand.append("sudo timedatectl set-timezone Europe/Oslo")
bashCommand.append("sudo reboot")


for x in range(19):
	print(bashCommand[x])
	subprocess.call(bashCommand[x],shell=True)
