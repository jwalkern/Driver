# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:42:36 2019

@author: svu
"""

from time import sleep
import spidev

def read_ADC(ADC, channel, vref):
    """
    Aflæser ADCen og returnerer resultatet
    """
    
    # skriv her koden der er nødvendig for at læse fra den angivne kanal 'channel' og reference spænding

    return # returner den læsete værdi

def init_ADC(SSn = 0):    
    """
    Initialiserer ADC chippen
    """

    # skriv kode her til at initialisere dit ADC object 
    
    return # returner ADC object


try:
    adc = init_ADC(  ) # angiv det rigtige slave slect nummer

    while(True):

        print("ADC reading" read_ADC(adc, , )) # tilføj manglende argumenter
        
        sleep(0.5)
except KeyboardInterrupt:
    exit()

    