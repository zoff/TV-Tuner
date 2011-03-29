#!/usr/bin/python
# -*- coding: utf-8 -*-
# televideo.py
# finestra principale
# Copyright (C) 2009-2010 Andrea "Klenje" Decorte <adecorte@gmail.com>
# Released under the terms of the Gnu Public License 3 or later

import sys
from PyQt4 import QtGui,  QtCore,  QtNetwork
from options import OptionsWindow
from settings import MySettings

class MainWindow(QtGui.QMainWindow):
    
    #version
    version = QtCore.QString("0.45")
    
    def __init__(self,  parent=None):
        QtGui.QMainWindow.__init__(self)

        self.setFixedSize(400,  530)
        self.center()
        self.setWindowTitle('Televideo ' + self.version)
        if sys.platform == "win32":         
            dirTemp = QtCore.QString(winPath)
        else:
            dirTemp = QtCore.QString(directory)
        self.setWindowIcon(QtGui.QIcon(dirTemp +"/icons/televideo.png"))

        self.progressBar = QtGui.QProgressBar()
        self.stopButton = QtGui.QPushButton()
        self.stopButton.setIcon(QtGui.QIcon(dirTemp +"/icons/stop.png"))
        
        statusBar = QtGui.QStatusBar()
        statusBar.addPermanentWidget(self.progressBar)
        statusBar.addPermanentWidget(self.stopButton)
        statusBar.setSizeGripEnabled(False)
        self.setStatusBar(statusBar)
        #check iniziale, se impostazioni vuote, aggiungo valori default
        if settings.pagIniziale == 0 or settings.edizione.isEmpty():
            settings.pagIniziale = 100
            settings.edizione = "Nazionale"
            settings.edizionePredefinita = 2
            settings.intervalloRefresh = 60
            #impostazione pulsanti a 100
            settings.numeroPagina1 = 100
            settings.numeroPagina2 = 100
            settings.numeroPagina3 = 100
            settings.numeroPagina4 = 100
            settings.numeroPagina5 = 100
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    def getProgressBar(self):
        return self.progressBar
    def updateProgressBar(self, ricevuti,  totali):
        self.getProgressBar().setMaximum(totali)
        self.getProgressBar().setValue(ricevuti)
    def getStopButton (self):
        return self.stopButton
    
    #azioni da eseguire prima della chiusura del programma
    def onClose(self):
        file = QtCore.QFile(http.getFileName())
        #applica opzione di ritornare  a edizione nazionale
        if settings.edizionePredefinita == 2:
            settings.edizione = "Nazionale"
        file.remove()
        print("file temporaneo rimosso")
    
class CustomButton(QtGui.QPushButton):
    def __init__(self,  parent = None):
        QtGui.QPushButton.__init__(self)
        self.paginaDesiderata = 100
    def setPaginaDesiderata(self,  pagina):
        self.paginaDesiderata = pagina
    #funzione che wrappa setText
    def setTextWithCheck(self,  testo):
        #nelle condizioni di default, pulsanti non hanno testo
        if testo.isEmpty():
            self.setText("configura")
        else:
            self.setText(testo)
    def mousePressEvent(self, event):
        if self.text() == 'configura':
            self.emit(QtCore.SIGNAL('configuraPreferiti'), True)            
        else:
            self.emit(QtCore.SIGNAL('vaiA'),  self.paginaDesiderata)

class GestioneConnessione(QtNetwork.QHttp):
    def __init__(self):
        QtNetwork.QHttp.__init__(self)
        #regionali
        #http://www.televideo.rai.it/televideo/pub/tt4web/Sardegna/page-100.png
        #http://www.televideo.rai.it/televideo/pub/tt4web/Marche/page-100.png
        self.file = QtCore.QTemporaryFile() #unico file temporaneo
        self.file.setAutoRemove(False) #lo rimuovo io in chiusura
        self.fileName = QtCore.QString()
        self.httpStatus = 0
        self.ricercaInCorso = False #è True quando sto cercando pagina successiva a una non trovata 
        #queste 2 variabili così se pagina non trovata, posso recuperare quella precedente, in caso utente clicchi No
        self.ultimaPaginaValida = 100
        self.ultimaSottopaginaValida = 1
	self.inAvanti = True #se sto andando in avanti o indietro, utile per cercare se pagina non trovata nella direzione corretta
        self.downloadInCorso = False #per disabilitare le azioni

        #settaggio proxy
        npq = QtNetwork.QNetworkProxyQuery(QtCore.QUrl("http://www.google.com"))
        listOfProxies = QtNetwork.QNetworkProxyFactory.systemProxyForQuery(npq)
        #print len(listOfProxies) 
        if settings.usaProxy == 2:
            self.setProxy(settings.hostProxy,  settings.portProxy,  settings.userNameProxy,  settings.passwordProxy)
        else:
            self.setProxy(listOfProxies[0])
        
        #segnali, qua perchè se no certe variabili non sono definite
        QtCore.QObject.connect(widget.buttonVai,  QtCore.SIGNAL('clicked ()'), self.preparaPagina)
        QtCore.QObject.connect(widget.pagina,  QtCore.SIGNAL('valueChanged (int)'),  self.preparaPagina)
        QtCore.QObject.connect(widget.sottopagina,  QtCore.SIGNAL('valueChanged (int)'),  self.caricaSottopagina)
        QtCore.QObject.connect(widget.homeButton,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.customButton1,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.customButton2,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.customButton3,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.customButton4,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.customButton5,  QtCore.SIGNAL('vaiA'), self.preparaPagina) 
        #QtCore.QObject.connect(widget.indietro,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        #QtCore.QObject.connect(widget.avanti,  QtCore.SIGNAL('vaiA'), self.preparaPagina)
        QtCore.QObject.connect(widget.saveButton,  QtCore.SIGNAL('clicked ()'), self.salvaPagina)   
    
    def avviaDownload(self,  url):
        self.downloadInCorso = True
        if self.file.open():
            self.fileName = self.file.fileName()
        if window.statusBar().currentMessage() != 'page not found':
            window.getStopButton().show()
            window.getProgressBar().show()
            window.statusBar().showMessage('downloading...')
        self.setHost(url.host(),  80)
        httpGetId = self.get(url.path(),  self.file)
        
    def preparaPagina(self,  paginaDiretta = None, avanti = None):
        #la prima pagina si chiama page-100.png, la seconda page-100.2.png
        #primo argomento edizione, secondo pagina, terzo sottopagina
        urlTemp = QtCore.QString("http://www.televideo.rai.it/televideo/pub/tt4web/%1/page-%2%3.png")

        #se non è vuoto, aggiorno il valore di avanti, se no mantengo il precedente
        if avanti is not None:
	    self.inAvanti = avanti
        #questo parametro per caricare una pagina da un pulsante
        if paginaDiretta is not None:
            widget.getPagina().setValue(paginaDiretta)
            widget.sottopagina.setValue(1)
            urlTemp2 = urlTemp.arg(settings.edizione).arg(QtCore.QString.number(paginaDiretta)).arg('')
        else:
            if widget.sottopagina.value() == 1:
                urlTemp2 = urlTemp.arg(settings.edizione).arg(QtCore.QString.number(widget.pagina.value())).arg('')
            else: 
                temp = QtCore.QString(".")
                temp.append(QtCore.QString.number(widget.sottopagina.value()))
                urlTemp2 = urlTemp.arg(settings.edizione).arg(widget.pagina.value()).arg(temp)
        self.avviaDownload(QtCore.QUrl(urlTemp2))
         
    #funzione che wrappa caricaPagina, perché il parametro ha significato diverso e quindi lo buttiamo    
    def caricaSottopagina (self, temp):
        self.preparaPagina(avanti = True)
        
    def downloadFinito(self, error):
        if window.statusBar().currentMessage() != 'page not found':
            window.statusBar().showMessage('done',  5000)
            window.updateProgressBar
            window.getProgressBar().hide()
            window.getStopButton().hide()
        if error:
            if self.error() == QtNetwork.QHttp.HostNotFound:
                #connessione assente
                window.statusBar().showMessage(http.errorString())
                return
            window.statusBar().showMessage(http.errorString())
            return
        self.file.close()
        image = QtGui.QImage()
        image.load(self.fileName)
        self.timer = None
        
        #auto refresh di una pagina
        if settings.refreshAutomatico == 2:
            self.timer = QtCore.QTimer()
            QtCore.QObject.connect(self.timer,  QtCore.SIGNAL('timeout ()'), self.preparaPagina)
            self.timer.start(settings.intervalloRefresh*1000)        #moltiplico per passare a ms
        
        if self.httpStatus == 404:
            if self.ricercaInCorso:
                if self.inAvanti:
                    self.preparaPagina((widget.pagina.value())+1, avanti = True) #carico direttamente pagina successiva inutile richiedere
                else:
                    self.preparaPagina((widget.pagina.value())-1, avanti = False) #carico direttamente pagina successiva inutile richiedere
                return
            if self.timer is not None:
                self.timer.stop() #se no ricarica anche se viene visualizzata MessageBox
            if settings.azionePaginaNonTrovata == 0: #verifica l'opzione apposita, qui è su Chiedi sempre
                answer = QtGui.QMessageBox.question(widget,   "Pagina non trovata",  "Vuoi cercare la prossima pagina esistente?\nPremi no per rimanere sulla pagina corrente",  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if answer == QtGui.QMessageBox.Yes:
                    #cerca prossima pagina
                    self.ricercaInCorso = True
                    if self.inAvanti:
                        self.preparaPagina((widget.pagina.value())+1, avanti = True)
                    else:
                        self.preparaPagina((widget.pagina.value())-1, avanti = False)
                    return
                else:
                    window.statusBar().clearMessage()        
                    window.statusBar().showMessage("page not found",  5000)
                    widget.getPagina().setValue(self.ultimaPaginaValida)
                    widget.getSottopagina().setValue(self.ultimaSottopaginaValida)
                    #preparaPagina(settings.pagIniziale)
                    return
            elif settings.azionePaginaNonTrovata == 1: #rimanere su pagina corrente, non chiedere
                    window.statusBar().clearMessage()        
                    window.statusBar().showMessage("page not found",  5000)
                    widget.getPagina().setValue(self.ultimaPaginaValida)
                    widget.getSottopagina().setValue(self.ultimaSottopaginaValida)
                    #preparaPagina(settings.pagIniziale)
                    return
            else: #vai a pagina successiva, non chiedere
                    self.ricercaInCorso = True
                    if self.inAvanti:
                        print("inAvanti")
                        self.preparaPagina((widget.pagina.value())+1, avanti = True)
                    else:
                        print("indietro")
                        self.preparaPagina((widget.pagina.value())-1, avanti=False)
                    return
        self.ricercaInCorso = False #se arrivi qua, pagina trovata, rimetto False
        widget.getIndietro().setPaginaDesiderata((widget.pagina.value())-1)
        widget.getAvanti().setPaginaDesiderata((widget.pagina.value())+1)        
        
        #questo per memorizzare ultima pagina cosi se nn trovo posso ritornare lì
        self.ultimaPaginaValida = widget.getPagina().value()
        self.ultimaSottopaginaValida = widget.getSottopagina().value()
        
        pixmap = QtGui.QPixmap.fromImage(image)
        widget.labelImage.setPixmap(pixmap)
        self.downloadInCorso = False
    
    def analizzaHeader(self,  header):
        self.httpStatus = header.statusCode()
    def salvaPagina(self):
        #apre finestra per scegliere dove salvare il file
        nomeDesiderato = QtGui.QFileDialog.getSaveFileName(widget,  "Scegli la posizione in cui salvare l'immagine",  "televideo.png",  "Image files (*.png)")
        if not nomeDesiderato.isEmpty():
            if (QtCore.QFile(nomeDesiderato)).exists():
                QtCore.QFile(nomeDesiderato).remove()
            if not self.file.copy(nomeDesiderato):
                QtGui.QMessageBox.critical(widget, "Errore",  "Impossibile salvare il file")
            else:
                window.statusBar().showMessage('file salvato')
    def getFileName(self):
        return self.fileName
    def isDownloadInCorso(self):
        return self.downloadInCorso
    def setDownloadFinito(self):
        self.downloadInCorso = False #in caso utente prema stop

class Grafica(QtGui.QWidget):
        def __init__(self):
             QtGui.QWidget.__init__(self)
             self.show()
             self.layout = QtGui.QGridLayout(self)
             #secondo layout, per fare stare + bottoni
             self.layoutSecondario = QtGui.QGridLayout()
             self.buttonVai = QtGui.QPushButton(self)
             
             #altrimenti non vede icone, aggiusto percorsi
             if sys.platform == "win32":
               dirTemp = QtCore.QString(winPath)
             else:
                dirTemp = QtCore.QString(directory)
             self.buttonVai.setIcon(QtGui.QIcon(dirTemp + "/icons/reload.png"))
             #self.buttonVai.setIconSize(QtCore.QSize(19, 19))
             self.buttonVai.setAutoDefault(True)
                         
             self.labelImage = QtGui.QLabel()
             self.labelImage.setText("No image")
             self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
             self.labelImage.show()            
             
             #self.layout.addWidget(self.buttonVai,  0,  2,  1,  1)
             self.layout.addWidget(self.labelImage,  1,  0,  1,  5)
            
             self.pagina = QtGui.QSpinBox()
             self.pagina.setRange(100,  899)
             self.pagina.setWrapping(True)
             self.pagina.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
             
            
             self.sottopagina = QtGui.QSpinBox()
             self.sottopagina.setRange(1,  99)
             self.sottopagina.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
                          
             if sys.platform == "win32":
                 self.layoutSecondario.addWidget(self.pagina,  0,  0)
                 self.layoutSecondario.addWidget(self.sottopagina,  0,  1)
             else:
                 self.layout.addWidget(self.pagina,  0,  0)
                 self.layoutSecondario.addWidget(self.sottopagina,  0,  0) 
             #pulsante per tornare indietro di una pag
             self.indietro = CustomButton()
             #self.indietro.setText('-')
             self.indietro.setIcon(QtGui.QIcon(dirTemp + "/icons/previous.png"))
             self.indietro.setPaginaDesiderata(self.pagina.value()-1)
            
             self.avanti = CustomButton()
             #self.avanti.setText('+')
             self.avanti.setIcon(QtGui.QIcon(dirTemp + "/icons/next.png"))
             self.avanti.setPaginaDesiderata(self.pagina.value()+1)
                          
             if sys.platform == "win32":
                self.layoutSecondario.addWidget(self.indietro,  0,  2)
                self.layoutSecondario.addWidget(self.buttonVai,  0,  3)
                self.layoutSecondario.addWidget(self.avanti,  0,  4)
             else:
                self.layoutSecondario.addWidget(self.indietro,  0,  1)
                self.layoutSecondario.addWidget(self.buttonVai,  0,  2)
                self.layoutSecondario.addWidget(self.avanti,  0,  3)

             self.homeButton = CustomButton()
             #self.homeButton.setText("&Home")
             self.homeButton.setIcon(QtGui.QIcon(dirTemp + "/icons/home.png"))
             self.homeButton.setToolTip("Apri la pagina iniziale")
             #self.homeButton.setIconSize(QtCore.QSize(19, 19))
             self.homeButton.setPaginaDesiderata(settings.pagIniziale)
             if sys.platform == "win32":
                 self.layoutSecondario.addWidget(self.homeButton,  0,  5)
             else:
                 self.layoutSecondario.addWidget(self.homeButton,  0,  4)
             
             self.saveButton = QtGui.QPushButton()
             self.saveButton.setIcon(QtGui.QIcon(dirTemp + "/icons/filesave.png"))
             self.saveButton.setToolTip("Salva la pagina corrente")
             if sys.platform == "win32":
                 self.layoutSecondario.addWidget(self.saveButton,  0,  6)
             else:
                 self.layoutSecondario.addWidget(self.saveButton,  0,  5)
             
             self.optionsButton = QtGui.QPushButton()
             self.optionsButton.setIcon(QtGui.QIcon(dirTemp + "/icons/preferences.png"))
             self.optionsButton.setToolTip("Apri la finestra delle opzioni")
             QtCore.QObject.connect(self.optionsButton,  QtCore.SIGNAL('clicked ()'), self.apriFinestraOpzioni)
             if sys.platform == "win32":
                 self.layoutSecondario.addWidget(self.optionsButton,  0,  7)
             else:
                 self.layoutSecondario.addWidget(self.optionsButton,  0,  6)             
             
             if sys.platform == "win32":
                 self.layout.addLayout(self.layoutSecondario,  0,  0,  1,  5)
             else:
                 self.layout.addLayout(self.layoutSecondario,  0,  1,  1,  4)
            
             self.customButton1 = CustomButton()
             self.customButton1.setTextWithCheck(settings.nomePagina1)
             self.customButton1.setPaginaDesiderata(settings.numeroPagina1)
             QtCore.QObject.connect(self.customButton1, QtCore.SIGNAL('configuraPreferiti'), self.apriFinestraOpzioni)
             self.customButton2 = CustomButton()
             self.customButton2.setTextWithCheck(settings.nomePagina2)
             self.customButton2.setPaginaDesiderata(settings.numeroPagina2)
             QtCore.QObject.connect(self.customButton2, QtCore.SIGNAL('configuraPreferiti'), self.apriFinestraOpzioni)       
             self.customButton3 = CustomButton()
             self.customButton3.setTextWithCheck(settings.nomePagina3)
             self.customButton3.setPaginaDesiderata(settings.numeroPagina3)
             QtCore.QObject.connect(self.customButton3, QtCore.SIGNAL('configuraPreferiti ()'), self.apriFinestraOpzioni)       
             self.customButton4 = CustomButton()
             self.customButton4.setTextWithCheck(settings.nomePagina4)
             self.customButton4.setPaginaDesiderata(settings.numeroPagina4)
             QtCore.QObject.connect(self.customButton4, QtCore.SIGNAL('configuraPreferiti'), self.apriFinestraOpzioni)
             self.customButton5 = CustomButton()
             self.customButton5.setTextWithCheck(settings.nomePagina5)
             self.customButton5.setPaginaDesiderata(settings.numeroPagina5)
             QtCore.QObject.connect(self.customButton5, QtCore.SIGNAL('configuraPreferiti'), self.apriFinestraOpzioni)
             self.layout.addWidget(self.customButton1,  2,  0)
             self.layout.addWidget(self.customButton2,  2,  1)
             self.layout.addWidget(self.customButton3,  2,  2)
             self.layout.addWidget(self.customButton4,  2,  3)
             self.layout.addWidget(self.customButton5,  2,  4)
             
             #scorciatoie da tastiera
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Minus),  self.getIndietro(), self.vaiIndietro)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Plus),  self.getAvanti(), self.vaiAvanti)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_1),  self.getCustomButton1(), self.vaiButton1)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_2),  self.getCustomButton2(), self.vaiButton2)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_3),  self.getCustomButton3(), self.vaiButton3)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_4),  self.getCustomButton4(), self.vaiButton4)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_5),  self.getCustomButton5(), self.vaiButton5)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_Plus),  self.getSottopagina(), self.sottopaginaSucc)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_Minus),  self.getSottopagina(), self.sottopaginaPrec)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL  + QtCore.Qt.Key_H),  self.getSottopagina(), self.pagIniziale)
             QtGui.QShortcut(QtGui.QKeySequence.Refresh,  self.getSottopagina(), self.aggiorna)
             QtGui.QShortcut(QtGui.QKeySequence.Save,  self.getSottopagina(), self.salva)
             QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape),  self.getSottopagina(), self.stop)
        
        def aggiornaPulsanti(self):
             self.customButton1.setTextWithCheck(settings.nomePagina1)
             self.customButton1.setPaginaDesiderata(settings.numeroPagina1)
             self.customButton2.setTextWithCheck(settings.nomePagina2)
             self.customButton2.setPaginaDesiderata(settings.numeroPagina2)
             self.customButton3.setTextWithCheck(settings.nomePagina3)
             self.customButton3.setPaginaDesiderata(settings.numeroPagina3)
             self.customButton4.setTextWithCheck(settings.nomePagina4)
             self.customButton4.setPaginaDesiderata(settings.numeroPagina4)
             self.customButton5.setTextWithCheck(settings.nomePagina5)
             self.customButton5.setPaginaDesiderata(settings.numeroPagina5)
             self.homeButton.setPaginaDesiderata(settings.pagIniziale)
             
        def apriFinestraOpzioni(self, tabPreferiti = False):
            w = OptionsWindow(relative = relative, tabPreferiti = tabPreferiti)
            w.exec_()
            #aggiorno pulsanti con nuove opzioni
            self.aggiornaPulsanti()
                
        def getPagina(self):
            return self.pagina
        def getSottopagina(self):
            return self.sottopagina
        def getIndietro(self):
            return self.indietro
        def getAvanti(self):
            return self.avanti
        def getLabelImage(self):
            return self.labelImage       
        def getButtonVai(self):
            return self.buttonVai
        def getCustomButton1(self):
            return self.customButton1
        def getCustomButton2(self):
            return self.customButton2
        def getCustomButton3(self):
            return self.customButton3
        def getCustomButton4(self):
            return self.customButton4
        def getCustomButton5(self):
            return self.customButton5
            
        def vaiIndietro(self):
            if not http.isDownloadInCorso():
                http.preparaPagina((widget.pagina.value())-1, avanti = False)      
        def vaiAvanti(self):
            if not http.isDownloadInCorso():
                http.preparaPagina((widget.pagina.value())+1, avanti = True)
        def vaiButton1(self):
            self.getCustomButton1().emit(QtCore.SIGNAL('vaiA'),  self.getCustomButton1().paginaDesiderata)
        def vaiButton2(self):
            self.getCustomButton2().emit(QtCore.SIGNAL('vaiA'),  self.getCustomButton2().paginaDesiderata)
        def vaiButton3(self):
            self.getCustomButton3().emit(QtCore.SIGNAL('vaiA'),  self.getCustomButton3().paginaDesiderata)
        def vaiButton4(self):
            self.getCustomButton4().emit(QtCore.SIGNAL('vaiA'),  self.getCustomButton4().paginaDesiderata)
        def vaiButton5(self):
            self.getCustomButton5().emit(QtCore.SIGNAL('vaiA'),  self.getCustomButton5().paginaDesiderata)
        def sottopaginaSucc(self):
            self.getSottopagina().setValue(self.getSottopagina().value()+1)
        def sottopaginaPrec(self):
            self.getSottopagina().setValue(self.getSottopagina().value()-1)
        def pagIniziale(self):
            if not http.isDownloadInCorso():
                self.getPagina().setValue(settings.pagIniziale)
        def aggiorna(self):
            if not http.isDownloadInCorso():
                QtCore.QObject.emit(self.getButtonVai(),  QtCore.SIGNAL('clicked()'))
        def salva(self):
            http.salvaPagina()
        def stop(self):
            http.abort()
            http.setDownloadFinito()
            #ripristino il valore della pagina su cui ero, visto che il caricamento è stato interrotto
            self.getPagina().setValue(http.ultimaPaginaValida)
            self.getSottopagina().setValue(http.ultimaSottopaginaValida)
            window.statusBar().showMessage('Stopped')

pathRelativo = QtCore.QDir.homePath().append("/.televideo")
#per le opzioni, se false è nella stessa cartella del programma, se no in .config nella home
relative = False
app = QtGui.QApplication(sys.argv)
#mi prendo percorso applicazione, per memorizzare file lì, se no si prende un path diverso a seconda di dove lanci app
path = app.arguments()
workingPath = QtCore.QDir()

if sys.platform == "win32":
    print "windows"
    # e aggiusto path
    winPath = QtCore.QString(app.applicationDirPath())
    workingPath.setCurrent(winPath)
else:
    print(sys.platform)
    filePathInfo = QtCore.QFileInfo(path[0])
    directory = filePathInfo.path()
    workingPath.setCurrent(directory)
    
#print(app.applicationDirPath())

#questo se il programma è installato in una posizione non scrivibile, quindi le immagini le salva in una cartella della home
testFile = QtCore.QFileInfo("COPYING")
if not testFile.isWritable():
    dir = QtCore.QDir(pathRelativo)
    if not dir.exists():
        dir.mkpath(pathRelativo)
    workingPath.setCurrent(pathRelativo)
    relative = True
    print("Non posso scrivere: le immagine verranno memorizzate nella cartella .televideo della home su Linux o nel Registro in Windows")

settings = MySettings(relative)

widget = Grafica()
window = MainWindow(widget)
window.show()
window.setCentralWidget(widget)

http = GestioneConnessione()

#apre pagina iniziale
widget.getPagina().setValue(settings.pagIniziale)
QtCore.QObject.emit(widget.getButtonVai(),  QtCore.SIGNAL('clicked()'))

#QtCore.QObject.connect(a, QtCore.SIGNAL("QtSig()"), pyFunction)
#QtCore.QObject.connect(a, QtCore.SIGNAL("QtSig()"), pyClass.pyMethod)
#QtCore.QObject.connect(a, QtCore.SIGNAL("QtSig()"), b, QtCore.SLOT("QtSlot()"))
#QtCore.QObject.connect(a, QtCore.SIGNAL("PySig()"), b, QtCore.SLOT("QtSlot()"))
#QtCore.QObject.connect(a, QtCore.SIGNAL("PySig"), pyFunction)

#segnali per il download
QtCore.QObject.connect(http,  QtCore.SIGNAL('responseHeaderReceived (const QHttpResponseHeader&)'), http.analizzaHeader)
QtCore.QObject.connect(http,  QtCore.SIGNAL('done(bool)'), http.downloadFinito)
QtCore.QObject.connect(http,  QtCore.SIGNAL('dataReadProgress (int, int)'), window.updateProgressBar)
QtCore.QObject.connect(app,  QtCore.SIGNAL('aboutToQuit ()'), window.onClose)

QtCore.QObject.connect(window.stopButton, QtCore.SIGNAL('clicked ()'), widget.stop)
QtCore.QObject.connect(widget.indietro,  QtCore.SIGNAL('vaiA'), widget.vaiIndietro)
QtCore.QObject.connect(widget.avanti,  QtCore.SIGNAL('vaiA'), widget.vaiAvanti)

#brutto hack che serve perchè se salvo su registro la pagina 100 non me la carica al primo colpo
if settings.pagIniziale == 100:
	widget.getCustomButton1().emit(QtCore.SIGNAL('vaiA'),  settings.pagIniziale)
sys.exit(app.exec_())
