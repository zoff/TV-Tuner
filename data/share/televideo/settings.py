#!/usr/bin/python
# -*- coding: utf-8 -*-
# settings.py
# wrapper per salvataggio e caricamento impostazioni
# Copyright (C) 2009-2010 Andrea "Klenje" Decorte <adecorte@gmail.com>
# Released under the terms of the Gnu Public License 3 or later

from PyQt4 import QtCore

class MySettings(QtCore.QSettings):
    def __init__(self,  relative):
        if relative:
            QtCore.QSettings.__init__(self, QtCore.QSettings.UserScope, "televideo")
        else:
            #salvo tutto nella stessa cartella del programma
            QtCore.QSettings.__init__(self, "televideo.ini", QtCore.QSettings.IniFormat)
    def getPagIniziale(self):
        return self.value("pagIniziale").toInt()[0]
    def setPagIniziale(self,  num):
        self.setValue("pagIniziale", QtCore.QVariant(num))
    pagIniziale = property(getPagIniziale,  setPagIniziale)
    def getEdizione(self):
        return self.value("edizione").toString()
    def setEdizione(self,  edizione):
        self.setValue("edizione", QtCore.QVariant(edizione))
    edizione = property(getEdizione,  setEdizione)
    def getNumeroPagina1(self):
        return self.value("numeroPagina1").toInt()[0]
    def setNumeroPagina1(self,  numero):
        self.setValue("numeroPagina1",  QtCore.QVariant(numero))
    def getNumeroPagina2(self):
        return self.value("numeroPagina2").toInt()[0]
    def setNumeroPagina2(self,  numero):
        self.setValue("numeroPagina2",  QtCore.QVariant(numero))
    def getNumeroPagina3(self):
        return self.value("numeroPagina3").toInt()[0]
    def setNumeroPagina3(self,  numero):
        self.setValue("numeroPagina3",  QtCore.QVariant(numero))
    def getNumeroPagina4(self):
        return self.value("numeroPagina4").toInt()[0]
    def setNumeroPagina4(self,  numero):
        self.setValue("numeroPagina4",  QtCore.QVariant(numero))
    def getNumeroPagina5(self):
        return self.value("numeroPagina5").toInt()[0]
    def setNumeroPagina5(self,  numero):
        self.setValue("numeroPagina5",  QtCore.QVariant(numero))
    numeroPagina1 = property(getNumeroPagina1,  setNumeroPagina1)
    numeroPagina2 = property(getNumeroPagina2,  setNumeroPagina2)
    numeroPagina3 = property(getNumeroPagina3,  setNumeroPagina3)
    numeroPagina4 = property(getNumeroPagina4,  setNumeroPagina4)
    numeroPagina5 = property(getNumeroPagina5,  setNumeroPagina5)
    def getEdizionePredefinita(self):
        return self.value("edizionePredefinita").toInt()[0]
    def setEdizionePredefinita(self,  stato):
        self.setValue("edizionePredefinita",  QtCore.QVariant(stato))
    edizionePredefinita = property(getEdizionePredefinita,  setEdizionePredefinita)
    def getAzionePaginaNonTrovata(self):
        return self.value("azionePaginaNonTrovata").toInt()[0]
    def setAzionePaginaNonTrovata(self,  azione):
        self.setValue("azionePaginaNonTrovata",  QtCore.QVariant(azione))
    azionePaginaNonTrovata= property(getAzionePaginaNonTrovata,  setAzionePaginaNonTrovata)
    
    def getRefreshAutomatico(self):
        return self.value("refreshAutomatico").toInt()[0]
    def setRefreshAutomatico(self,  stato):
        self.setValue("refreshAutomatico",  QtCore.QVariant(stato))
    refreshAutomatico = property(getRefreshAutomatico,  setRefreshAutomatico)
    def getIntervalloRefreshAutomatico(self):
        return self.value("intervalloRefresh").toInt()[0]
    def setIntervalloRefreshAutomatico(self,  intervallo):
        self.setValue("intervalloRefresh",  QtCore.QVariant(intervallo))
    intervalloRefresh = property(getIntervalloRefreshAutomatico,  setIntervalloRefreshAutomatico)
    
    def getNomePagina1(self):
        return self.value("nomePagina1").toString()
    def setNomePagina1(self,  nome):
        self.setValue("nomePagina1",  QtCore.QVariant(nome))
    def getNomePagina2(self):
        return self.value("nomePagina2").toString()
    def setNomePagina2(self,  nome):
        self.setValue("nomePagina2",  QtCore.QVariant(nome))
    def getNomePagina3(self):
        return self.value("nomePagina3").toString()
    def setNomePagina3(self,  nome):
        self.setValue("nomePagina3",  QtCore.QVariant(nome))
    def getNomePagina4(self):
        return self.value("nomePagina4").toString()
    def setNomePagina4(self,  nome):
        self.setValue("nomePagina4",  QtCore.QVariant(nome))
    def getNomePagina5(self):
        return self.value("nomePagina5").toString()
    def setNomePagina5(self,  nome):
        self.setValue("nomePagina5",  QtCore.QVariant(nome))
    nomePagina1 = property(getNomePagina1,  setNomePagina1)
    nomePagina2 = property(getNomePagina2,  setNomePagina2)
    nomePagina3 = property(getNomePagina3,  setNomePagina3)
    nomePagina4 = property(getNomePagina4,  setNomePagina4)
    nomePagina5 = property(getNomePagina5,  setNomePagina5)
    def getUsaProxy(self):
        return self.value("usaProxy").toInt()[0]
    def setUsaProxy(self,  stato):
        self.setValue("usaProxy",  QtCore.QVariant(stato))
    usaProxy = property(getUsaProxy,  setUsaProxy)
    def getHostProxy(self):
        return self.value("host").toString()
    def setHostProxy(self,  host):
        self.setValue("host",  QtCore.QVariant(host))
    def getPortProxy(self):
        return self.value("port").toInt()[0]
    def setPortProxy(self,  port):
        self.setValue("port",  QtCore.QVariant(port))
    def getUserNameProxy(self):
        return self.value("userName").toString()
    def setUserNameProxy(self,  userName):
        self.setValue("userName",  QtCore.QVariant(userName))
    def getPasswordProxy(self):
        return self.value("password").toString()
    def setPasswordProxy(self,  password):
        self.setValue("password",  QtCore.QVariant(password))    
    hostProxy = property(getHostProxy,  setHostProxy)
    portProxy = property(getPortProxy,  setPortProxy)
    userNameProxy = property(getUserNameProxy,  setUserNameProxy)
    passwordProxy = property(getPasswordProxy,  setPasswordProxy)   
 
