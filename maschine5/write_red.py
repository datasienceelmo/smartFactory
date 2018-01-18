#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

#Eigene Methoden
#########################################################################################
################################################################################

#Methode zum Addieren der Produktionszeit
#Produtkionszeit rot an Maschine5: 11 Sekunden
def addTime(input, prodTime):
    totalTime = input + prodTime
    return totalTime

def process_production(input):
    print "Folgende Daten sind derzeit auf dem Transponder gespeichert:\n" , input

    #Initialisierung der Produktionszeit an Maschine 5
    prodTime = 11
    
    #Auslesen des Status aus dem dritten Wertes im Array
    curStatus = input[2]

     #Auslesen der bereits benötigten Zeitaufwands aus dem vierten Wertes im Array
    curTime = input[3]

    #Funktionsaufruf zum Addieren der Zeit
    totalTime = addTime(curTime, prodTime)

    #Übergabe des Input Arrays an die data Variable
    data = input

    #Hochzaehlen des Status um 1
    data[2] = curStatus + 1

    #Uebergabe der Produktionszeit (prodTime) an die 4. Stelle des Arrays
    data[3] = totalTime

    print "\n"
    print "Produktion wird gestartet. Die Produktionszeit beträgt: ", prodTime, " Sekunden."
    print "\n"
    print "Produktionsfortschritt:"

    #SleepTimer zur Simulation der Produktionszeit
    for i in xrange(prodTime,0,-1):
        time.sleep(1)
        print i, "..."

    print"\n"

    # Fill the data with 0x00
    for x in range(0,16):
                data.append(0x00)

    print "Now we fill it with 0x00:"
    MIFAREReader.MFRC522_Write(8, data)
    
    continue_reading = False

################################################################################
################################################################################

continue_reading = True

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

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
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
        print "\n"

        # Check if authenticated
        if status == MIFAREReader.MI_OK:

            # Variable for the data
            print "Status ok Produktdaten auslesen..."
            print "\n"
            data = MIFAREReader.MFRC522_Read(8)
            print data
            print "\n"

            # Stop
            MIFAREReader.MFRC522_StopCrypto1()

            # Make sure to stop reading for cards
            continue_reading = False
        else:
            print "Authentication error"
