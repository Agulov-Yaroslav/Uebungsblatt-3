#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Übungsblatt 03"""


# Aufgabe 1

def print_square():
    """
    Die Funktion soll keine Parameter haben, der
    Benutzer wird stattdessen um Eingabe einer Zahl per Tastatur gebeten.
    Diese Zahl soll dann quadriert und wieder ausgegeben werden.
    """
    user_zahl = input("Bitte geben Sie eine Zahl ein: ")

    # Ich würde noch überprüfen, ob der User wirklich eine Zahl eingegeben hat,
    # aber in der Aufgabe steht es nicht:
    #
    # while True:
    #     user_zahl = input("Bitte geben Sie eine Zahl ein: ")
    #     try:
    #         print(float(user_zahl) ** 2)
    #         break
    #     except:
    #         print("Das ist keine Zahl!")
    #         continue

    print(int(user_zahl) ** 2)


# Aufgabe 2

def account_number(number):
    """

    :param number: eine Kontonummer
    :type number: int
    :return: Nummer mit insgesamt 9 Ziffern oder Nullen vorne
    :rtype: str
    """
    if 999999999 >= number >= 100:
        number = f"{number:09d}"
        return number
    return None

# Aufgabe 3

def translate(dictionary, word):
    """


    :param dictionary: ein Wörterbuch
    :type dictionary: dict
    :param word: das zu übersetzende Wort
    :type word: str
    :return: die jeweilige Übersetzung
    :rtype: str
    """
    return dictionary.get(word)


# Aufgabe 4

def invert_dict(dictionary):
    """
    Die Schlüssel-Wert-Paare von dictionary
    sollen invertiert und anschließend als neues Objekt vom Typ dict zurückgegeben werden.

    :param dictionary:
    :type dictionary: dict
    :return:
    :rtype: dict
    """
    inv_dict = {}
    for x, y in dictionary.items():
        inv_dict.update({f"{y}": f"{x}"})
    return inv_dict


# Aufgabe 4 Antwort Verständnisfrage:
#
# In einem Dictionary können mehrere Schlüssel auf denselben Wert zeigen. Aber nicht umgekehrt
# Wenn man dieses Wörterbuch invertiert, werden diese mehrfach vorkommenden
# Werte zu Schlüsseln im neuen Wörterbuch, und da Schlüssel in einem Dictionary
# eindeutig sein müssen, würde nur der letzte Schlüssel-Wert-Paar, der diese
# Werte im invertierten Wörterbuch zuweist, bestehen bleiben. Das führt zu
# einem nicht-deterministischen Ergebnis, da
# es unklar ist, welcher der ursprünglichen Schlüssel im neuen Wörterbuch als Wert beibehalten wird.


# Aufgabe 5

def word_mincer(word, begin_upper=False):
    """
    Die Modifikation besteht daraus, dass das Wort am Ende
    immer abwechselnd Groß- und Kleinbuchstaben enthalten soll.

    :param word: zu modifizierende Wort
    :type word: str
    :param begin_upper: ein optionaler Parameter
    :type begin_upper: bool
    :return:
    :rtype: str
    """
    edit_word = list(word.lower())
    itterator = 1 - int(begin_upper)

    while itterator < len(edit_word):
        edit_word[itterator] = edit_word[itterator].upper()
        itterator += 2

    return ''.join(edit_word)


# Testaufrufe

if __name__ == "__main__":
    print_square()
    print(account_number(12345))
    print(account_number(0))
    print(account_number(123456789))
    print(account_number(-999))
    print(account_number(11))
    print(account_number(1111111111))
    DE_EN = {
        'König': 'King',
        'Ritter': 'Knight',
        'Drache': 'Dragon',
        'Aaaarrggh': 'Aaaarrggh'
    }
    print(translate(DE_EN, 'Ritter'))
    print(translate(DE_EN, 'Pferd'))
    print(invert_dict(DE_EN))
    print(word_mincer('König'))
    print(word_mincer('KÖNIG'))
    print(word_mincer('kÖnIg'))
    print(word_mincer('KöNiG'))
    print(word_mincer('Kaugummiautomat'))
    print(word_mincer('Kaugummiautomat', begin_upper=True))
