#!/usr/bin/python
#-*- coding: utf-8 -*-

class Nombre:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def fullName(self):
        return "{} {}".format(self.nombre, self.apellido)


class Usuario:
    def __init__(self, IDusuario, nombre, apellido, correo, contraseña):
        self.IDusuario = IDusuario
        self.nombreC = Nombre(nombre, apellido)
        self.correo = correo
        self.contraseña = contraseña

    def registrar(self, ):
        pass

    def participarEvento(self, ):
        pass

    def ColaborarEvento(self, ):
        pass

    def comentarEvento(self, ):
        pass

    def getCorreo(self, ):
        pass

    def setContraseña(self, usuarioID):
        pass

    def getContraseña(self, ):
        pass

    def setNombre(self, nombre):
        pass

    def getNombre(self, ):
        pass

