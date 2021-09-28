#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from typing import List

def convert_to_absolute(number: float) -> float:
    if number >= 0:
        return number
    if number < 0:
        return -number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    resultat = [""]*len(prefixes)

    for k in range(len(prefixes)):
        resultat[k] = prefixes[k]+suffixe

    return resultat


def factorial(number: int) -> int:
    #if ((number % 1) != number) | (number < 0):
    #    print("Le nombre n'est pas entier ou est negatif.")
    #    return None
    if number == 0 | number == 1:
        return 1

    resultat = 1
    for k in range(2,number):
        resultat *= k

    return resultat

def prime_integer_summation() -> int:
    #k=2
    sumprimes = 0
    k = 2
    n = 0
    divisible = False
    while n < 100:
        diviseur = 2
        while (diviseur*diviseur <= k): #vérifier les diviseurs avant la racine de k
            if k % diviseur == 0:
                divisible = True
                break
            diviseur += 1

        if divisible:
            divisible = False
            k += 1
            continue

        #Si on est arriver ici, k est premier
        n += 1
        sumprimes += k
        k += 1
    return sumprimes

def use_continue() -> None:
    for k in range(11):
        if k == 5:
            continue
        print(k)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = [True]*len(groups)
    #for (k,j) in product(len(groups),len):

    for k in range(0,len(groups)):
        curr_group = groups[k]
        curr_len = len(curr_group)
        temp_critere = True

        if curr_len > 10 or curr_len <= 3:
            result[k] = False
            continue

        possede_50ans = False
        possede_70ans_plus = False
        # if 25 in curr_group[j]: ...
        # if (min(curr_coupr[j]) < 18) or (50 in curr_group[j] and max(curr_group[j])>70): ...
        for j in range(0, curr_len):
            if(curr_group[j] == 25):
                temp_critere = True
                break
            if(curr_group[j] < 18):
                temp_critere = False
            if(curr_group[j] > 70):
                possede_70ans_plus = True
            if(curr_group[j] == 50):
                possede_50ans = True
            if(possede_70ans_plus and possede_50ans):
                temp_critere = False

        result[k] = temp_critere


    return result


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
