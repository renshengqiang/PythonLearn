#coding=utf-8
#!/usr/bin/python

#pip install
#	sudo apt-get purge python-pkg-resources
#	sudo apt-get -f install
#	sudo apt-get install python-pip
#pip install Crypto

import binascii
import sys
from Crypto.Cipher import AES

class prpcrypt():
	def __init__(self,key):
		self.key = self.length_adjust(key)
		self.mode = AES.MODE_CBC
		self.iv = "hi, i am pwdtool"#必须为16位或者16的整数倍,此处写死加解密函数不做判断
	
	#如果key大于16位则补为16的倍数
	def length_adjust(self, param):
		length = 16
		count = len(param)
		if count < length:
			add = length - count
			param = param + ('\0' * add)
		elif count > length:
			add = length - (count % length)
			param = param + ('\0' * add)
		return param

	#加密函数
	def encrypt(self,text):
		cryptor = AES.new(self.key, self.mode, self.iv)
		text = self.length_adjust(text)
		self.ciphertext = cryptor.encrypt(text)
		tmp = binascii.b2a_hex(self.ciphertext)
		return tmp

	#解密函数
	def decrypt(self,text):
		cryptor = AES.new(self.key, self.mode, self.iv)
		plain_text = cryptor.decrypt(binascii.a2b_hex(text))
		return plain_text.rstrip('\0')

if __name__ == '__main__':
	key_value = raw_input("please type your key: ")
	while 1:
		choise = raw_input("1: encrypt	2:decrypt	3: exit\n")
		pc = prpcrypt(key_value)
		if choise == '1':
			pwd = raw_input("Please type your passworld: ")
			encrypted = pc.encrypt(pwd)
			print "After Encrypt: ",encrypted
			continue
		if choise == '2':
			encrypted = raw_input("Please type your encrypted passworld: ")
			decrypted = pc.decrypt(encrypted)
			print "PWD is: ",decrypted
			continue
		if choise == '3':
			break

	


