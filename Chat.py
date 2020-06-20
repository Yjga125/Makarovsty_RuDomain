# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(814, 605)
        Chat.setStyleSheet(u"background:#fffffa;\n"
"\n"
"QToolButton{\n"
"border-radius:30px;\n"
"width:100px;\n"
"height:100px ;\n"
"}\n"
"QListWidget{\n"
"background:#FFF;\n"
"font-size:15px;\n"
"\n"
"}\n"
"QLabel{\n"
"font-size:15px;\n"
"}")
        self.centralwidget = QWidget(Chat)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.contacts = QListWidget(self.centralwidget)
        QListWidgetItem(self.contacts)
        QListWidgetItem(self.contacts)
        QListWidgetItem(self.contacts)
        self.contacts.setObjectName(u"contacts")
        self.contacts.setMaximumSize(QSize(400, 16777215))
        self.contacts.setStyleSheet(u"background:#fff;")

        self.verticalLayout.addWidget(self.contacts)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(50, 50))
        self.add.setStyleSheet(u"background:#000;\n"
"border-radius:25px;\n"
"max-width:50px;\n"
"min-width:50px;\n"
"max-height:50px;\n"
"min-heigth:50px;\n"
"color:#fff;\n"
"font-size:25px;")

        self.verticalLayout_2.addWidget(self.add)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(9)
        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setStyleSheet(u"background:#000;\n"
"font: 8pt \"Arial\";\n"
"font: 87 20pt \"Arial Black\";\n"
"border-radius:25px;\n"
"max-width:50px;\n"
"min-width:50px;\n"
"max-height:50px;\n"
"min-heigth:50px;\n"
"color:#fff;\n"
"font-size:35px;\n"
"text-align:center;\n"
"padding:0;")

        self.gridLayout.addWidget(self.send, 2, 3, 1, 1)

        self.messages = QTextBrowser(self.centralwidget)
        self.messages.setObjectName(u"messages")
        self.messages.setStyleSheet(u"background:#fff")

        self.gridLayout.addWidget(self.messages, 1, 2, 1, 2)

        self.nextmessage = QTextEdit(self.centralwidget)
        self.nextmessage.setObjectName(u"nextmessage")
        self.nextmessage.setMaximumSize(QSize(16777215, 50))
        self.nextmessage.setStyleSheet(u"background:#fff")

        self.gridLayout.addWidget(self.nextmessage, 2, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        Chat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Chat", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))

        __sortingEnabled = self.contacts.isSortingEnabled()
        self.contacts.setSortingEnabled(False)
        ___qlistwidgetitem = self.contacts.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Chat", u"\u043a\u0442\u043e-\u0442\u043e1@\u043f\u043e\u0447\u0442\u0430.\u0440\u0444", None));
        ___qlistwidgetitem1 = self.contacts.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Chat", u"\u043a\u0442\u043e-\u0442\u043e2@\u043f\u043e\u0447\u0442\u0430.\u0440\u0444", None));
        ___qlistwidgetitem2 = self.contacts.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Chat", u"\u043a\u0442\u043e-\u0442\u043e3@\u043f\u043e\u0447\u0442\u0430.\u0440\u0444", None));
        self.contacts.setSortingEnabled(__sortingEnabled)

        self.add.setText(QCoreApplication.translate("Chat", u"\u271a", None))
        self.send.setText(QCoreApplication.translate("Chat", u"\u25b7", None))
        self.label_2.setText(QCoreApplication.translate("Chat", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

