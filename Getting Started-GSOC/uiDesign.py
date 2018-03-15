from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, 
                        QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout,
                        QWidget)

class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.createPageComponents()
        self.createProgressBar()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        self.setLayout(mainLayout)

        self.setGeometry(100, 100, 600, 100)
        self.setWindowTitle("Getting Started-GSOC")
        self.show()


    def createPageComponents(self):
        self.groupBox = QGroupBox('Step 1: Subscribing to Mailing Lists')

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

    def createProgressBar(self):
        pass

    def subscribeMailingList(self):
        print(self.editorUserEmail.text(), self.checkBox1.isChecked(), self.checkBox2.isChecked())
        if not self.checkBox1.isChecked() and not self.checkBox2.isChecked():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle('Error!')
            msgBox.setText('No Options Selected')
            msgBox.setDetailedText("You need to select at least one Mailing List.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

        if '@' not in self.editorUserEmail.text():
            msgBox2 = QMessageBox()
            msgBox2.setIcon(QMessageBox.Critical)
            msgBox2.setWindowTitle('Error!')
            msgBox2.setText('Enter Proper Email Address')
            msgBox2.setStandardButtons(QMessageBox.Ok)
            msgBox2.exec_()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())