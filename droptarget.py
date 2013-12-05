# -*- coding: utf-8 -*-

#Copyright (C)2010 Abhinandh <abhinandh@gmail.com>
#This Program in licenser under General Public License Ver 3

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from trayicon import TrayIcon

class DropWidget(QLabel):

    hidden = True

    def __init__(self, parent=None):
        super(QWidget,self).__init__(parent)
        self.setWindowFlags(Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.signals = self.Signals()
        self.setAcceptDrops(1)
        self.resize(QSize(217,68))
        self.setAlignment(Qt.AlignCenter)
        self.setPixmap(QPixmap(':/bg/cloudapp_droptarget.png'))

        self.trayIcon = TrayIcon()
        self.trayIcon.show()
        self.trayIcon.activated[QSystemTrayIcon.ActivationReason].connect(self.trayActivated)
        self.signals.itemDropped[str].connect(self.trayIcon.apiHandle.addItem)

        self.trayIcon.apiHandle.pdialog.voffsetSlider.valueChanged[int].connect(self.vmove)
        self.move(qApp.desktop().screenGeometry().width()-217,self.trayIcon.apiHandle.pdialog.settings['drop_topoffset'])

    def vmove(self, val):
        self.move(self.x(),val)

    def dragEnterEvent(self, event):
        if self.trayIcon.apiHandle.connected:
            event.acceptProposedAction()

    def dropEvent(self, event):
        mimeData = event.mimeData()
        pos = event.pos()
        if pos.x() > 25:
            if mimeData.hasUrls():
                for url in mimeData.urls():
                    if url.scheme() in ('file', 'http','https','ftp'):
                        self.signals.itemDropped.emit(url.toString())
                        self.animOpacity()

    def trayActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.toggle()
        elif reason == QSystemTrayIcon.Context:
            if hasattr(self.trayIcon, "deleteAction"):
                deleteCheckBox = self.trayIcon.deleteAction.widget.checkBox
                if deleteCheckBox.isChecked():
                    deleteCheckBox.toggle()

    def animOpacity(self):
        if self.hidden:
            self.show()
        else:
            self.hide()

        self.hidden = not self.hidden

    def toggle(self):
        self.animOpacity()

    class Signals(QObject):
        itemDropped = pyqtSignal(str)
