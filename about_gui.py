# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutzrhrxY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
import wipm_rc


class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName("About")
        About.resize(424, 255)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.header_logo = QLabel(About)
        self.header_logo.setObjectName("header_logo")
        self.header_logo.setMaximumSize(QSize(97, 35))
        self.header_logo.setPixmap(QPixmap(":/img/resources/logo_latch.svg"))
        self.header_logo.setScaledContents(True)
        self.header_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.header_logo)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.description = QLabel(About)
        self.description.setObjectName("description")
        font = QFont()
        font.setFamilies(["Telefonica Sans"])
        self.description.setFont(font)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setWordWrap(True)
        self.description.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.description)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.footer = QLabel(About)
        self.footer.setObjectName("footer")
        self.footer.setFont(font)

        self.verticalLayout.addWidget(self.footer)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)

    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", "About WiPM", None))
        self.header_logo.setText("")
        self.description.setText(
            QCoreApplication.translate(
                "About",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Telefonica Sans'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The <span style=" font-style:italic;">WordPress in Paranoid Mode</span> installer allows you to remotely install this utility to protect your WordPress database.</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px;'
                ' margin-right:0px; -qt-block-indent:0; text-indent:0px;">You can find more information about the project <a href="https://github.com/Telefonica/latch-plugin-wipm"><span style=" text-decoration: underline; color:#094fd1;">here</span></a>.</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Installer image generated with <span style=" font-style:italic;">stable diffusion</span>.</p></body></html>',
                None,
            )
        )
        self.footer.setText(
            QCoreApplication.translate(
                "About",
                "<html><head/><body><p align=\"center\">Made with <span style=\" font-family:'Poppins','sans-serif'; font-size:14pt; color:#ff2600;\">\u2665 </span>by Ideas Locas</p></body></html>",
                None,
            )
        )

    # retranslateUi
