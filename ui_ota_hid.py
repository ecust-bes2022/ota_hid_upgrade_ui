# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ota_hid.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QProgressBar,
    QSizePolicy, QSpacerItem, QTimeEdit, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, LineEdit, PrimaryPushButton)

class Ui_ota_tota_hid(object):
    def setupUi(self, ota_tota_hid):
        if not ota_tota_hid.objectName():
            ota_tota_hid.setObjectName(u"ota_tota_hid")
        ota_tota_hid.resize(712, 262)
        self.verticalLayout = QVBoxLayout(ota_tota_hid)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.widget = QWidget(ota_tota_hid)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = BodyLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_bin_path = LineEdit(self.widget)
        self.line_bin_path.setObjectName(u"line_bin_path")
        self.line_bin_path.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout.addWidget(self.line_bin_path)

        self.btn_browse = PrimaryPushButton(self.widget)
        self.btn_browse.setObjectName(u"btn_browse")

        self.horizontalLayout.addWidget(self.btn_browse)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(ota_tota_hid)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.ckbox_log_switch = CheckBox(self.widget_2)
        self.ckbox_log_switch.setObjectName(u"ckbox_log_switch")
        self.ckbox_log_switch.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.ckbox_log_switch)

        self.line_log_path = LineEdit(self.widget_2)
        self.line_log_path.setObjectName(u"line_log_path")
        self.line_log_path.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.line_log_path)

        self.btn_log_browse = PrimaryPushButton(self.widget_2)
        self.btn_log_browse.setObjectName(u"btn_log_browse")

        self.horizontalLayout_2.addWidget(self.btn_log_browse)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(ota_tota_hid)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = BodyLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_vid = LineEdit(self.widget_3)
        self.line_vid.setObjectName(u"line_vid")
        self.line_vid.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.line_vid)

        self.label_3 = BodyLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_pid = LineEdit(self.widget_3)
        self.line_pid.setObjectName(u"line_pid")
        self.line_pid.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_pid.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.line_pid)

        self.label_4 = BodyLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.line_work_interval = LineEdit(self.widget_3)
        self.line_work_interval.setObjectName(u"line_work_interval")
        self.line_work_interval.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.line_work_interval)

        self.label_5 = BodyLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.line_packet_interval = LineEdit(self.widget_3)
        self.line_packet_interval.setObjectName(u"line_packet_interval")
        self.line_packet_interval.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.horizontalLayout_3.addWidget(self.line_packet_interval)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(ota_tota_hid)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_6 = BodyLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_total_bins = BodyLabel(self.widget_4)
        self.label_total_bins.setObjectName(u"label_total_bins")

        self.horizontalLayout_4.addWidget(self.label_total_bins)

        self.horizontalSpacer_2 = QSpacerItem(91, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.timeEdit = QTimeEdit(self.widget_4)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.timeEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.timeEdit.setStyleSheet(u"")
        self.timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_4.addWidget(self.timeEdit)

        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_index = BodyLabel(self.widget_4)
        self.label_index.setObjectName(u"label_index")

        self.horizontalLayout_4.addWidget(self.label_index)

        self.label_sending_index = BodyLabel(self.widget_4)
        self.label_sending_index.setObjectName(u"label_sending_index")

        self.horizontalLayout_4.addWidget(self.label_sending_index)

        self.horizontalSpacer_4 = QSpacerItem(90, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(ota_tota_hid)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, 9)
        self.progressBar_ota = QProgressBar(self.widget_5)
        self.progressBar_ota.setObjectName(u"progressBar_ota")
        self.progressBar_ota.setValue(0)

        self.horizontalLayout_5.addWidget(self.progressBar_ota)

        self.btn_upgrade = PrimaryPushButton(self.widget_5)
        self.btn_upgrade.setObjectName(u"btn_upgrade")

        self.horizontalLayout_5.addWidget(self.btn_upgrade)


        self.verticalLayout.addWidget(self.widget_5)


        self.retranslateUi(ota_tota_hid)

        QMetaObject.connectSlotsByName(ota_tota_hid)
    # setupUi

    def retranslateUi(self, ota_tota_hid):
        ota_tota_hid.setWindowTitle(QCoreApplication.translate("ota_tota_hid", u"Bes Usb Hid Ota Upgrade Tool", None))
        self.label.setText(QCoreApplication.translate("ota_tota_hid", u"bin path", None))
        self.btn_browse.setText(QCoreApplication.translate("ota_tota_hid", u"Browse", None))
        self.ckbox_log_switch.setText(QCoreApplication.translate("ota_tota_hid", u"log path", None))
        self.btn_log_browse.setText(QCoreApplication.translate("ota_tota_hid", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("ota_tota_hid", u"vid hex", None))
        self.label_3.setText(QCoreApplication.translate("ota_tota_hid", u"pid hex", None))
        self.label_4.setText(QCoreApplication.translate("ota_tota_hid", u"work interval", None))
        self.label_5.setText(QCoreApplication.translate("ota_tota_hid", u"packet interval", None))
        self.label_6.setText(QCoreApplication.translate("ota_tota_hid", u"total:", None))
        self.label_total_bins.setText(QCoreApplication.translate("ota_tota_hid", u"0", None))
        self.label_index.setText(QCoreApplication.translate("ota_tota_hid", u"sending:", None))
        self.label_sending_index.setText(QCoreApplication.translate("ota_tota_hid", u"0", None))
        self.btn_upgrade.setText(QCoreApplication.translate("ota_tota_hid", u"Upgrade", None))
    # retranslateUi

