#создай приложение для запоминания информации
#подключение библиотек
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,     QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox
from random import randint,shuffle

t = 0
f = 0
def switcher():
    global quest_num, qexist
    if ans_btn.text == "Ответить на вопрос":
        if qexist:
            show_result()
            RadioGroupBox.hide()
            AnsGroupBox.show()
            ans_btn.text = 'Следующий вопрос'
            ans_btn.setText(ans_btn.text)
    else:
        if qexist:
            questions.remove(questions[quest_num])
            answers.remove(answers[quest_num])
            RadioGroupBox.show()
            AnsGroupBox.hide()
            change_q(answers,sh_list)
            ans_btn.text = 'Ответить на вопрос'
            ans_btn.setText(ans_btn.text)

def show_result():
    global quest_num,right_btn,t,f
    if right_btn.isChecked() == True:
        t = t + 1
        trueq.setText('Правильно'+str(t))
        res_mes.setText('Правильный ответ')
        right_var.setText(answers[quest_num][0])
    else:
        f = f + 1
        falseq.setText('Неправильно:'+str(f))
        res_mes.setText('Ошибка!')
        right_var.setText(answers[quest_num][0])

global quest_num, qexist 
qexist = True
#хранилище вопросов
questions = [
    "В каком году было Ледовое побоище?",
    'Когда закончилась Великая Отечественная война?',
    "В каком году марсиане завоевали Землю?"
]
answers = [
    ['1242','1400','1098','1945'],
    ['1945','1989','1941','1953'],
    ['2056', '1854','2022','980']
]
#создание элементов интерфейса
app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Викторина')
main_win.resize(400, 200)

question = QLabel()
result = QLabel()

RadioGroupBox = QGroupBox('Варианты ответов:')
btn1 = QRadioButton()
btn2 = QRadioButton()
btn3 = QRadioButton()
btn4 = QRadioButton()

#макет группы вопроса
hline1 =  QHBoxLayout()
hline2 =  QHBoxLayout()
qgroup_line = QVBoxLayout()
agroup_line = QVBoxLayout()
hline1.addWidget(btn1, alignment = Qt.AlignCenter)
hline1.addWidget(btn2, alignment = Qt.AlignCenter)
hline2.addWidget(btn3, alignment = Qt.AlignCenter)
hline2.addWidget(btn4, alignment = Qt.AlignCenter)
qgroup_line.addLayout(hline1)
qgroup_line.addLayout(hline2)
RadioGroupBox.setLayout(qgroup_line)

#true or false
trueq = QLabel('Правильно:'+str(t))
falseq = QLabel('Неправильно:'+str(f))

#макет группы ответа
AnsGroupBox = QGroupBox('Результат теста:')
res_mes = QLabel('Правильно')
right_var = QLabel('вариант 1')

ans_btn = QPushButton('Ответить на вопрос')
ans_btn.text = 'Ответить на вопрос'

main_line = QVBoxLayout()

#Макет группы ответа
agroup_line.addWidget(res_mes)
agroup_line.addWidget(right_var)
AnsGroupBox.setLayout(agroup_line)
AnsGroupBox.hide()

# Привязка к главной линии
main_line.addWidget(question, alignment = Qt.AlignCenter)
main_line.addWidget(RadioGroupBox)
main_line.addWidget(AnsGroupBox)
main_line.addWidget(ans_btn, alignment = Qt.AlignCenter)
#привязка счетчика
main_line.addWidget(trueq)
main_line.addWidget(falseq)

main_win.setLayout(main_line)
sh_list = [btn1,btn2,btn3,btn4]


def change_q(answers,sh_list):
    global quest_num, qexist , right_btn
    if len(questions)>0 and qexist:
        quest_num = randint(0,len(questions)-1)
        question.setText(questions[quest_num])
        shuffle(sh_list)
        sh_list[0].setText(answers[quest_num][0])
        sh_list[1].setText(answers[quest_num][1])
        sh_list[2].setText(answers[quest_num][2])
        sh_list[3].setText(answers[quest_num][3])
        right_btn = sh_list[0]
    else:
        qexist = False
        question.setText('Вопросы закончились!')
        RadioGroupBox.hide()
        ans_btn.hide()


change_q(answers,sh_list)
ans_btn.clicked.connect(switcher)

#запуск приложения
main_win.show()
app.exec_()

