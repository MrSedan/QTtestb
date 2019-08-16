__author__ = "MrSedan"
from gui import *

def bp():
    ui.lineEdit.backspace()

def numb(cif):
    ui.lineEdit.setText(ui.lineEdit.text()+str(cif))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #ui.lineEdit.setInputMask("9"*20)
    ui.pushButton_17.clicked.connect(bp)
    ui.pushButton.clicked.connect(numb, int(1))
    sys.exit(app.exec_())