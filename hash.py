#!/usr/bin/env python
# hash : Chiffre un mot de passe en le hachant avec SHA256
# -*- coding: utf-8 -*-

# This file is part of Brute-Force-Crack with Python3
# See wiki doc for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "CodeKiller"
__date__ =  "11 juin 2020"

import hashlib

"""
Le moyen le plus simple pour cracker un mote de passe
c'est de le hacher menu, puis de le comparer
"""

__version__ = "1.0.0 Beta"

motdepass = input("String2Hash ? \n>")

hashPass = hashlib.sha256(bytes(motdepass, 'utf-8')).hexdigest()

print (hashPass)
