from gui import *

def bp():
    text = ui.lineEdit.text()
    try:
        ui.lineEdit.setText(text[:len(text)-1])
    except:
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.pushButton_17.clicked.connect(bp)
    sys.exit(app.exec_())