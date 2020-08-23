# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\solutionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_solutionWidget(object):
    def setupUi(self, solutionWidget):
        solutionWidget.setObjectName("solutionWidget")
        solutionWidget.resize(564, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(solutionWidget.sizePolicy().hasHeightForWidth())
        solutionWidget.setSizePolicy(sizePolicy)
        solutionWidget.setMinimumSize(QtCore.QSize(0, 245))
        self.solution = QtWidgets.QWidget(solutionWidget)
        self.solution.setGeometry(QtCore.QRect(10, 10, 551, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solution.sizePolicy().hasHeightForWidth())
        self.solution.setSizePolicy(sizePolicy)
        self.solution.setMinimumSize(QtCore.QSize(0, 241))
        self.solution.setBaseSize(QtCore.QSize(0, 241))
        self.solution.setAutoFillBackground(False)
        self.solution.setObjectName("solution")
        self.pick1Avatar = QtWidgets.QGraphicsView(self.solution)
        self.pick1Avatar.setGeometry(QtCore.QRect(0, 0, 81, 81))
        self.pick1Avatar.setObjectName("pick1Avatar")
        self.commentBrowser = QtWidgets.QTextBrowser(self.solution)
        self.commentBrowser.setGeometry(QtCore.QRect(0, 120, 441, 111))
        self.commentBrowser.setMinimumSize(QtCore.QSize(0, 111))
        self.commentBrowser.setObjectName("commentBrowser")
        self.lockSolutionCheckBox = QtWidgets.QCheckBox(self.solution)
        self.lockSolutionCheckBox.setEnabled(True)
        self.lockSolutionCheckBox.setGeometry(QtCore.QRect(450, 90, 88, 23))
        self.lockSolutionCheckBox.setObjectName("lockSolutionCheckBox")
        self.pick4Star = QtWidgets.QGraphicsView(self.solution)
        self.pick4Star.setGeometry(QtCore.QRect(270, 90, 81, 21))
        self.pick4Star.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick4Star.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick4Star.setObjectName("pick4Star")
        self.pick2Star = QtWidgets.QGraphicsView(self.solution)
        self.pick2Star.setGeometry(QtCore.QRect(90, 90, 81, 21))
        self.pick2Star.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick2Star.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick2Star.setObjectName("pick2Star")
        self.pick2Avatar = QtWidgets.QGraphicsView(self.solution)
        self.pick2Avatar.setGeometry(QtCore.QRect(90, 0, 81, 81))
        self.pick2Avatar.setObjectName("pick2Avatar")
        self.dislikeLabel = QtWidgets.QLabel(self.solution)
        self.dislikeLabel.setGeometry(QtCore.QRect(450, 30, 16, 16))
        self.dislikeLabel.setObjectName("dislikeLabel")
        self.pick3Star = QtWidgets.QGraphicsView(self.solution)
        self.pick3Star.setGeometry(QtCore.QRect(180, 90, 81, 21))
        self.pick3Star.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick3Star.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick3Star.setObjectName("pick3Star")
        self.pick5Star = QtWidgets.QGraphicsView(self.solution)
        self.pick5Star.setGeometry(QtCore.QRect(360, 90, 81, 21))
        self.pick5Star.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick5Star.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick5Star.setObjectName("pick5Star")
        self.pick5Avatar = QtWidgets.QGraphicsView(self.solution)
        self.pick5Avatar.setGeometry(QtCore.QRect(360, 0, 81, 81))
        self.pick5Avatar.setObjectName("pick5Avatar")
        self.likeLabel = QtWidgets.QLabel(self.solution)
        self.likeLabel.setGeometry(QtCore.QRect(450, 10, 16, 16))
        self.likeLabel.setObjectName("likeLabel")
        self.pick4Avatar = QtWidgets.QGraphicsView(self.solution)
        self.pick4Avatar.setGeometry(QtCore.QRect(270, 0, 81, 81))
        self.pick4Avatar.setObjectName("pick4Avatar")
        self.pick1Star = QtWidgets.QGraphicsView(self.solution)
        self.pick1Star.setGeometry(QtCore.QRect(0, 90, 81, 21))
        self.pick1Star.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick1Star.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pick1Star.setObjectName("pick1Star")
        self.pick3Avatar = QtWidgets.QGraphicsView(self.solution)
        self.pick3Avatar.setGeometry(QtCore.QRect(180, 0, 81, 81))
        self.pick3Avatar.setObjectName("pick3Avatar")
        self.label = QtWidgets.QLabel(self.solution)
        self.label.setGeometry(QtCore.QRect(450, 30, 41, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.upCount = QtWidgets.QLabel(self.solution)
        self.upCount.setGeometry(QtCore.QRect(470, 10, 41, 16))
        self.upCount.setObjectName("upCount")
        self.downCount = QtWidgets.QLabel(self.solution)
        self.downCount.setGeometry(QtCore.QRect(470, 30, 41, 16))
        self.downCount.setObjectName("downCount")
        self.favorSolutionButton = QtWidgets.QPushButton(self.solution)
        self.favorSolutionButton.setEnabled(False)
        self.favorSolutionButton.setGeometry(QtCore.QRect(450, 120, 51, 23))
        self.favorSolutionButton.setObjectName("favorSolutionButton")

        self.retranslateUi(solutionWidget)
        QtCore.QMetaObject.connectSlotsByName(solutionWidget)

    def retranslateUi(self, solutionWidget):
        _translate = QtCore.QCoreApplication.translate
        solutionWidget.setWindowTitle(_translate("solutionWidget", "Form"))
        self.lockSolutionCheckBox.setText(_translate("solutionWidget", "锁定此阵容"))
        self.dislikeLabel.setText(_translate("solutionWidget", "踩"))
        self.likeLabel.setText(_translate("solutionWidget", "赞"))
        self.upCount.setText(_translate("solutionWidget", "<html><head/><body><p><span style=\" color:#009309;\">赞数</span></p></body></html>"))
        self.downCount.setText(_translate("solutionWidget", "<html><head/><body><p><span style=\" color:#990000;\">踩数</span></p></body></html>"))
        self.favorSolutionButton.setText(_translate("solutionWidget", "收藏"))
