###################################################
##Auteur : SAUTRON Dimitri
##Description : Creation d'un mot de passe complexe
##Version : 1.2.1
##Date de creation : 05/04/2020
##Date de la derniere mise a jour : 16/04/2020
##Fichier : Generation WordList
###################################################
# 
#
#
###################################################
import os
import random

def Systeme():
	Environnement = os.name
	if Environnement == 'nt':
		OS=str(input("Souhaitez-vous creer un autre mot de passe, oui ou non ? : "))
	elif Environnement == 'posix':
		OS=raw_input("Souhaitez-vous creer un autre mot de passe, oui ou non ? : ")
	else:
		print("Votre systeme n est pas pris en compte !")
	return OS
	
Caractere = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!@{}[]"
# Caractere=random.choice(Caractere)
print("Caractere Possible : "+Caractere)
def VerifChiffre():
	Number = 0
	while True:
		try:
			Number = int(input("Choissisez le nombre de caractere pour votre mot de passe (1 a 30) : "))
		except ErreurChiffre:
			print("Erreur, ce n'est pas un chiffre. Veuillez ressayer !")
		else:
			if Number >= 1 and Number <=30:
				return Number
			else:
				print("Erreur, ce n'est pas un chiffre, compris entre 1 et 30.")
		
def PassWord(TailleMDP,data):
	SortieMDP = ""
	for x in range(0,TailleMDP):
		SortieMDP+= str(random.choice(data))
	return SortieMDP


while True:
	ChoixTailleMDP = VerifChiffre()
	MDP = PassWord(ChoixTailleMDP,Caractere)
	print("password :"+ MDP)
	print("\n")
	Reponse = Systeme()
	if Reponse == "oui":
		print("On genere, un nouveau mot de passe")
	else:
		break