import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calc import Ui_MainWindow


app = QApplication(sys.argv)


window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

isOpSelected=False
isNum2Selected=False
isNum1Selected=False
num1=0
num2=0
op=""

def numClicked(num):
    global isOpSelected, isNum2Selected, isNum1Selected,num1, num2, op
    if not isOpSelected:
        num1=num
        isNum1Selected = True
        ui.num1.setText("  "+str(num1))
    else:
        num2=num
        isNum2Selected = True
        ui.num2.setText("  "+str(num2))
        
def chooseOp(oper):
    global isOpSelected, isNum2Selected, isNum1Selected, num1, num2, op
    if not isNum2Selected and isNum1Selected:
        op = oper
        ui.op.setText("   "+op)
        isOpSelected = True

def calculate():
    global isOpSelected, isNum2Selected, num1, num2, op
    if isNum2Selected:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error"
        else:
            result = "Error"
        ui.ans.setText(str(result))
    else:
        ui.ans.setText("Error")

def Again():
    global isOpSelected, isNum2Selected, isNum1Selected, num1, num2, op
    isOpSelected = False
    isNum2Selected = False
    isNum1Selected = False
    num1 = 0
    num2 = 0
    op = ""
    ui.num1.setText("")
    ui.num2.setText("")
    ui.op.setText("")
    ui.ans.setText("")


ui.pushButton.clicked.connect(lambda:numClicked(0))
ui.pushButton_1.clicked.connect(lambda:numClicked(1))
ui.pushButton_2.clicked.connect(lambda:numClicked(1))
ui.pushButton_3.clicked.connect(lambda:numClicked(3))
ui.pushButton_4.clicked.connect(lambda:numClicked(4))
ui.pushButton_5.clicked.connect(lambda:numClicked(5))
ui.pushButton_6.clicked.connect(lambda:numClicked(6))
ui.pushButton_7.clicked.connect(lambda:numClicked(7))
ui.pushButton_8.clicked.connect(lambda:numClicked(8))
ui.pushButton_9.clicked.connect(lambda:numClicked(9))
ui.plus.clicked.connect(lambda:chooseOp("+"))
ui.minus.clicked.connect(lambda:chooseOp("-"))
ui.product.clicked.connect(lambda:chooseOp("*"))
ui.division.clicked.connect(lambda:chooseOp("/"))
ui.calculate.clicked.connect(calculate)
ui.again.clicked.connect(Again)


window.show()
sys.exit(app.exec_())
