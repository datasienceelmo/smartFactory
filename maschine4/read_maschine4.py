#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import write_blue
import write_red
import write_purple
import write_yellow

continue_reading = True

#Ab hier kommen unsere Funktionen
##########################################################################################
################################################################################

def get_product(input):

    #Ueberpruefung der Variablen in den jeweiligen Datenfelder und Aufruf der entsprechenden Schreibdatei (write_Farbe)
    if input[0] == 11 and input[2] == 2:
        print "Blaues Produkt erkannt \n"
        # Aufruf der richtigen Schreibdatei mittels .process_production(), da bei Aufruf per Import-Funktion diese sofort ausgefuehrt werden wuerde
        write_blue.process_production(input)
        print "Bearbeitung abgeschlossen"
        print "Der Transponder hat nun folgende Daten gespeichert: \n", data

    elif input[0] == 22 and input[2] == 2:
        print "Rotes Produkt erkannt \n"
        write_red.process_production(input)
        print "Bearbeitung abgeschlossen"
        print "Der Transponder hat nun folgende Daten gespeichert: \n", data

    elif input[0] == 33 and input[2] == 2:
        print "Lila Produkt erkannt \n"
        write_purple.process_production(input)
        print "Bearbeitung abgeschlossen"
        print "Der Transponder hat nun folgende Daten gespeichert: \n", data

    elif input[0] == 44 and input[2] == 2:
        print "Gelbes Produkt erkannt \n"
        write_yellow.process_production(input)
        print "Bearbeitung abgeschlossen"
        print "Der Transponder hat nun folgende Daten gespeichert: \n", data

    #Bearbeitung des Produktes an dieser Station nicht möglich
    else:
        print "\n"
        print data
        print "Verletzung der richtigen Produktionsreihenfolge festgestellt."
        print "Derzeitiger Status:", data[2]
        print "Bitte leiten Sie das Produkt zur entsprechenden Station weiter."
        
   
##########################################################################################
################################################################################
################################################################################


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "\n"
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            
            # MIFAREReader.MFRC522_Read(8)
            data = MIFAREReader.MFRC522_Read(8)
            get_product(data)
            
            data = str(data)
    
            MIFAREReader.MFRC522_StopCrypto1()
            
            print "\n"
            print "Reader Cooldown (2 Sekunden)"
            for i in xrange(2,0,-1):
                time.sleep(1)
                print i, "..."
            
        else:
            print "Authentication error"



    
