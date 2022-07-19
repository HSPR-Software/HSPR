from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 891)
        MainWindow.setStyleSheet("#QWidget#centralwidget {background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(0, 116, 183, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        btn_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        btn_policy.setHorizontalStretch(0)
        btn_policy.setVerticalStretch(0)

        self.upload_button = QtWidgets.QPushButton(self.centralwidget)
        btn_policy.setHeightForWidth(self.upload_button.sizePolicy().hasHeightForWidth())
        self.upload_lb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_hb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_adb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_button.setSizePolicy(btn_policy)
        self.upload_lb_btn.setSizePolicy(btn_policy)
        self.upload_hb_btn.setSizePolicy(btn_policy)
        self.upload_adb_btn.setSizePolicy(btn_policy)
        self.upload_button.setStyleSheet("\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color:#60a3d9;\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.upload_lb_btn.setStyleSheet("\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color:#60a3d9;\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.upload_hb_btn.setStyleSheet("\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color:#60a3d9;\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.upload_adb_btn.setStyleSheet("\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color:#60a3d9;\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.upload_button.setObjectName("upload_button")
        self.upload_lb_btn.setObjectName("lb_button")
        self.upload_hb_btn.setObjectName("hb_button")
        self.upload_adb_btn.setObjectName("adb_button")

        self.horizontalLayout_5.addWidget(self.upload_button)
        self.horizontalLayout_5.addWidget(self.upload_lb_btn)
        self.horizontalLayout_5.addWidget(self.upload_hb_btn)
        self.horizontalLayout_5.addWidget(self.upload_adb_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.clear_loadeddata_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_loadeddata_btn.setSizePolicy(btn_policy)
        self.clear_loadeddata_btn.setStyleSheet("\n"
                                        "QPushButton:pressed {\n"
                                        "   background-color:#60a3d9;\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.clear_loadeddata_btn.setObjectName("clear_loadeddata_btn")
        self.verticalLayout.addWidget(self.clear_loadeddata_btn)

        self.label_upload = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_upload.sizePolicy().hasHeightForWidth())
        self.label_upload.setSizePolicy(sizePolicy)
        self.label_upload.setText("")
        self.label_upload.setObjectName("label_upload")
        self.verticalLayout.addWidget(self.label_upload)
        self.gridLayout_parameters = QtWidgets.QGridLayout()
        self.gridLayout_parameters.setHorizontalSpacing(10)
        self.gridLayout_parameters.setVerticalSpacing(25)
        self.gridLayout_parameters.setObjectName("gridLayout_parameters")
        self.label_hb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_hb.setFont(font)
        self.label_hb.setObjectName("label_hb")
        self.gridLayout_parameters.addWidget(self.label_hb, 3, 0, 1, 1)
        self.height_hb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_hb.sizePolicy().hasHeightForWidth())
        self.height_hb.setSizePolicy(sizePolicy)
        self.height_hb.setStyleSheet("QLineEdit {\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 1px;\n"
                                     "    border-radius: 8px;\n"
                                     "    min-width: 4em;\n"
                                     "    padding: 3px;\n"
                                     "}\n"
                                     "")
        self.height_hb.setObjectName("height_hb")
        self.gridLayout_parameters.addWidget(self.height_hb, 3, 1, 1, 1)
        self.width_lb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_lb.sizePolicy().hasHeightForWidth())
        self.width_lb.setSizePolicy(sizePolicy)
        self.width_lb.setStyleSheet("QLineEdit {\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 1px;\n"
                                    "    border-radius: 8px;\n"
                                    "    min-width: 4em;\n"
                                    "    padding: 3px;\n"
                                    "}\n"
                                    "")
        self.width_lb.setObjectName("width_lb")
        self.gridLayout_parameters.addWidget(self.width_lb, 2, 2, 1, 1)
        self.label_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_lb.setFont(font)
        self.label_lb.setObjectName("label_lb")
        self.gridLayout_parameters.addWidget(self.label_lb, 2, 0, 1, 1)
        self.width_hb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_hb.sizePolicy().hasHeightForWidth())
        self.width_hb.setSizePolicy(sizePolicy)
        self.width_hb.setStyleSheet("QLineEdit {\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 1px;\n"
                                    "    border-radius: 8px;\n"
                                    "    min-width: 4em;\n"
                                    "    padding: 3px;\n"
                                    "}\n"
                                    "")
        self.width_hb.setObjectName("width_hb")
        self.gridLayout_parameters.addWidget(self.width_hb, 3, 2, 1, 1)
        self.height_lb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_lb.sizePolicy().hasHeightForWidth())
        self.height_lb.setSizePolicy(sizePolicy)
        self.height_lb.setBaseSize(QtCore.QSize(0, 0))
        self.height_lb.setStyleSheet("QLineEdit {\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 1px;\n"
                                     "    border-radius: 8px;\n"
                                     "    min-width: 4em;\n"
                                     "    padding: 3px;\n"
                                     "}\n"
                                     "")
        self.height_lb.setObjectName("height_lb")
        self.gridLayout_parameters.addWidget(self.height_lb, 2, 1, 1, 1)
        self.label_adb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_adb.setFont(font)
        self.label_adb.setObjectName("label_adb")
        self.gridLayout_parameters.addWidget(self.label_adb, 4, 0, 1, 1)
        self.height_adb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_adb.sizePolicy().hasHeightForWidth())
        self.height_adb.setSizePolicy(sizePolicy)
        self.height_adb.setStyleSheet("QLineEdit {\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 1px;\n"
                                      "    border-radius: 8px;\n"
                                      "    min-width: 4em;\n"
                                      "    padding: 3px;\n"
                                      "}\n"
                                      "")
        self.height_adb.setObjectName("height_adb")
        self.gridLayout_parameters.addWidget(self.height_adb, 4, 1, 1, 1)
        self.width_adb = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_adb.sizePolicy().hasHeightForWidth())
        self.width_adb.setSizePolicy(sizePolicy)
        self.width_adb.setStyleSheet("QLineEdit {\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 1px;\n"
                                     "    border-radius: 8px;\n"
                                     "    min-width: 4em;\n"
                                     "    padding: 3px;\n"
                                     "}\n"
                                     "")
        self.width_adb.setObjectName("width_adb")
        self.gridLayout_parameters.addWidget(self.width_adb, 4, 2, 1, 1)
        self.label_height = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_height.sizePolicy().hasHeightForWidth())
        self.label_height.setSizePolicy(sizePolicy)
        self.label_height.setObjectName("label_height")
        self.gridLayout_parameters.addWidget(self.label_height, 0, 1, 1, 1)
        self.label_width = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_width.sizePolicy().hasHeightForWidth())
        self.label_width.setSizePolicy(sizePolicy)
        self.label_width.setObjectName("label_width")
        self.gridLayout_parameters.addWidget(self.label_width, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_parameters)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.compute_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compute_button.sizePolicy().hasHeightForWidth())
        self.compute_button.setSizePolicy(sizePolicy)
        self.compute_button.setStyleSheet("QPushButton:pressed {\n"
                                          "   background-color:#60a3d9;\n"
                                          "    border-style: inset;\n"
                                          "}")
        self.compute_button.setObjectName("compute_button")
        self.gridLayout_2.addWidget(self.compute_button, 0, 0, 1, 1)
        self.checkbox_xlsx = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_xlsx.sizePolicy().hasHeightForWidth())
        self.checkbox_xlsx.setSizePolicy(sizePolicy)
        self.checkbox_xlsx.setObjectName("checkbox_xlsx")
        self.gridLayout_2.addWidget(self.checkbox_xlsx, 1, 1, 1, 1)
        self.checkbox_manually = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_manually.sizePolicy().hasHeightForWidth())
        self.checkbox_manually.setSizePolicy(sizePolicy)
        self.checkbox_manually.setStyleSheet("")
        self.checkbox_manually.setObjectName("checkbox_manually")
        self.gridLayout_2.addWidget(self.checkbox_manually, 0, 1, 1, 1)
        self.checkbox_automatic = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_automatic.setObjectName("checkbox_automatic")
        self.gridLayout_2.addWidget(self.checkbox_automatic, 0, 2, 1, 1)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy)
        self.export_button.setStyleSheet("QPushButton:pressed {\n"
                                         "   background-color:#60a3d9;\n"
                                         "    border-style: inset;\n"
                                         "}")
        self.export_button.setObjectName("export_button")
        self.gridLayout_2.addWidget(self.export_button, 1, 0, 1, 1)
        self.checkbox_adb = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_adb.setObjectName("checkbox_adb")
        self.gridLayout_2.addWidget(self.checkbox_adb, 0, 3, 1, 1)
        self.checkbox_csv = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_csv.sizePolicy().hasHeightForWidth())
        self.checkbox_csv.setSizePolicy(sizePolicy)
        self.checkbox_csv.setObjectName("checkbox_csv")
        self.gridLayout_2.addWidget(self.checkbox_csv, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 8, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.assessment_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assessment_view.sizePolicy().hasHeightForWidth())
        self.assessment_view.setSizePolicy(sizePolicy)
        self.assessment_view.setStyleSheet("#QTableView {\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 2px;\n"
                                           "    border-radius: 8px;\n"
                                           "    border-color: #003b73;\n"
                                           "    min-width: 4em;\n"
                                           "    padding: 3px;\n"
                                           "}\n"
                                           "")
        self.assessment_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.assessment_view.setObjectName("assessment_view")
        self.verticalLayout_2.addWidget(self.assessment_view)
        self.loading_screen = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loading_screen.sizePolicy().hasHeightForWidth())
        self.loading_screen.setSizePolicy(sizePolicy)
        self.loading_screen.setText("")
        self.loading_screen.setObjectName("loading_screen")
        self.verticalLayout_2.addWidget(self.loading_screen, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 6, 1, 1)
        self.table_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_view.sizePolicy().hasHeightForWidth())
        self.table_view.setSizePolicy(sizePolicy)
        self.table_view.setStyleSheet("#QTableView {\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 8px;\n"
                                      "    border-color: #003b73;\n"
                                      "    min-width: 4em;\n"
                                      "    padding: 3px;\n"
                                      "}")
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.setObjectName("table_view")
        self.gridLayout.addWidget(self.table_view, 3, 10, 1, 1)
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setObjectName("header")
        self.gridLayout.addWidget(self.header, 0, 1, 1, 13)
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setEnabled(True)
        self.tab_widget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
                                      "    border-top: 2px solid #C2C7CB;\n"
                                      "    position: absolute;\n"
                                      "    top: -0.5em;\n"
                                      "}\n"
                                      "\n"
                                      "QTabWidget::tab-bar {\n"
                                      "    alignment: center;\n"
                                      "}\n"
                                      "\n"
                                      "/* Style the tab using the tab sub-control. Note that\n"
                                      "    it reads QTabBar _not_ QTabWidget */\n"
                                      "QTabBar::tab {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                      "                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                      "    border: 2px solid #C4C4C3;\n"
                                      "    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
                                      "    border-top-left-radius: 4px;\n"
                                      "    border-top-right-radius: 4px;\n"
                                      "    min-width: 8ex;\n"
                                      "    padding: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                                      "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
                                      "                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:selected {\n"
                                      "    border-color: #9B9B9B;\n"
                                      "    border-bottom-color: #C2C7CB; /* same as pane color */\n"
                                      "}")
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setUsesScrollButtons(True)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.low_beam = QtWidgets.QWidget()
        self.low_beam.setEnabled(True)
        self.low_beam.setObjectName("low_beam")
        self.tab_widget.addTab(self.low_beam, "")
        self.high_beam = QtWidgets.QWidget()
        self.high_beam.setObjectName("high_beam")
        self.tab_widget.addTab(self.high_beam, "")
        self.adb50_oncoming = QtWidgets.QWidget()
        self.adb50_oncoming.setObjectName("adb50_oncoming")
        self.tab_widget.addTab(self.adb50_oncoming, "")
        self.adb50_preceding = QtWidgets.QWidget()
        self.adb50_preceding.setObjectName("adb50_preceding")
        self.tab_widget.addTab(self.adb50_preceding, "")
        self.adb100_oncoming = QtWidgets.QWidget()
        self.adb100_oncoming.setObjectName("adb100_oncoming")
        self.tab_widget.addTab(self.adb100_oncoming, "")
        self.adb100_preceding = QtWidgets.QWidget()
        self.adb100_preceding.setObjectName("adb100_preceding")
        self.tab_widget.addTab(self.adb100_preceding, "")
        self.adb200_oncoming = QtWidgets.QWidget()
        self.adb200_oncoming.setObjectName("adb200_oncoming")
        self.tab_widget.addTab(self.adb200_oncoming, "")
        self.adb200_preceding = QtWidgets.QWidget()
        self.adb200_preceding.setObjectName("adb200_preceding")
        self.tab_widget.addTab(self.adb200_preceding, "")
        self.gridLayout.addWidget(self.tab_widget, 4, 0, 1, 14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        self.howto_action = QtWidgets.QAction("&How to use")
        self.about_action = QtWidgets.QAction("&About")
        self.menubar.addAction(self.howto_action)
        self.menubar.addAction(self.about_action)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.toolBar = QtWidgets.QToolBar(MainWindow)
        #self.toolBar.setObjectName("toolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HSPR"))
        self.upload_button.setText(_translate("MainWindow", "Upload zip file"))
        self.upload_lb_btn.setText(_translate("MainWindow", "Upload LB files"))
        self.upload_hb_btn.setText(_translate("MainWindow", "Upload HB files"))
        self.upload_adb_btn.setText(_translate("MainWindow", "Upload ADB files"))
        self.clear_loadeddata_btn.setText(_translate("MainWindow", "Clear loaded data"))
        
        #self.how_button.setText(_translate("MainWindow", "How to use"))
        #self.about_button.setText(_translate("MainWindow", "About"))
        self.label_hb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">High Beam </p></body></html>"))
        self.label_lb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Low Beam </p></body></html>"))
        self.label_adb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">  ADB         </p></body></html>"))
        self.label_height.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Height </span></p></body></html>"))
        self.label_width.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Width </span></p></body></html>"))
        self.compute_button.setText(_translate("MainWindow", "Compute"))
        self.checkbox_xlsx.setText(_translate("MainWindow", ".xlsx "))
        self.checkbox_manually.setText(_translate("MainWindow", "Manually"))
        self.checkbox_automatic.setText(_translate("MainWindow", "Automatic"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.checkbox_adb.setText(_translate("MainWindow", "ADB"))
        self.checkbox_csv.setText(_translate("MainWindow", ".csv"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Headlamp Safety Performance Rating </span></p></body></html>"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.low_beam), _translate("MainWindow", "Low Beam"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.high_beam), _translate("MainWindow", "High Beam"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb50_oncoming), _translate("MainWindow", "ADB (Oncoming 50m)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb50_preceding), _translate("MainWindow", "ADB (Preceding 50m)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb100_oncoming), _translate("MainWindow", "ADB (Oncoming 100m)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb100_preceding), _translate("MainWindow", "ADB (Preceding 100m)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb200_oncoming), _translate("MainWindow", "ADB (Oncoming 200m)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.adb200_preceding), _translate("MainWindow", "ADB (Preceding 200m)"))
        #self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
