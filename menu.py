from conexionNueva import Invernadero

class Menu:
	inv = Invernadero()
	def __init__(self):
		while True:
			print("1) Mostrar usuarios")
			print("2) Agregar usuarios")
			print("0) Salir")
			op = input()

			if op == "1":
				self.mostrar()
			elif op == "2":
				pass
			elif op == "0":
				break

	def mostrar(self):
		usuarios = self.inv.mostrar_usuario()
		for u in usuarios:
			print("{0:2} {1:10} {2:8} {3:8} {4:15} {5:6} {6:1}".format(u[0].u[1],u[2],u[3],u[4],u[5],u[6]))




'''
from conexionNueva import Invernadero

inv = Invernadero()
inv.mostrar_usuario()
'''