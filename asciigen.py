from pyfiglet import Figlet
import os, sys

#clear layar
os.system('cls' if os.name=='nt' else 'clear')

aa = "\033[1;30m"
b = "\033[1;31m"
c = "\033[1;32m"
d = "\033[1;33m"
e = "\033[1;34m"
f = "\033[1;35m"
g = "\033[1;36m"
h = "\033[1;39m"

def font1():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='digital')
	print (aa)
	print (custom_fig.renderText(a))

def font2():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='3-d')
	print (b)
	print (custom_fig.renderText(a))

def font3():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='3x5')
	print (c)
	print (custom_fig.renderText(a))

def font4():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='4x4_offr')
	print (d)
	print (custom_fig.renderText(a))

def font5():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='5lineoblique')
	print (e)
	print (custom_fig.renderText(a))

def font6():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='5x7')
	print (f)
	print (custom_fig.renderText(a))

def font7():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='5x8')
	print (g)
	print (custom_fig.renderText(a))

def font8():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='a_zooloo')
	print (h)
	print (custom_fig.renderText(a))

def font9():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='acrobatic')
	print (c)
	print (custom_fig.renderText(a))

def font10():

	a = input("\033[1;30m[√]\033[1;32m Teks:\033[1;35m ")
	os.system('clear')
	custom_fig = Figlet(font='caligraphy')
	print (e)
	print (custom_fig.renderText(a))

if __name__ == "__main__":

	def menu():

		try:
			#banner
			os.system('cls' if os.name=='nt' else 'clear')
			print ("\033[1;35m	╔═╗┌─┐┌─┐┬┬  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐")
			print ("\033[1;30m	╠═╣└─┐│  ││  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘")
			print ("\033[1;32m	╩ ╩└─┘└─┘┴┴  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─")
			print ("\033[1;33m	 ASCII TEXT GENERATOR VERSI 1 BY KHAZUL ")

			#menu option

			print ("\n\033[1;35m[01]\033[1;34m Digital ")
			print ("\033[1;35m[02]\033[1;34m 3D ")
			print ("\033[1;35m[03]\033[1;34m 3x5 ")
			print ("\033[1;35m[04]\033[1;34m 4x4_offr ")
			print ("\033[1;35m[05]\033[1;34m 5lineoblique ")
			print ("\033[1;35m[06]\033[1;34m 5x7 ")
			print ("\033[1;35m[07]\033[1;34m 5x8 ")
			print ("\033[1;35m[08]\033[1;34m A_Zooloo ")
			print ("\033[1;35m[09]\033[1;34m Acrobatic ")
			print ("\033[1;35m[10]\033[1;34m Caligraphy ")
			pil = input("\n\033[1;36m[?]\033[1;33m Pilih: ")
			if pil == "1" or pil == "01":
				font1()
			elif pil =="2" or pil == "02":
				font2()
			elif pil == "3" or pil == "03":
				font3()
			elif pil == "4" or pil == "04":
				font4()
			elif pil == "5" or pil == "05":
				font5()
			elif pil == "6" or pil == "06":
				font6()
			elif pil == "7" or pil == "07":
				font7()
			elif pil == "8" or pil == "08":
				font8()
			elif pil == "9" or pil == "09":
				font9()
			elif pil == "10":
				font10()
		except KeyboardInterrupt:
			sys.exit()
	menu()

	try:

		while True:
			ul = input("\n\033[1;31m[?]\033[1;33m Mau ulang?(y/n)\033[1;35m ")
			if ul == "y":
				menu()
			if ul == "n":
				exit("\033[1;34mGoodbyee..")
	except:
		pass
