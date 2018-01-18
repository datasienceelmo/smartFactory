#!/usr/bin/env python
# -*- coding: utf8 -*-
import write_blue
import write_red
import write_purple
import write_yellow

#Dauerschleife zum permanenten Beschreiben der Transponder
while True:
    print "\nBitte Produktfarbe (Kleinbuchstaben) eingeben"
    #Implementierung der Terminaleingabe 
    terminal_input = raw_input('Eingabe :')

    #Ueberpruefung der Eingabe und Aufruf der entsprechenden Schreibdatei (write_Farbe)
    if terminal_input == "blau":
        print "Produkt blau: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        # Aufruf der richtigen Schreibdatei mittels .init(), da bei Aufruf per Import-Funktion diese sofort ausgefuehrt werden wuerde
        write_blue.init() 
        print "Schreibvorgang abgeschlossen"

    elif terminal_input == "rot":
        print "Produkt rot: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        write_red.init()
        print "Schreibvorgang abgeschlossen"
        
    elif terminal_input == "lila":
        print "Produkt lila: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        write_purple.init()
        print "Schreibvorgang abgeschlossen"
        
    elif terminal_input == "gelb":
        print "Produkt gelb: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        write_yellow.init()
        print "Schreibvorgang abgeschlossen"

    #Ausgabe bei Falscheingabe
    else:
        print "Produkt nicht produzierbar. Derzeit koennen folgende Produkte produziert werden: \n blau, rot, lila, gelb"

