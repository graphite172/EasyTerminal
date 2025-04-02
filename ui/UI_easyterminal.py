# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_easyterminal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QListView, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_EasyTerminal(object):
    def setupUi(self, EasyTerminal):
        if not EasyTerminal.objectName():
            EasyTerminal.setObjectName(u"EasyTerminal")
        EasyTerminal.resize(446, 299)
        EasyTerminal.setMouseTracking(False)
        self.centralwidget = QWidget(EasyTerminal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gr_drivelist = QGroupBox(self.centralwidget)
        self.gr_drivelist.setObjectName(u"gr_drivelist")
        self.gr_drivelist.setGeometry(QRect(226, 10, 201, 261))
        self.btn_tmopen = QPushButton(self.gr_drivelist)
        self.btn_tmopen.setObjectName(u"btn_tmopen")
        self.btn_tmopen.setGeometry(QRect(106, 220, 81, 30))
        self.list_drive = QListView(self.gr_drivelist)
        self.list_drive.setObjectName(u"list_drive")
        self.list_drive.setGeometry(QRect(10, 20, 181, 191))
        self.btn_find_path = QPushButton(self.gr_drivelist)
        self.btn_find_path.setObjectName(u"btn_find_path")
        self.btn_find_path.setGeometry(QRect(18, 220, 81, 30))
        self.gr_toollist = QGroupBox(self.centralwidget)
        self.gr_toollist.setObjectName(u"gr_toollist")
        self.gr_toollist.setGeometry(QRect(10, 10, 201, 261))
        self.btn_installtm = QPushButton(self.gr_toollist)
        self.btn_installtm.setObjectName(u"btn_installtm")
        self.btn_installtm.setGeometry(QRect(8, 20, 181, 41))
        self.btn_installgitbash = QPushButton(self.gr_toollist)
        self.btn_installgitbash.setObjectName(u"btn_installgitbash")
        self.btn_installgitbash.setGeometry(QRect(9, 60, 181, 41))
        self.btn_installpowershell = QPushButton(self.gr_toollist)
        self.btn_installpowershell.setObjectName(u"btn_installpowershell")
        self.btn_installpowershell.setGeometry(QRect(10, 100, 181, 41))
        self.btn_installPython = QPushButton(self.gr_toollist)
        self.btn_installPython.setObjectName(u"btn_installPython")
        self.btn_installPython.setGeometry(QRect(10, 140, 181, 41))
        EasyTerminal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(EasyTerminal)
        self.statusbar.setObjectName(u"statusbar")
        EasyTerminal.setStatusBar(self.statusbar)

        self.retranslateUi(EasyTerminal)

        QMetaObject.connectSlotsByName(EasyTerminal)
    # setupUi

    def retranslateUi(self, EasyTerminal):
        EasyTerminal.setWindowTitle(QCoreApplication.translate("EasyTerminal", u"EasyTerminal", None))
        self.gr_drivelist.setTitle(QCoreApplication.translate("EasyTerminal", u"Drive Box", None))
        self.btn_tmopen.setText(QCoreApplication.translate("EasyTerminal", u"\ud130\ubbf8\ub110 \uc5f4\uae30", None))
        self.btn_find_path.setText(QCoreApplication.translate("EasyTerminal", u"\uacbd\ub85c \ucc3e\uae30", None))
        self.gr_toollist.setTitle(QCoreApplication.translate("EasyTerminal", u"Tool Box", None))
        self.btn_installtm.setText(QCoreApplication.translate("EasyTerminal", u"Windows Terminal \uc124\uce58/\uc5c5\ub370", None))
        self.btn_installgitbash.setText(QCoreApplication.translate("EasyTerminal", u"Git Bash \uc124\uce58/\uc5c5\ub370\uc774\ud2b8", None))
        self.btn_installpowershell.setText(QCoreApplication.translate("EasyTerminal", u"Powershell \uc124\uce58/\uc5c5\ub370\uc774\ud2b8", None))
        self.btn_installPython.setText(QCoreApplication.translate("EasyTerminal", u"Python LTS \uc124\uce58/\uc5c5\ub370\uc774\ud2b8", None))
    # retranslateUi

