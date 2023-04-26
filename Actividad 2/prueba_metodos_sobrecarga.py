# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 18:56:31 2023

@author: Facu
"""

class Calculadora:
    __n1=0
    
    def __init__(self, n1):
        self.__n1 = n1
    
    #suma   
    def __add__(self,otro):
        return Calculadora(self.__n1+otro.__n1)
    
    def __repr__(self):
        return f'El resultado es: {self.__n1}'
    
    def __gt__(self, otro):
        return self.__n1 > otro.__n1
        


    
 