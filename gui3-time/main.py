import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from timetable import Ui_MainWindow


app = QApplication(sys.argv)


window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)


def calcAns():
    sh= ui.SHslider.value()
    sm= ui.SMslider.value()
    ph= ui.PHslider.value()
    pm= ui.PMslider.value()
    jh= ui.JHslider.value()
    jm= ui.JMslider.value()
    m=sm+pm+jm
    h=sh+jh+ph+(m//60)
    m=m%60
    ui.answer.setText(f"  {h} hours and {m} minutes ")


ui.SHslider.valueChanged.connect(calcAns)
ui.SHslider.valueChanged.connect(lambda: ui.SHL.setText(str(ui.SHslider.value())+" hours"))
ui.SMslider.valueChanged.connect(calcAns)
ui.SMslider.valueChanged.connect(lambda: ui.SML.setText(str(ui.SMslider.value())+" minutes"))
ui.PHslider.valueChanged.connect(calcAns)
ui.PHslider.valueChanged.connect(lambda: ui.PHL.setText(str(ui.PHslider.value())+" hours"))
ui.PMslider.valueChanged.connect(calcAns)
ui.PMslider.valueChanged.connect(lambda: ui.PML.setText(str(ui.PMslider.value())+" minutes"))
ui.JHslider.valueChanged.connect(calcAns)
ui.JHslider.valueChanged.connect(lambda: ui.JHL.setText(str(ui.JHslider.value())+" hours"))
ui.JMslider.valueChanged.connect(calcAns)
ui.JMslider.valueChanged.connect(lambda: ui.JML.setText(str(ui.JMslider.value())+" minutes"))



window.show()
sys.exit(app.exec_())
