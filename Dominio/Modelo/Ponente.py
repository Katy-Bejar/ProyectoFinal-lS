#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuario import Usuario

class Ponente(Usuario):
    def __init__(self, nacionalidad,especialidad, numPublicaiones):
        self.nacionalidad = nacionalidad
        self.especialidad = especialidad
        self.numPublicaiones = numPublicaiones

    def especialidad(self):
        return self.especialidad
    
    def numPublicaiones(self):
        return self.numPublicaiones
    
    def setNumPublicaciones(self, numPublicaiones):
        self.numPublicaiones = numPublicaiones

    def getNumPublicaciones(self, ):
        return self.numPublicaiones

