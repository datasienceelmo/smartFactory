#!/usr/bin/env python
# -*- coding: utf8 -*-

#import read as R
#import Write as W
#import Write_init as WI



while True:
    terminal_input = raw_input('Eingabe :')
    if terminal_input == "blau":
        print "i bims blau"
        import write_blue

    elif terminal_input == "rot":
        print "i bims rot"
        import write_red
        
    elif terminal_input == "lila":
        print "i bims lila"
        import write_purple
        
    elif terminal_input == "gelb":
        print "i bims gelb"
        import write_yellow
        
    else:
        print "Produkt nicht produzierbar!!!"

