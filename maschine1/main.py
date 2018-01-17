#!/usr/bin/env python
# -*- coding: utf8 -*-

#Dauerschleife zum permanenten Beschreiben der Transponder
while True:
    print "\nBitte Produktfarbe (Kleinbuchstaben) eingeben"
    #Implementierung der Terminaleingabe 
    terminal_input = raw_input('Eingabe :')

    #Ueberpruefung der Eingabe und Aufruf der entsprechenden Schreibdatei (write_Farbe)
    if terminal_input == "blau":
        print "Produkt blau: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        import write_blue
        print "Schreibvorgang abgeschlossen"

    elif terminal_input == "rot":
        print "Produkt rot: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        import write_red
        print "Schreibvorgang abgeschlossen"
        
    elif terminal_input == "lila":
        print "Produkt lila: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        import write_purple
        print "Schreibvorgang abgeschlossen"
        
    elif terminal_input == "gelb":
        print "Produkt gelb: Bitte Transponder zum Beschreiben auf das Lesegerät halten"
        import write_yellow
        print "Schreibvorgang abgeschlossen"

    #Ausgabe bei Falscheingabe
    else:
        print "Produkt nicht produzierbar. Derzeit koennen folgende Produkte produziert werden: \n blau, rot, lila, gelb"

