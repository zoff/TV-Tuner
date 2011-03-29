#!/usr/bin/python
# -*- coding: utf-8 -*-
# options.py
# finestra delle opzioni
# Copyright (C) 2009-2010 Andrea "Klenje" Decorte <adecorte@gmail.com>
# Released under the terms of the Gnu Public License 3 or later

import sys
from PyQt4 import QtGui,  QtCore
from settings import MySettings

class OptionsWindow(QtGui.QDialog):
    def __init__(self,  parent=None,  flags = 0,  relative = False,  tabPreferiti = False):
        QtGui.QWidget.__init__(self)
        self.settings = MySettings(relative)
        self.setWindowTitle("Televideo - Opzioni")
        self.setFixedSize(360,  280)
        #tab bar
        self.tabs = QtGui.QTabWidget(self)
        pag1 = QtGui.QWidget()
        self.edizionePredefinita = QtGui.QCheckBox("&Avvia sempre su edizione nazionale")
        label = QtGui.QLabel("Pagina &iniziale")
        self.pagIniziale = QtGui.QSpinBox()
        self.pagIniziale.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.pagIniziale.setRange(100, 899)
        label.setBuddy(self.pagIniziale)
        labelEdizione = QtGui.QLabel("Scegli &edizione")
        self.edizione = QtGui.QComboBox()
        
        #carico edizioni. i nomi sono questi perché se no non trova i percorsi
        self.edizione.addItem("Nazionale")
        self.edizione.addItem("Abruzzo")
        self.edizione.addItem("Altoadige")
        self.edizione.addItem("Aosta")
        self.edizione.addItem("Basilicata")
        self.edizione.addItem("Calabria")
        self.edizione.addItem("Campania")        
        self.edizione.addItem("Emilia")
        self.edizione.addItem("Friuli")
        self.edizione.addItem("Lazio")
        self.edizione.addItem("Liguria")
        self.edizione.addItem("Lombardia")
        self.edizione.addItem("Marche")
        self.edizione.addItem("Molise")
        self.edizione.addItem("Piemonte")
        self.edizione.addItem("Puglia")
        self.edizione.addItem("Sardegna")
        self.edizione.addItem("Sicilia")
        self.edizione.addItem("Toscana")
        self.edizione.addItem("Trentino")
        self.edizione.addItem("Umbria")
        self.edizione.addItem("Veneto")
        labelEdizione.setBuddy(self.edizione)
        self.refreshAutomatico = QtGui.QCheckBox("A&ggiorna pagina ogni")
        self.intervalloRefreshAutomatico = QtGui.QSpinBox()
        self.intervalloRefreshAutomatico.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.intervalloRefreshAutomatico.setRange(15, 6000 )
        labelRefresh = QtGui.QLabel("&sec") 
        labelRefresh.setBuddy(self.intervalloRefreshAutomatico)
        QtCore.QObject.connect(self.refreshAutomatico, QtCore.SIGNAL('stateChanged (int)'), self.attivaIntervalloRefresh)
 
        layoutRefresh = QtGui.QHBoxLayout()
        layoutRefresh.addWidget(self.refreshAutomatico)
        layoutRefresh.addWidget(self.intervalloRefreshAutomatico)
        layoutRefresh.addWidget(labelRefresh) 
        
        layout = QtGui.QGridLayout(pag1)
        layout.addWidget(label,  0,  0)
        layout.addWidget(self.pagIniziale,  0,  1)
        layout.addWidget(self.edizionePredefinita,  2,  0,  1,   2)
        layout.addWidget(labelEdizione,  1,  0)
        layout.addWidget(self.edizione,  1,  1) 
        
        layout.addLayout(layoutRefresh,  3,  0,  1,  2)
        
        labelAzione = QtGui.QLabel("&Se pagina non trovata:")
        self.azione= QtGui.QComboBox()
        self.azione.addItem("Chiedi sempre")
        self.azione.addItem("Rimani su pagina corrente")
        self.azione.addItem("Cerca pagina successiva")
        labelAzione.setBuddy(self.azione)
        layout.addWidget(labelAzione,  4,  0)
        layout.addWidget(self.azione,  4,  1) 
        
        self.tabs.addTab(pag1,  "&Opzioni")
        
        pagCustomButtons = QtGui.QWidget()
        layoutCustomButtons = QtGui.QGridLayout(pagCustomButtons)
        label1 = QtGui.QLabel("Preferito &1")
        self.name1 = QtGui.QLineEdit()
        self.name1.setMaxLength(10)
        self.page1 = QtGui.QSpinBox()
        self.page1.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.page1.setRange(100,  899)
        label1.setBuddy(self.name1)
        layoutCustomButtons.addWidget(label1,  0,  0)
        layoutCustomButtons.addWidget(self.name1,  0,  1)
        layoutCustomButtons.addWidget(self.page1,  0,  2)
        label2 = QtGui.QLabel("Preferito &2")
        self.name2 = QtGui.QLineEdit()
        self.name2.setMaxLength(10)
        self.page2 = QtGui.QSpinBox()
        self.page2.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.page2.setRange(100,  899)
        label2.setBuddy(self.name2)
        layoutCustomButtons.addWidget(label2,  1,  0)
        layoutCustomButtons.addWidget(self.name2,  1,  1)
        layoutCustomButtons.addWidget(self.page2,  1,  2)
        label3 = QtGui.QLabel("Preferito &3")
        self.name3 = QtGui.QLineEdit()
        self.name3.setMaxLength(10)
        self.page3 = QtGui.QSpinBox()
        self.page3.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.page3.setRange(100,  899)
        label3.setBuddy(self.name3)
        layoutCustomButtons.addWidget(label3,  2,  0)
        layoutCustomButtons.addWidget(self.name3,  2,  1)
        layoutCustomButtons.addWidget(self.page3,  2,  2)
        label4 = QtGui.QLabel("Preferito &4")
        self.name4 = QtGui.QLineEdit()
        self.name4.setMaxLength(10)
        self.page4 = QtGui.QSpinBox()
        self.page4.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.page4.setRange(100,  899)
        label4.setBuddy(self.name4)
        layoutCustomButtons.addWidget(label4,  3,  0)
        layoutCustomButtons.addWidget(self.name4,  3,  1)
        layoutCustomButtons.addWidget(self.page4,  3,  2)
        label5 = QtGui.QLabel("Preferito &5")
        self.name5 = QtGui.QLineEdit()
        self.name5.setMaxLength(10)
        self.page5 = QtGui.QSpinBox()
        self.page5.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.page5.setRange(100,  899)
        label5.setBuddy(self.name5)
        layoutCustomButtons.addWidget(label5,  4,  0)
        layoutCustomButtons.addWidget(self.name5,  4,  1)
        layoutCustomButtons.addWidget(self.page5,  4,  2)
        self.tabs.addTab(pagCustomButtons,  "&Preferiti")
        
        #impostazioni proxy
        pagProxy = QtGui.QWidget()
        self.usaProxy = QtGui.QCheckBox("&Usa server proxy")
        labelProxy1 = QtGui.QLabel("&Host:Port")
        self.hostProxy = QtGui.QLineEdit()
        self.portProxy = QtGui.QLineEdit()
        validator = QtGui.QIntValidator(20,  65535,  pagProxy)
        self.portProxy.setValidator(validator)
        labelProxy1.setBuddy(self.hostProxy)
        layoutProxy = QtGui.QGridLayout(pagProxy)
        layoutProxy.addWidget(self.usaProxy,  0,  0,  1,  3)
        layoutProxy.addWidget(labelProxy1,  1,  0)
        layoutProxy.addWidget(self.hostProxy,  1,  1)
        layoutProxy.addWidget(self.portProxy, 1,  2)
        
        labelUsername = QtGui.QLabel("User&name: ")
        self.userName = QtGui.QLineEdit()
        labelPassword = QtGui.QLabel("Pass&word: ")
        self.password = QtGui.QLineEdit()
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        labelUsername.setBuddy(self.userName)
        labelPassword.setBuddy(self.password)
        layoutProxy.addWidget(labelUsername,  2,  0)
        layoutProxy.addWidget(self.userName,  2,  1,  1,  2)
        layoutProxy.addWidget(labelPassword,  3,  0)
        layoutProxy.addWidget(self.password,  3,  1,  1,  2)
        
        labelWarning = QtGui.QLabel("<b>Attenzione</b>: le impostazioni di questa scheda saranno applicate solo al riavvio.<br />Se desideri usare il proxy definito nelle Opzioni di sistema, lascia deselezionato la casella Usa server proxy")
        labelWarning.setWordWrap(True)
        layoutProxy.addWidget(labelWarning,  4,  0,  1,  3)
        self.tabs.addTab(pagProxy,  "Pro&xy")
        QtCore.QObject.connect(self.usaProxy, QtCore.SIGNAL('stateChanged (int)'), self.selezioneProxy)
        
        #pagina riepilogo scorciatoie
        pagShortcuts = QtGui.QWidget()
        shortcuts1 = QtGui.QLabel("Pagina successiva\t")
        shortcuts2 = QtGui.QLabel("Ctrl +")
        shortcuts3 = QtGui.QLabel("Pagina precedente")
        shortcuts4 = QtGui.QLabel("Ctrl -")
        shortcuts5 = QtGui.QLabel("Sottopagina succ.")
        shortcuts6 = QtGui.QLabel("Alt +")
        shortcuts7 = QtGui.QLabel("Sottopagina prec.")
        shortcuts8 = QtGui.QLabel("Alt -")
        shortcuts9 = QtGui.QLabel("Pagina iniziale")
        shortcuts10 = QtGui.QLabel("Ctrl H")
        shortcuts11 = QtGui.QLabel("Preferito da 1 a 5")
        shortcuts12 = QtGui.QLabel("Ctrl 1 - 5")
        shortcuts13 = QtGui.QLabel("Salva pagina")
        shortcuts14 = QtGui.QLabel("Ctrl S")
        shortcuts15 = QtGui.QLabel("Aggiorna pagina")
        shortcuts16 = QtGui.QLabel("F5")
        shortcuts17 = QtGui.QLabel("Interrompi caricamento")
        shortcuts18 = QtGui.QLabel("Esc")
        layout3 = QtGui.QGridLayout(pagShortcuts)
        layout3.addWidget(shortcuts1,  0,  0)
        layout3.addWidget(shortcuts2,  0,  1)
        layout3.addWidget(shortcuts3,  1,  0)
        layout3.addWidget(shortcuts4,  1,  1)
        layout3.addWidget(shortcuts5,  2,  0)
        layout3.addWidget(shortcuts6,  2,  1)
        layout3.addWidget(shortcuts7,  3,  0)
        layout3.addWidget(shortcuts8,  3,  1)
        layout3.addWidget(shortcuts9,  4,  0)
        layout3.addWidget(shortcuts10,  4,  1)
        layout3.addWidget(shortcuts11,  5,  0)
        layout3.addWidget(shortcuts12,  5,  1)
        layout3.addWidget(shortcuts13,  6,  0)
        layout3.addWidget(shortcuts14,  6,  1)
        layout3.addWidget(shortcuts15,  7,  0)
        layout3.addWidget(shortcuts16,  7,  1)
        layout3.addWidget(shortcuts17,  8,  0)
        layout3.addWidget(shortcuts18,  8,  1)
        self.tabs.addTab(pagShortcuts,  "Scorcia&toie")
        
        #about
        pagAbout = QtGui.QWidget()
        about = QtGui.QLabel("<qt>Scritto per cazzeggio da <a href='mailto:adecorte@gmail.com'>Andrea 'Klenje' Decorte</a>.  Thanks a <i>elpibe</i> e <i>ildiavolo</i> per idee e betatesting<br /><br />Released under GPL2 or later; icone dai temi CrystalSVG e Tango di KDEmod<br /><br /><a href='http://code.google.com/p/telenonvideo'>Sito ufficiale su Google Code</a></qt>")
        about.setFrameStyle(QtGui.QFrame.StyledPanel)
        about.setWordWrap(True)
        about.setAlignment(QtCore.Qt.AlignJustify)
        about.setOpenExternalLinks(True)
        layout2 = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight,  pagAbout)
        layout2.addWidget(about)
        self.tabs.addTab(pagAbout, "&About")
        
        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Save | QtGui.QDialogButtonBox.Cancel,  QtCore.Qt.Horizontal)
        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL('accepted()'), self.salvaOpzioni)
        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL('rejected()'), self.reject)
        
        layoutTotale = QtGui.QVBoxLayout(self)
        layoutTotale.addWidget(self.tabs)
        layoutTotale.addWidget(buttonBox)
        
        #parametro per andare direttamente alla tab dei preferiti, se un pulsante non è configurato
        if tabPreferiti:
            self.showTabPreferiti()        
        
        self.caricaOpzioni()
        
    def getEdizionePredefinita(self):
        return self.edizionePredefinita
    def getEdizione(self):
        return self.edizione
    def getAzione(self):
        return self.azione
    def getNomePagina1(self):
        return self.name1
    def getNumeroPagina1(self):
        return self.page1
    def getNomePagina2(self):
        return self.name2
    def getNumeroPagina2(self):
        return self.page2
    def getNomePagina3(self):
        return self.name3
    def getNumeroPagina3(self):
        return self.page3
    def getNomePagina4(self):
        return self.name4
    def getNumeroPagina4(self):
        return self.page4
    def getNomePagina5(self):
        return self.name5
    def getNumeroPagina5(self):
        return self.page5
    def getPaginaIniziale(self):
        return self.pagIniziale
    def getHostProxy(self):
        return self.hostProxy
    def getPortProxy(self):
        return self.portProxy
    def getUsernameProxy(self):
        return self.userName
    def getPasswordProxy(self):
        return self.password
    def getUsaProxy(self):
        return self.usaProxy
    def getIntervalloRefresh(self):
        return self.intervalloRefreshAutomatico
    def getRefreshAutomatico(self):
        return self.refreshAutomatico
        
    def showTabPreferiti(self):
        self.tabs.setCurrentIndex(1) #è la seconda tab

    def salvaOpzioni(self):     
         if self.settings.isWritable():
             self.settings.pagIniziale = self.getPaginaIniziale().value()
             self.settings.edizionePredefinita = self.getEdizionePredefinita().checkState()
             self.settings.refreshAutomatico = self.getRefreshAutomatico().checkState()
             self.settings.intervalloRefresh = self.getIntervalloRefresh().text()
             self.settings.nomePagina1 = self.getNomePagina1().text()
             self.settings.numeroPagina1 = self.getNumeroPagina1().value()
             self.settings.nomePagina2 = self.getNomePagina2().text()
             self.settings.numeroPagina2 = self.getNumeroPagina2().value()
             self.settings.nomePagina3 = self.getNomePagina3().text()
             self.settings.numeroPagina3 = self.getNumeroPagina3().value()
             self.settings.nomePagina4 = self.getNomePagina4().text()
             self.settings.numeroPagina4 = self.getNumeroPagina4().value()
             self.settings.nomePagina5 = self.getNomePagina5().text()
             self.settings.numeroPagina5 = self.getNumeroPagina5().value()
             self.settings.edizione = self.getEdizione().currentText()
             self.settings.azionePaginaNonTrovata = self.getAzione().currentIndex()
             self.settings.usaProxy = self.getUsaProxy().checkState()
             self.settings.hostProxy = self.getHostProxy().text()
             self.settings.portProxy = self.getPortProxy().text()
             self.settings.userNameProxy = self.getUsernameProxy().text()
             self.settings.passwordProxy = self.getPasswordProxy().text()
         self.reject()
    def caricaOpzioni(self):
        self.getPaginaIniziale().setValue(self.settings.pagIniziale)
        if self.settings.edizionePredefinita == 0:
             self.getEdizionePredefinita().setCheckState(QtCore.Qt.Unchecked)
        elif self.settings.edizionePredefinita == 2:
             self.getEdizionePredefinita().setCheckState(QtCore.Qt.Checked)
        if self.settings.refreshAutomatico == 0:
             self.getRefreshAutomatico().setCheckState(QtCore.Qt.Unchecked)
        elif self.settings.refreshAutomatico == 2:
             self.getRefreshAutomatico().setCheckState(QtCore.Qt.Checked)
        self.getIntervalloRefresh().setValue(self.settings.intervalloRefresh)
        self.getNomePagina1().setText(self.settings.nomePagina1)    
        self.getNumeroPagina1().setValue(self.settings.numeroPagina1)  
        self.getNomePagina2().setText(self.settings.nomePagina2)    
        self.getNumeroPagina2().setValue(self.settings.numeroPagina2)
        self.getNomePagina3().setText(self.settings.nomePagina3)    
        self.getNumeroPagina3().setValue(self.settings.numeroPagina3)
        self.getNomePagina4().setText(self.settings.nomePagina4)    
        self.getNumeroPagina4().setValue(self.settings.numeroPagina4)
        self.getNomePagina5().setText(self.settings.nomePagina5)    
        self.getNumeroPagina5().setValue(self.settings.numeroPagina5)
        indice = self.getEdizione().findText(self.settings.edizione)
        self.getEdizione().setCurrentIndex(indice)
        self.getAzione().setCurrentIndex(self.settings.azionePaginaNonTrovata)
        if self.settings.usaProxy == 0:
             self.getUsaProxy().setCheckState(QtCore.Qt.Unchecked)
        elif self.settings.usaProxy == 2:
             self.getUsaProxy().setCheckState(QtCore.Qt.Checked)
        self.getHostProxy().setText(self.settings.hostProxy)
        self.getPortProxy().setText(QtCore.QString(self.settings.portProxy))
        self.getUsernameProxy().setText(self.settings.userNameProxy)
        self.getPasswordProxy().setText(self.settings.passwordProxy)
        self.usaProxy.emit(QtCore.SIGNAL('stateChanged (int)'),  self.getUsaProxy().checkState())
        self.refreshAutomatico.emit(QtCore.SIGNAL('stateChanged (int)'),  self.getRefreshAutomatico().checkState())
        
    def selezioneProxy(self,  selezionato):
        if selezionato ==  QtCore.Qt.Unchecked:
            self.getHostProxy().setEnabled(False)
            self.getPortProxy().setEnabled(False)
            self.getUsernameProxy().setEnabled(False)
            self.getPasswordProxy().setEnabled(False)
        if selezionato ==  QtCore.Qt.Checked:
            self.getHostProxy().setEnabled(True)
            self.getPortProxy().setEnabled(True)
            self.getUsernameProxy().setEnabled(True)
            self.getPasswordProxy().setEnabled(True)
            
    def attivaIntervalloRefresh(self,  selezionato):
        if selezionato ==  QtCore.Qt.Unchecked:
            self.getIntervalloRefresh().setEnabled(False)
        if selezionato ==  QtCore.Qt.Checked:
            self.getIntervalloRefresh().setEnabled(True)
