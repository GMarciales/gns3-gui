# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/dynamips/ui/dynamips_preferences_page.ui'
#
# Created: Tue Sep 30 19:03:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DynamipsPreferencesPageWidget(object):
    def setupUi(self, DynamipsPreferencesPageWidget):
        DynamipsPreferencesPageWidget.setObjectName(_fromUtf8("DynamipsPreferencesPageWidget"))
        DynamipsPreferencesPageWidget.resize(430, 505)
        self.vboxlayout = QtGui.QVBoxLayout(DynamipsPreferencesPageWidget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.uiTabWidget = QtGui.QTabWidget(DynamipsPreferencesPageWidget)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiGeneralSettingsTabWidget = QtGui.QWidget()
        self.uiGeneralSettingsTabWidget.setObjectName(_fromUtf8("uiGeneralSettingsTabWidget"))
        self.gridLayout = QtGui.QGridLayout(self.uiGeneralSettingsTabWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiDynamipsPathLineEdit = QtGui.QLineEdit(self.uiGeneralSettingsTabWidget)
        self.uiDynamipsPathLineEdit.setObjectName(_fromUtf8("uiDynamipsPathLineEdit"))
        self.horizontalLayout.addWidget(self.uiDynamipsPathLineEdit)
        self.uiDynamipsPathToolButton = QtGui.QToolButton(self.uiGeneralSettingsTabWidget)
        self.uiDynamipsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiDynamipsPathToolButton.setObjectName(_fromUtf8("uiDynamipsPathToolButton"))
        self.horizontalLayout.addWidget(self.uiDynamipsPathToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.uiDynamipsPathLabel = QtGui.QLabel(self.uiGeneralSettingsTabWidget)
        self.uiDynamipsPathLabel.setObjectName(_fromUtf8("uiDynamipsPathLabel"))
        self.gridLayout.addWidget(self.uiDynamipsPathLabel, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(390, 193, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.uiConsolePortRangeGroupBox = QtGui.QGroupBox(self.uiGeneralSettingsTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName(_fromUtf8("uiConsolePortRangeGroupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uiConsoleStartPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2001)
        self.uiConsoleStartPortSpinBox.setObjectName(_fromUtf8("uiConsoleStartPortSpinBox"))
        self.horizontalLayout_5.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtGui.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName(_fromUtf8("uiConsolePortRangeLabel"))
        self.horizontalLayout_5.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 2500)
        self.uiConsoleEndPortSpinBox.setObjectName(_fromUtf8("uiConsoleEndPortSpinBox"))
        self.horizontalLayout_5.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout.addWidget(self.uiConsolePortRangeGroupBox, 2, 0, 1, 2)
        self.uiAuxPortRangeGroupBox = QtGui.QGroupBox(self.uiGeneralSettingsTabWidget)
        self.uiAuxPortRangeGroupBox.setObjectName(_fromUtf8("uiAuxPortRangeGroupBox"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.uiAuxPortRangeGroupBox)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.uiAuxStartPortSpinBox = QtGui.QSpinBox(self.uiAuxPortRangeGroupBox)
        self.uiAuxStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiAuxStartPortSpinBox.setMaximum(65535)
        self.uiAuxStartPortSpinBox.setProperty("value", 2501)
        self.uiAuxStartPortSpinBox.setObjectName(_fromUtf8("uiAuxStartPortSpinBox"))
        self.horizontalLayout_6.addWidget(self.uiAuxStartPortSpinBox)
        self.uiAuxPortRangeLabel = QtGui.QLabel(self.uiAuxPortRangeGroupBox)
        self.uiAuxPortRangeLabel.setObjectName(_fromUtf8("uiAuxPortRangeLabel"))
        self.horizontalLayout_6.addWidget(self.uiAuxPortRangeLabel)
        self.uiAuxEndPortSpinBox = QtGui.QSpinBox(self.uiAuxPortRangeGroupBox)
        self.uiAuxEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiAuxEndPortSpinBox.setMaximum(65535)
        self.uiAuxEndPortSpinBox.setProperty("value", 3000)
        self.uiAuxEndPortSpinBox.setObjectName(_fromUtf8("uiAuxEndPortSpinBox"))
        self.horizontalLayout_6.addWidget(self.uiAuxEndPortSpinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout.addWidget(self.uiAuxPortRangeGroupBox, 3, 0, 1, 2)
        self.uiTabWidget.addTab(self.uiGeneralSettingsTabWidget, _fromUtf8(""))
        self.uiServerSettingsTabWidget = QtGui.QWidget()
        self.uiServerSettingsTabWidget.setObjectName(_fromUtf8("uiServerSettingsTabWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiServerSettingsTabWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiUseLocalServercheckBox = QtGui.QCheckBox(self.uiServerSettingsTabWidget)
        self.uiUseLocalServercheckBox.setChecked(True)
        self.uiUseLocalServercheckBox.setObjectName(_fromUtf8("uiUseLocalServercheckBox"))
        self.gridLayout_2.addWidget(self.uiUseLocalServercheckBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtGui.QGroupBox(self.uiServerSettingsTabWidget)
        self.uiRemoteServersGroupBox.setObjectName(_fromUtf8("uiRemoteServersGroupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.uiRemoteServersGroupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uiRemoteServersTreeWidget = QtGui.QTreeWidget(self.uiRemoteServersGroupBox)
        self.uiRemoteServersTreeWidget.setEnabled(False)
        self.uiRemoteServersTreeWidget.setObjectName(_fromUtf8("uiRemoteServersTreeWidget"))
        self.horizontalLayout_3.addWidget(self.uiRemoteServersTreeWidget)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        self.uiTabWidget.addTab(self.uiServerSettingsTabWidget, _fromUtf8(""))
        self.uiAdvancedSettingsTabWidget = QtGui.QWidget()
        self.uiAdvancedSettingsTabWidget.setObjectName(_fromUtf8("uiAdvancedSettingsTabWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.uiAdvancedSettingsTabWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uiHypervisorAllocationGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiHypervisorAllocationGroupBox.setObjectName(_fromUtf8("uiHypervisorAllocationGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.uiHypervisorAllocationGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.uiAllocateHypervisorPerDeviceCheckBox = QtGui.QCheckBox(self.uiHypervisorAllocationGroupBox)
        self.uiAllocateHypervisorPerDeviceCheckBox.setChecked(True)
        self.uiAllocateHypervisorPerDeviceCheckBox.setObjectName(_fromUtf8("uiAllocateHypervisorPerDeviceCheckBox"))
        self.verticalLayout_2.addWidget(self.uiAllocateHypervisorPerDeviceCheckBox)
        self.uiMemoryUsageLimitPerHypervisorLabel = QtGui.QLabel(self.uiHypervisorAllocationGroupBox)
        self.uiMemoryUsageLimitPerHypervisorLabel.setObjectName(_fromUtf8("uiMemoryUsageLimitPerHypervisorLabel"))
        self.verticalLayout_2.addWidget(self.uiMemoryUsageLimitPerHypervisorLabel)
        self.uiMemoryUsageLimitPerHypervisorSpinBox = QtGui.QSpinBox(self.uiHypervisorAllocationGroupBox)
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setEnabled(False)
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setMaximum(1000000)
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setSingleStep(128)
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setProperty("value", 512)
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setObjectName(_fromUtf8("uiMemoryUsageLimitPerHypervisorSpinBox"))
        self.verticalLayout_2.addWidget(self.uiMemoryUsageLimitPerHypervisorSpinBox)
        self.uiAllocateHypervisorPerIOSCheckBox = QtGui.QCheckBox(self.uiHypervisorAllocationGroupBox)
        self.uiAllocateHypervisorPerIOSCheckBox.setEnabled(False)
        self.uiAllocateHypervisorPerIOSCheckBox.setChecked(True)
        self.uiAllocateHypervisorPerIOSCheckBox.setObjectName(_fromUtf8("uiAllocateHypervisorPerIOSCheckBox"))
        self.verticalLayout_2.addWidget(self.uiAllocateHypervisorPerIOSCheckBox)
        self.verticalLayout_3.addWidget(self.uiHypervisorAllocationGroupBox)
        self.uiHypervisorPortRangeGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiHypervisorPortRangeGroupBox.setObjectName(_fromUtf8("uiHypervisorPortRangeGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.uiHypervisorPortRangeGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiHypervisorStartPortSpinBox = QtGui.QSpinBox(self.uiHypervisorPortRangeGroupBox)
        self.uiHypervisorStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiHypervisorStartPortSpinBox.setMaximum(65535)
        self.uiHypervisorStartPortSpinBox.setProperty("value", 7200)
        self.uiHypervisorStartPortSpinBox.setObjectName(_fromUtf8("uiHypervisorStartPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiHypervisorStartPortSpinBox)
        self.uiHypervisorPortRangeLabel = QtGui.QLabel(self.uiHypervisorPortRangeGroupBox)
        self.uiHypervisorPortRangeLabel.setObjectName(_fromUtf8("uiHypervisorPortRangeLabel"))
        self.horizontalLayout_4.addWidget(self.uiHypervisorPortRangeLabel)
        self.uiHypervisorEndPortSpinBox = QtGui.QSpinBox(self.uiHypervisorPortRangeGroupBox)
        self.uiHypervisorEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiHypervisorEndPortSpinBox.setMaximum(65535)
        self.uiHypervisorEndPortSpinBox.setProperty("value", 7700)
        self.uiHypervisorEndPortSpinBox.setObjectName(_fromUtf8("uiHypervisorEndPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiHypervisorEndPortSpinBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.uiHypervisorPortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName(_fromUtf8("uiUDPPortRangeGroupBox"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.uiUDPStartPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10001)
        self.uiUDPStartPortSpinBox.setObjectName(_fromUtf8("uiUDPStartPortSpinBox"))
        self.horizontalLayout_7.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtGui.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName(_fromUtf8("uiUDPPortRangeLabel"))
        self.horizontalLayout_7.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName(_fromUtf8("uiUDPEndPortSpinBox"))
        self.horizontalLayout_7.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem4 = QtGui.QSpacerItem(147, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.uiUDPPortRangeGroupBox)
        self.uiMemoryUsageOptimisationGroupBox = QtGui.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiMemoryUsageOptimisationGroupBox.setObjectName(_fromUtf8("uiMemoryUsageOptimisationGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.uiMemoryUsageOptimisationGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiGhostIOSSupportCheckBox = QtGui.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiGhostIOSSupportCheckBox.setChecked(True)
        self.uiGhostIOSSupportCheckBox.setObjectName(_fromUtf8("uiGhostIOSSupportCheckBox"))
        self.verticalLayout.addWidget(self.uiGhostIOSSupportCheckBox)
        self.uiMmapSupportCheckBox = QtGui.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiMmapSupportCheckBox.setChecked(True)
        self.uiMmapSupportCheckBox.setObjectName(_fromUtf8("uiMmapSupportCheckBox"))
        self.verticalLayout.addWidget(self.uiMmapSupportCheckBox)
        self.uiJITSharingSupportCheckBox = QtGui.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiJITSharingSupportCheckBox.setEnabled(True)
        self.uiJITSharingSupportCheckBox.setChecked(False)
        self.uiJITSharingSupportCheckBox.setObjectName(_fromUtf8("uiJITSharingSupportCheckBox"))
        self.verticalLayout.addWidget(self.uiJITSharingSupportCheckBox)
        self.uiSparseMemorySupportCheckBox = QtGui.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiSparseMemorySupportCheckBox.setChecked(False)
        self.uiSparseMemorySupportCheckBox.setObjectName(_fromUtf8("uiSparseMemorySupportCheckBox"))
        self.verticalLayout.addWidget(self.uiSparseMemorySupportCheckBox)
        self.verticalLayout_3.addWidget(self.uiMemoryUsageOptimisationGroupBox)
        spacerItem5 = QtGui.QSpacerItem(390, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.uiTabWidget.addTab(self.uiAdvancedSettingsTabWidget, _fromUtf8(""))
        self.vboxlayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(164, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.uiTestSettingsPushButton = QtGui.QPushButton(DynamipsPreferencesPageWidget)
        self.uiTestSettingsPushButton.setObjectName(_fromUtf8("uiTestSettingsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiTestSettingsPushButton)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(DynamipsPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.vboxlayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DynamipsPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DynamipsPreferencesPageWidget)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiDynamipsPathLineEdit, self.uiDynamipsPathToolButton)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiDynamipsPathToolButton, self.uiAllocateHypervisorPerDeviceCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiAllocateHypervisorPerDeviceCheckBox, self.uiMemoryUsageLimitPerHypervisorSpinBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiMemoryUsageLimitPerHypervisorSpinBox, self.uiAllocateHypervisorPerIOSCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiAllocateHypervisorPerIOSCheckBox, self.uiGhostIOSSupportCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiGhostIOSSupportCheckBox, self.uiMmapSupportCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiMmapSupportCheckBox, self.uiJITSharingSupportCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiJITSharingSupportCheckBox, self.uiSparseMemorySupportCheckBox)

    def retranslateUi(self, DynamipsPreferencesPageWidget):
        DynamipsPreferencesPageWidget.setWindowTitle(_translate("DynamipsPreferencesPageWidget", "Dynamips", None))
        self.uiDynamipsPathToolButton.setText(_translate("DynamipsPreferencesPageWidget", "...", None))
        self.uiDynamipsPathLabel.setText(_translate("DynamipsPreferencesPageWidget", "Path to Dynamips:", None))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Console port range for routers", None))
        self.uiConsolePortRangeLabel.setText(_translate("DynamipsPreferencesPageWidget", "to", None))
        self.uiAuxPortRangeGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Auxiliary console port range for routers", None))
        self.uiAuxPortRangeLabel.setText(_translate("DynamipsPreferencesPageWidget", "to", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralSettingsTabWidget), _translate("DynamipsPreferencesPageWidget", "General settings", None))
        self.uiUseLocalServercheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Use the local server", None))
        self.uiRemoteServersGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Remote servers", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("DynamipsPreferencesPageWidget", "Host", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(1, _translate("DynamipsPreferencesPageWidget", "Port", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiServerSettingsTabWidget), _translate("DynamipsPreferencesPageWidget", "Server settings", None))
        self.uiHypervisorAllocationGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Hypervisor allocation", None))
        self.uiAllocateHypervisorPerDeviceCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Allocate a new hypervisor for each device", None))
        self.uiMemoryUsageLimitPerHypervisorLabel.setText(_translate("DynamipsPreferencesPageWidget", "Memory usage limit per hypervisor:", None))
        self.uiMemoryUsageLimitPerHypervisorSpinBox.setSuffix(_translate("DynamipsPreferencesPageWidget", " MiB", None))
        self.uiAllocateHypervisorPerIOSCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Allocate a new hypervisor per IOS image", None))
        self.uiHypervisorPortRangeGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Dynamips hypervisor port range", None))
        self.uiHypervisorPortRangeLabel.setText(_translate("DynamipsPreferencesPageWidget", "to", None))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "UDP tunneling port range", None))
        self.uiUDPPortRangeLabel.setText(_translate("DynamipsPreferencesPageWidget", "to", None))
        self.uiMemoryUsageOptimisationGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Memory usage optimisation", None))
        self.uiGhostIOSSupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The ghost IOS feature is a solution that helps to decrease memory usage by sharing an IOS image between different router instances.", None))
        self.uiGhostIOSSupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable ghost IOS support", None))
        self.uiMmapSupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The mmap feature tells Dynamips to use disk files instead of real memory for router instances.", None))
        self.uiMmapSupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable mmap support", None))
        self.uiJITSharingSupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The JIT sharing feature allows router instances to share JIT blocks, instead of recompiling multiple times in a non-shared way.", None))
        self.uiJITSharingSupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable JIT sharing support (unstable)", None))
        self.uiSparseMemorySupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The sparse memory feature reduces the amount of virtual memory used by router instances.", None))
        self.uiSparseMemorySupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable sparse memory support", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiAdvancedSettingsTabWidget), _translate("DynamipsPreferencesPageWidget", "Advanced settings", None))
        self.uiTestSettingsPushButton.setText(_translate("DynamipsPreferencesPageWidget", "Test settings", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("DynamipsPreferencesPageWidget", "Restore defaults", None))

