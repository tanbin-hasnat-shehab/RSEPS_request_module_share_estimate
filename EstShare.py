# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import shutil
import time
import os
from req_module import *
from RSEPS_requests_module import *
from datetime import datetime


rseps=RSEPS(version='2022')

#print(rseps.location)
db=Request_Firebase(project_id='pp1123435454')
sdb=Request_Firebase_Storage(project_id='pp1123435454')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Dutch801 XBd BT")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scheme_code = QtWidgets.QLineEdit(self.tab)
        self.scheme_code.setGeometry(QtCore.QRect(230, 100, 231, 51))
        self.scheme_code.setObjectName("scheme_code")
        self.upload_btn = QtWidgets.QPushButton(self.tab)
        self.upload_btn.setGeometry(QtCore.QRect(480, 100, 191, 51))
        self.upload_btn.setObjectName("upload_btn")
        self.serial_status = QtWidgets.QLabel(self.tab)
        self.serial_status.setGeometry(QtCore.QRect(130, 160, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.serial_status.setFont(font)
        self.serial_status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.serial_status.setLineWidth(1)
        self.serial_status.setText("")
        self.serial_status.setAlignment(QtCore.Qt.AlignCenter)
        self.serial_status.setObjectName("serial_status")
        self.upload_upazila = QtWidgets.QLineEdit(self.tab)
        self.upload_upazila.setGeometry(QtCore.QRect(330, 30, 231, 51))
        self.upload_upazila.setObjectName("upload_upazila")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Dutch801 XBd BT")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.chat_panel = QtWidgets.QListWidget(self.tab)
        self.chat_panel.setGeometry(QtCore.QRect(10, 270, 971, 251))
        self.chat_panel.setObjectName("chat_panel")
        self.msg_input = QtWidgets.QPlainTextEdit(self.tab)
        self.msg_input.setGeometry(QtCore.QRect(80, 160, 831, 101))
        self.msg_input.setObjectName("msg_input")
        self.msg_btn = QtWidgets.QPushButton(self.tab)
        self.msg_btn.setGeometry(QtCore.QRect(910, 200, 71, 31))
        self.msg_btn.setObjectName("msg_btn")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 200, 81, 31))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.serial_no = QtWidgets.QLineEdit(self.tab_2)
        self.serial_no.setGeometry(QtCore.QRect(350, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.serial_no.setFont(font)
        self.serial_no.setObjectName("serial_no")
        self.show_name = QtWidgets.QPushButton(self.tab_2)
        self.show_name.setGeometry(QtCore.QRect(530, 100, 101, 31))
        self.show_name.setObjectName("show_name")
        self.import_btn = QtWidgets.QPushButton(self.tab_2)
        self.import_btn.setGeometry(QtCore.QRect(920, 470, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.import_btn.setFont(font)
        self.import_btn.setObjectName("import_btn")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.import_upazila = QtWidgets.QLineEdit(self.tab_2)
        self.import_upazila.setGeometry(QtCore.QRect(350, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.import_upazila.setFont(font)
        self.import_upazila.setObjectName("import_upazila")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(0, 140, 1061, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.my_list = QtWidgets.QListWidget(self.tab_2)
        self.my_list.setGeometry(QtCore.QRect(10, 180, 911, 341))
        self.my_list.setObjectName("my_list")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 41, 21))
        self.label_11.setObjectName("label_11")
        self.status = QtWidgets.QLabel(self.tab)
        self.status.setGeometry(QtCore.QRect(600, 10, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Dutch801 XBd BT")
        font.setPointSize(16)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.version = QtWidgets.QComboBox(self.tab_2)
        self.version.setGeometry(QtCore.QRect(70, 10, 71, 22))
        self.version.setObjectName("version")
        self.label_2.raise_()
        self.serial_no.raise_()
        self.show_name.raise_()
        self.import_btn.raise_()
        self.label_4.raise_()
        self.import_upazila.raise_()
        self.label_5.raise_()
        self.my_list.raise_()
        self.version.raise_()
        self.label_11.raise_()
        self.status.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(0, 440, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(0, 490, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(90, 440, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(190, 490, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.folder_names = QtWidgets.QListWidget(self.tab_3)
        self.folder_names.setGeometry(QtCore.QRect(190, 90, 771, 341))
        self.folder_names.setObjectName("folder_names")
        self.new_folder_name = QtWidgets.QLineEdit(self.tab_3)
        self.new_folder_name.setGeometry(QtCore.QRect(90, 20, 971, 31))
        self.new_folder_name.setObjectName("new_folder_name")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label_12.setObjectName("label_12")
        self.new_folder_btn = QtWidgets.QPushButton(self.tab_3)
        self.new_folder_btn.setGeometry(QtCore.QRect(90, 60, 75, 23))
        self.new_folder_btn.setObjectName("new_folder_btn")
        self.add_file = QtWidgets.QPushButton(self.tab_3)
        self.add_file.setGeometry(QtCore.QRect(0, 100, 75, 23))
        self.add_file.setObjectName("add_file")
        self.folder_download = QtWidgets.QPushButton(self.tab_3)
        self.folder_download.setGeometry(QtCore.QRect(80, 100, 91, 23))
        self.folder_download.setObjectName("folder_download")
        self.delete_folder = QtWidgets.QPushButton(self.tab_3)
        self.delete_folder.setGeometry(QtCore.QRect(80, 140, 75, 23))
        self.delete_folder.setObjectName("delete_folder")
        self.admin_key = QtWidgets.QLineEdit(self.tab_3)
        self.admin_key.setPlaceholderText("admin key") 
        self.admin_key.setGeometry(QtCore.QRect(0, 140, 71, 21))
        self.admin_key.setObjectName("admin_key")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #############################
        
        self.upload_btn.clicked.connect(self.upload_fn)
        #self.show_name.clicked.connect(self.show_name_fn)
        self.import_btn.clicked.connect(self.import_btn_fn)
        self.msg_btn.clicked.connect(self.msg_add_fn)

        self.new_folder_btn.clicked.connect(self.new_folder_btn_fn)
        self.add_file.clicked.connect(self.add_file_fn)
        self.folder_download.clicked.connect(self.folder_download_fn)
        self.delete_folder.clicked.connect(self.folder_delete_fn)
        

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSEPS ESTIMATE SHARE 2022"))
        self.label.setText(_translate("MainWindow", "Scheme Code"))
        self.upload_btn.setText(_translate("MainWindow", "Upload"))
        self.label_3.setText(_translate("MainWindow", "Upazila Name in Upper Case"))
        self.msg_btn.setText(_translate("MainWindow", "send"))
        self.label_10.setText(_translate("MainWindow", "Add a Messege"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Upload"))
        self.label_2.setText(_translate("MainWindow", "Serial No"))
        self.show_name.setText(_translate("MainWindow", "Show Name"))
        self.import_btn.setText(_translate("MainWindow", "Import"))
        self.label_4.setText(_translate("MainWindow", "Upazila Name in Upper Case"))
        self.label_11.setText(_translate("MainWindow", "version"))
        #self.status.setText(_translate("MainWindow", "this is status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Import"))
        self.label_6.setText(_translate("MainWindow", "Email : "))
        self.label_7.setText(_translate("MainWindow", "For any problem : "))
        self.label_8.setText(_translate("MainWindow", "tanbinhasnat04@gmail.com"))
        self.label_9.setText(_translate("MainWindow", "Contact on Facebook"))
        self.label_12.setText(_translate("MainWindow", "Folder Name"))
        self.new_folder_btn.setText(_translate("MainWindow", "Create"))
        self.add_file.setText(_translate("MainWindow", "add file"))
        self.folder_download.setText(_translate("MainWindow", "download folder"))
        self.delete_folder.setText(_translate("MainWindow", "delete folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "File Manager"))

        #########################


        r1=RSEPS(location='RUMA',scheme_name='from class')
        name_of_ex_upazila=r1.existing_upazila()
        self.upload_upazila.setText(name_of_ex_upazila)

        self.version.addItem('2022')
        self.version.addItem('2019')
        self.import_upazila.setText(name_of_ex_upazila)
        
        self.cloud_folder_names=sdb.folder_list()
        if len(self.cloud_folder_names)>0:
            for name in self.cloud_folder_names:
                self.folder_names.addItem(name)


        cloud_msg1=db.show_data()
        cloud_msg=(cloud_msg1['chat_data'])     
        if len(cloud_msg)>0:
            for name in cloud_msg:
                self.chat_panel.addItem(name)


        def add_updated_import_list():
            names_in_db=db.show_data()
            name_list=[]
            try:
                for i in range(len(names_in_db['estimate_data'])):
                    name_list.append(names_in_db['estimate_data'][i]['name'])
                #print(name_list)
                c=0
                for data in name_list:
                    self.my_list.addItem(str(c)+' . '+data[0])
                    c+=1
            except:
                pass
        add_updated_import_list()
    def add_updated_import_list(self):
        self.my_list.clear()
        names_in_db=db.show_data()
        name_list=[]
        try:
            for i in range(len(names_in_db['estimate_data'])):
                name_list.append(names_in_db['estimate_data'][i]['name'])
            #print(name_list)
            c=0
            for data in name_list:
                self.my_list.addItem(str(c)+' . '+data[0])
                c+=1
        except:
            pass
    def upload_fn(self,MainWindow):
        rs_version=self.version.currentText()
        rseps=RSEPS(version=rs_version)
        scheme_code_in_upload=self.scheme_code.text()
        name_est,est_data,_=rseps.get_data(scheme_code=scheme_code_in_upload)
        name_est=f'version - {rs_version} - {name_est}'
        additional_item_array=rseps.get_additional_items(scheme_code=scheme_code_in_upload)
        #print(addi)
        #print(name_est)
        #print(est_data)
        _,ls_items_in_list=rseps.get_LS_items(scheme_code=scheme_code_in_upload)
        datas=db.show_data()
        try:
            length=len(datas['estimate_data'])
        except:
            length=0


        db.input_data(path=f'estimate_data/{length}/name/',data={0:name_est})
        for i in range (len(est_data)):
            db.input_data(path=f'estimate_data/{length}/data/',data={i:est_data[i]})
        for i in range (len(additional_item_array)):
            db.input_data(path=f'estimate_data/{length}/additional/',data={i:additional_item_array[i]})
            #db.input_data(path=f'estimate_data/{0}/',data={i:data[i]})
        for i in range (len(ls_items_in_list)):
            db.input_data(path=f'estimate_data/{length}/LS_items/',data={i:ls_items_in_list[i]})
        _translate = QtCore.QCoreApplication.translate
        self.status.setText(_translate("MainWindow", "Success"))
        self.add_updated_import_list()
        
    def import_btn_fn(self):
        
        serial=self.serial_no.text()
        ds=db.show_data()
        full_data=ds['estimate_data'][int(serial)]
        ss_name=full_data['name'][0]
        rseps=RSEPS(scheme_name=ss_name)
        if 'additional' in full_data.keys():
            rseps.input_additional(additional_list=full_data['additional'])
        #print(full_data)
        if 'data' in full_data.keys():
            for i in range(len(full_data['data'])):
                e_data=full_data['data'][i].split('|')
                
                e_data[1]=int(e_data[1])
                if e_data[2]=='None':
                    e_data[2]=None
                if e_data[3]=='None':
                    e_data[3]=None
                
                if e_data[4]=='None':
                    e_data[4]=None
                if e_data[5]=='None':
                    e_data[5]=None
                if e_data[6]=='None':
                    e_data[6]=None
                if e_data[7]=='None':
                    e_data[7]=None
                if e_data[8]=='None':
                    e_data[8]=None
                #print(e_data)
                
                rseps.input_data(estimate_input=e_data)
        if 'LS_items' in full_data.keys():
            #print(f"this is LS : {full_data['LS_items']}")
            rseps.input_LS(LS_list=full_data['LS_items'],sc_name=full_data['name'])




    #########################################################




    def new_folder_btn_fn(self):
        f_names_cloud=sdb.folder_list()
        existing_fol_names=[]
        for i in range(self.folder_names.count()):
            existing_fol_names.append(self.folder_names.item(i).text())
        #print(existing_fol_names)
        if self.new_folder_name.text()!='' and (self.new_folder_name.text() not in f_names_cloud) and self.new_folder_name.text() not in existing_fol_names:
            self.folder_names.addItem(self.new_folder_name.text())
            
    def add_file_fn(self):
        fname1=QFileDialog.getOpenFileName()


        src_path = fname1[0]
        dst_path = os.getcwd()
        try:
            shutil.copy(src_path, dst_path)
        except:
            pass
        if fname1 and self.folder_names.currentItem():
            #print(fname1[0])
            #print(self.folder_names.currentItem().text())
            fname2=fname1[0].split('/')
            name_to_fr=fname2[-1]
            #sdb.upload_file(path=self.folder_names.currentItem().text(),file_name=name_to_fr)
            sdb.upload_file(path=self.folder_names.currentItem().text(),attribute='condition',random_name_extention=True,file_name=name_to_fr)
            try:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Added Successfully ")
                msg.setWindowTitle("Upload Status")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()
            except:
                pass
        dst_path=dst_path+f'\\{name_to_fr}'
        print(dst_path)
        try:
            os.remove(dst_path)
        except:
            pass
    def folder_download_fn(self):
        if self.folder_names.currentItem().text()!='':
            #sdb.download_file(path=self.folder_names.currentItem().text())
            sdb.download_files(path=self.folder_names.currentItem().text(),attribute='condition',name_as_db=True)
            try:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Downloaded Successfully ")
                msg.setWindowTitle("Download Status")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec_()
            except:
                pass 
    def folder_delete_fn(self):
        admin_keyword='dhaka1205'
        if self.folder_names.currentItem().text()!='' and self.admin_key.text()==admin_keyword:
            sdb.delete_files(path=self.folder_names.currentItem().text(),delete_path=True)   
        
    
    def msg_add_fn(self):
        name_of_ex_upazila=self.upload_upazila.text()
        current_time = datetime.now()
        msg=self.msg_input.toPlainText()
        full_msg=f'From <{name_of_ex_upazila}> _ <{current_time}> => {msg}'
        self.chat_panel.addItem(full_msg)
        datas=db.show_data()
        try:
            length=len(datas['chat_data'])
        except:
            length=0
        db.input_data(path=f'chat_data/',data={length:full_msg})


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())