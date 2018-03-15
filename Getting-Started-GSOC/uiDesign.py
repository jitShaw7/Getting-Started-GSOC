from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, 
                        QLabel, QLineEdit, QMessageBox, QProgressBar, QPushButton, 
                        QVBoxLayout, QWidget)

import mailingList

class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.createPageComponents()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        self.setLayout(mainLayout)

        self.setGeometry(100, 100, 600, 100)
        self.setWindowTitle("Getting Started-GSOC")
        self.show()


    def createPageComponents(self):
        self.groupBox = QGroupBox('Subscribing to Mailing Lists')

        layout = QVBoxLayout()

        sublayout = QGridLayout()
        labelUserEmail = QLabel('Enter Your Email:')
        self.editorUserEmail = QLineEdit()
        self.checkBox1 = QCheckBox('debian-outreach')
        self.checkBox1.toggle()
        checkBox1_decription = QLabel(': Discussion of Debian\'s participation in internship-like programs, such as Outreachy, GSOC')
        self.checkBox2 = QCheckBox('debian-user')
        checkBox2_decription = QLabel(': Support for Debian users who speak English.')
        sublayout.addWidget(labelUserEmail, 0, 0)
        sublayout.addWidget(self.editorUserEmail, 0, 1)
        sublayout.addWidget(self.checkBox1, 1, 0)
        sublayout.addWidget(checkBox1_decription, 1,1)
        sublayout.addWidget(self.checkBox2, 2, 0)
        sublayout.addWidget(checkBox2_decription, 2, 1)


        self.buttonSubscribeML = QPushButton('&Subscribe')
        self.buttonSubscribeML.resize(self.buttonSubscribeML.minimumSizeHint())
        self.buttonSubscribeML.clicked.connect(self.subscribeMailingList)

        layout.addLayout(sublayout)
        layout.addWidget(self.buttonSubscribeML)

        self.groupBox.setLayout(layout)

    def subscribeMailingList(self):
        check = 0
        if not self.checkBox1.isChecked() and not self.checkBox2.isChecked():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle('Error!')
            msgBox.setText('No Options Selected')
            msgBox.setDetailedText("You need to select at least one Mailing List.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            check += 1

        if '@' not in self.editorUserEmail.text():
            msgBox2 = QMessageBox()
            msgBox2.setIcon(QMessageBox.Critical)
            msgBox2.setWindowTitle('Error!')
            msgBox2.setText('Enter Proper Email Address')
            msgBox2.setStandardButtons(QMessageBox.Ok)
            msgBox2.exec_()
        else:
            check += 1

        optionList = []
        if self.checkBox1.isChecked():
            optionList.append(self.checkBox1.text())
        if self.checkBox2.isChecked():
            optionList.append(self.checkBox2.text())

        if check == 2:
            value = mailingList.subscribe(self.editorUserEmail.text(), optionList)
            if value == 1:
                msgBox3 = QMessageBox()
                msgBox3.setWindowTitle('Success!')
                msgBox3.setText('Subscription Successful...')
                msgBox3.setStandardButtons(QMessageBox.Ok)
                msgBox3.exec_()
            else:
                msgBox4 = QMessageBox()
                msgBox4.setIcon(QMessageBox.Critical)
                msgBox4.setWindowTitle('Error')
                msgBox4.setText('Subscription Unsuccessful...')
                msgBox4.setDetailedText('''There was some error while trying to Subscribe you to the selected mailing lists. Please make sure you are connected to the internet and your email address is valid.''')
                msgBox4.setStandardButtons(QMessageBox.Ok)
                msgBox4.exec_()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())