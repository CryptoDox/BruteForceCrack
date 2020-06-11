
# Brute Force Crack

Un petit programme en Python "crack_pass.py" qui déchiffre un mot de passe à partir de son hash SHA256.
"hash.py" donne le hash (SHA256) d'un mot de passe. Rien de fabuleux, mais très facile à adapter à vos besoins...

## Requirements

Vous avez besoin de [Python3](https://www.python.org/downloads/) installé pour faire fonctionner ce script.

## Usage

Vous pouvez executer le script avec la commande `python crack_pass.py`. Il prend deux arguments en paramètres : le hash à cracker et le type d'attaque. Il existe plusieurs arguments en option. Vous trouverez la liste de ces options avec la commande: `python crack_pass.py --help`

Les types d'attaques possibles :

- `brute_force` : Test toutes les possibilités alphanumeriques d'une longeur inférieure ou égale à `--length_max`.
- `dict` : Test tous les mots de passe contenu dans un dictionnaire désigné avec le paramètre `--dictionary`.
- `dict_repl` : Test tous les mots de passe, contenu dans un dictionnaire désigné avec le paramètre `--dictionary` puis, en remplaçant les caractères par ceux indiqués avec le paramètre `--replacements`. Les charactères désignés, présent dans le mot de passe, sont tous remplacés par ceux fournit en paramètres.
- `targeted` : Test toutes les permutations possibles à l'aide d'une liste de mots précisés avec le paramètre `--words`.

## Contributing

This program is published under a GPLv2 license (see LICENCE) so feel free to clone the project and make improvements, there are so many that you can try to implement!
