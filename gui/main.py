import sys
from PyQt5.QtWidgets import QApplication, QDialog
from myproject import Ui_Dialog 


app = QApplication(sys.argv)


window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)


def make_background_red():
    window.setStyleSheet("background-color: red;")


def print_text():
    text = ui.NameField.text()
    print(f"Text entered: {text}")

def nameCheck():
    name = ui.NameField.text()
    if name:
        return True
    else:
        ui.StateLabel.setStyleSheet("color: red;")
        ui.StateLabel.setText("من فضلك أدخل اسمك.")
        return False

def ageCheck():
    age = ui.AgeField.text()
    if age.isdigit():
        return True
    else:
        ui.StateLabel.setStyleSheet("color: red;")
        ui.StateLabel.setText("من فضلك أدخل رقم صحيح للسن.")
        return False
    
def genderCheck():
    if ui.comboBox.currentText() != "اختر من القائمة":
        return True
    else:
        ui.StateLabel.setStyleSheet("color: red;")
        ui.StateLabel.setText("من فضلك اختر نوعك من القائمة.")
        return False
    
def print_info():
    if nameCheck() and ageCheck() and genderCheck():
        name = ui.NameField.text()
        age = ui.AgeField.text()
        gen= ui.comboBox.currentText()
        print(f"Name: {name}, Age: {age}, Gender: {gen}")
        ui.StateLabel.setStyleSheet("color: green;")
        ui.StateLabel.setText(f"تم تسجيلك بنجاح: {name}, {age}, {gen}")


ui.myButton.clicked.connect(print_info)


window.show()
sys.exit(app.exec_())
