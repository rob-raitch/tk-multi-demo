# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk.platform.qt import QtCore, QtGui
# import MA.TestEnv
# from MA.UI import *
# from time import sleep
# from cmds import *
from MA.Test import TestCase
import os
import subprocess
from toolkit import *
from multiprocessing import Process
from DemoAppRegression import *
from MayaRegression import *
from threading import Thread

# import the shotgun_menus module from the qtwidgets framework
automation = sgtk.platform.import_framework(
    "tk-framework-qtwidgets", "shotgun_menus")

class AutomationDemo(QtGui.QWidget):
    """
    Demonstrates the use of the the ShotgunMenu class available in the
    tk-frameworks-qtwidgets framework.
    """

    def __init__(self, parent=None):
        """
        Initialize the demo widget.
        """

        # call the base class init
        super(AutomationDemo, self).__init__(parent)

        # --- build a shotgun menu

        sg_menu = automation.ShotgunMenu(self)
        #submenu = automation.ShotgunMenu(self)
        #submenu.setTitle("SubAutomation")

        # create some dummy actions
        automation1 = QtGui.QAction("Maya Automation", self)
        automation1.setObjectName("Maya Automation")
        automation1.triggered.connect(self.run_maya_automation)
        automation2 = QtGui.QAction("Nuke Automation", self)
        automation2.setObjectName("Nuke Automation")
        automation3 = QtGui.QAction("Demo App Automation", self)
        automation3.setObjectName("Demo App Automation")
        automation3.triggered.connect(self.run_demo_automation)
        #automation4 = QtGui.QAction("Automation 4", self)

        # add a group of actions to the top-level menu
        sg_menu.add_group([automation1, automation2, automation3], "Automation List")

        # add some actions to the sub menu
        #submenu.add_group([automation3, automation4], "Submenu Automation")

        # a button to trigger the menu
        sg_menu_button = QtGui.QPushButton("Automation")
        sg_menu_button.setFixedWidth(100)
        sg_menu_button.clicked.connect(
            lambda: sg_menu.exec_(QtGui.QCursor.pos())
        )
        sg_menu_button.setObjectName("Automation")

        # help label
        doc = QtGui.QLabel("Click the button to show Automation.")
        doc.setAlignment(QtCore.Qt.AlignCenter)

        # lay out and align the widgets
        layout = QtGui.QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(doc)
        layout.addSpacing(8)
        layout.addWidget(sg_menu_button)
        layout.addStretch()

        layout.setAlignment(sg_menu_button, QtCore.Qt.AlignCenter)

    def run_demo_automation(self):
        # p = Process(target=DemoAppRegression())
        # p.start()
        # p.join()
        #execfile("//mtldnvpx12/C/Python27/Lib/TOOLKIT/DemoAppRegression.py")
        # DemoAppRegression()
        t = Thread(target=DemoAppRegression())
        t.daemon = True
        t.start()

    def run_maya_automation(self):
        MayaRegressionShot()
        #execfile("//mtldnvpx12/C/Python27/Lib/TOOLKIT/MayaRegression.py")
        #os.system("python //mtldnvpx12/C/Python27/Lib/TOOLKIT/MayaRegression.py&")
        # p = Process(target=MayaRegressionShot())
        # p.start()
        # p.join()
        # t = Thread(target=MayaRegressionShot())
        # t.daemon = True
        # t.start()