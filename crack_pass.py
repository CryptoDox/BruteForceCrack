#!/usr/bin/env python
# crack_pass : De-chiffre le hash d'un mot de passe
# -*- coding: utf-8 -*-

# This file is part of Brute-Force-Crack with Python3
# See wiki doc for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "CodeKiller"
__date__ =  "11 juin 2020"

import hashlib
import argparse
import time

"""
Le moyen le plus simple pour cracker un mote de passe
c'est de le hacher menu, puis de le comparer
"""

__version__ = "1.0.0 Beta"

start_time = time.time()

def check_password(hash, password):
	if(hashlib.sha256(bytes(password, 'utf-8')).hexdigest().upper()==hash.upper()):
		print("MOT DE PASSE : "+password)
		elapsed_time = time.time() - start_time
		print("Durée de l'attaque : "+str(elapsed_time)+" secondes.")
		quit()

def count_print(i):
	i=i+1
	if(i%1000000==0):
		print("# "+str(i)+" combinaisons testé.")
	return i


### BEGIN BRUTE FORCE ATTACK

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def bruteforce_length(hash, init_password, target_length, current_length, i):
	if(current_length==target_length):
		i = count_print(i)
		check_password(hash, init_password)
	else:
		for c in chars:
			i = bruteforce_length(hash, init_password+c, target_length, current_length+1, i)
	return i

def bruteforce_attack(hash, max_length):
	i=0
	for l in range(1,max_length+1):
		i = bruteforce_length(hash, "", l, 0, i)

### END BRUTE FORCE ATTACK

### BEGIN SIMPLE DICTIONARY ATTACK

def dictionary_attack(hash, dict_filename):
	i=0
	with open(dict_filename) as f:
		for line in f:
			i = count_print(i)
			password = line.rstrip()
			check_password(hash, password)

### END SIMPLE DICTIONARY ATTACK

### BEGIN DICTIONARY ATTACK WITH REPLACEMENTS

def get_transformations(password, replacements, from_index):
	if(from_index==len(replacements)):
		return [password]
	else:
		res = []
		nexts = get_transformations(password, replacements, from_index+1)
		repl = replacements[from_index]
		for t in nexts:
			res.append(t)
			transformation = t.replace(repl[0], repl[1])
			if(transformation!=t):
				res.append(transformation)
		return res

def dict_attack_with_replacements(hash, dict_filename, replacements):
	i=0
	with open(dict_filename) as f:
		for line in f:
			i = count_print(i)
			password = line.rstrip()
			transformations = get_transformations(password, replacements, 0)
			for t in transformations:
				check_password(hash, t)

### END DICTIONARY ATTACK WITH REPLACEMENTS

### BEGIN TARGETED ATTACK

def generate_possibilities(combination, words):
	result = [combination]
	for w in words:
		without = set(words)
		without.remove(w)
		new_combination = list(combination)
		new_combination.append(w)
		result.extend(generate_possibilities(new_combination, without))
	return result

def targeted_attack(hash, words):
	possibilities = map(lambda l: "".join(l), generate_possibilities([], words))
	i=0
	for p in possibilities:
		i = count_print(i)
		check_password(hash, p)

### END TARGETED ATTACK

parser = argparse.ArgumentParser(description="Brute Force Crack. "+ 
	"A utiliser uniquement dans un but éducatif. "+
	" See github.com/CryptoDox/BruteForceCrack for the full code and documentation.")
parser.add_argument("hash", help="SHA256 hash of the password to crack.")
parser.add_argument("method",
	help="Types d'attaques. Paramètres acceptés : brute_force, dict, dict_repl, targeted. ")
parser.add_argument("-l", "--length_max", type=int, default=5,
	help="Longeur max du password en mode 'brute_force'. 5 par default.")
parser.add_argument("-d", "--dictionary", default="",
	help="Nom du dictionnaire à utiliser en mode 'dict' ou 'dict_repl'.")
parser.add_argument("-w", "--words", default="",
	help="Liste de mots séparés par une virgule en mode 'targeted'.")
parser.add_argument("-r", "--replacements", default="",
	help="liste de caractères de remplacements séparés par une virgule en mode 'dict_repl'. "+
	"Dans chaque couple, les caractères doivent être séparés par un slash. Ex. 'i' remplacé par '1' doit être renseigné comme ceci: 'i/1'.")
args = parser.parse_args()

if(args.method=="brute_force"):
	bruteforce_attack(args.hash, args.length_max)
elif(args.method=="dict"):
	if(args.dictionary==""):
		print("La méthode 'dict' nécessite un argument 'dictionary'")
		quit()
	dictionary_attack(args.hash, args.dictionary)
elif(args.method=="dict_repl"):
	if(args.dictionary==""):
		print("La méthode 'dict_repl' nécessite un argument 'dictionary'")
		quit()
	if(args.replacements==""):
		print("La méthode 'dict_repl' nécessite un argument 'replacements'")
		quit()
	replacements = map(lambda r: r.split("/"), args.replacements.split(","))
	dict_attack_with_replacements(args.hash, args.dictionary, replacements)
elif(args.method=="targeted"):
	if(args.words==""):
		print("La méthode 'targeted' nécessite un argument 'words'")
		quit()
	words_set = set(args.words.split(","))
	targeted_attack(args.hash, words_set)
else:
	print("Ce type de méthode '"+args.method+"' n\'existe pas.")
	quit()

print("Echec du déchiffrement avec ces paramètres et dans ce mode.")