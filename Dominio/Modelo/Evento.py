#!/usr/bin/python
#-*- coding: utf-8 -*-

class Evento:
    def __init__(self, tipoEvento, nombre, fecha, descripcion, lugar):
        self.tipoEvento = tipoEvento
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.lugar = lugar

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self, ):
        return self.fecha

    def setLugar(self, lugar):
        self.lugar = lugar

    def getLugar(self, ):
        return self.lugar

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self, ):
        return self.descripcion

