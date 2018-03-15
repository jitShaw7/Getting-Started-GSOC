from PyQt5.QtWidgets import QApplication
import sys
import uiDesign

class GettingStarted(uiDesign.MainWindow):
    def __init__(self):
        super(GettingStarted, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GettingStarted()
    sys.exit(app.exec_())

