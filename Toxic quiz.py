from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup, QMessageBox


def show_variant1():
    victory_win = QMessageBox()
    victory_win.setText("Типичный обитатель своего рейтинга.\nТы просто принял поражение.")
    victory_win.exec_()
def show_variant2():
    victory_win = QMessageBox()
    victory_win.setText("Ты токсичное чудище. \nВали с этой игры.")
    victory_win.exec_()
def show_variant3():
    victory_win = QMessageBox()
    victory_win.setText("Адекватный обитатель нашей игры. \nВместо обычного тильта - выясняешь проблему.")
    victory_win.exec_()
def show_variant4():
    victory_win = QMessageBox()
    victory_win.setText("Объективно недовольный игрок.\nНадо улучшить коммуникацию с тиммейтами.")
    victory_win.exec_()

def show_variant11():
    victory_win1 = QMessageBox()
    victory_win1.setText("святой / адекват")
    victory_win1.exec_()
def show_variant12():
    victory_win1 = QMessageBox()
    victory_win1.setText("скрытый тильт / средний токсик")
    victory_win1.exec_()
def show_variant13():
    victory_win1 = QMessageBox()
    victory_win1.setText("токсик с триггером")
    victory_win1.exec_()
def show_variant14():
    victory_win1 = QMessageBox()
    victory_win1.setText("токсичное стихийное бедствие")
    victory_win1.exec_()

def show_variant111():
    victory_win = QMessageBox()
    victory_win.setText("Спокойный и адекватный игрок.\nТы умеешь держать эмоции при себе.")
    victory_win.exec_()

def show_variant122():
    victory_win = QMessageBox()
    victory_win.setText("Скрытый тильтер.\nВнутри буря, снаружи — тишина.")
    victory_win.exec_()

def show_variant133():
    victory_win = QMessageBox()
    victory_win.setText("Обиженный токсик.\nМелкие вещи уже выводят тебя из себя.")
    victory_win.exec_()

def show_variant144():
    victory_win = QMessageBox()
    victory_win.setText("Токсичное бедствие.\nИз-за одного крипа готов взорвать всю игру.")
    victory_win.exec_()


#ВОПРОС НОМЕР 1

app = QApplication([])

#УВЕЛИЧИВАЕЮ РАЗМЕР ТЕКСТА
font = app.font()
font.setPointSize(13)       
app.setFont(font)

main_win = QWidget()
main_win.setWindowTitle("КАКОЙ ТЫ УРОВЕНЬ ТОКСИКА В ИГРЕ")
main_win.resize(900, 700)


frage = QLabel("Что ты делаешь, если тебе руинят в играх")
frage.setAlignment(Qt.AlignCenter)

RadioGroupBox = QGroupBox("Варики ответов")

btn_ant1 = QRadioButton("gg wp")
btn_ant2 = QRadioButton("Оскорбляю человека")
btn_ant3 = QRadioButton("Выясняю проблему")
btn_ant4 = QRadioButton("Молчу и просто кидаю репорты")

RadioGroup1 = QButtonGroup()
RadioGroup1.addButton(btn_ant1)
RadioGroup1.addButton(btn_ant2)
RadioGroup1.addButton(btn_ant3)
RadioGroup1.addButton(btn_ant4)

def check_answer1():
    selected = RadioGroup1.checkedButton()
    if not selected:
        QMessageBox.warning(main_win, 'Ошибка', 'Выбери вариант!')
        return
    if selected == btn_ant1:
        show_variant1()
    elif selected == btn_ant2:
        show_variant2()
    elif selected == btn_ant3:
        show_variant3()
    elif selected == btn_ant4:
        show_variant4()
    main_win.close()
    main_win1.show()


btn_OK1 = QPushButton("Ответить")
btn_OK1.clicked.connect(check_answer1)

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(frage, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn_ant1, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn_ant2, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn_ant3, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn_ant4, alignment= Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

layout_main.addStretch(1)
layout_main.addWidget(btn_OK1, alignment = Qt.AlignCenter)

main_win.setLayout(layout_main)


#ВОПРОС НОМЕР 2

main_win1 = QWidget()
main_win1.setWindowTitle("КАКОЙ ТЫ УРОВЕНЬ ТОКСИКА В ИГРЕ")
main_win1.resize(900, 700)

frage1 = QLabel("На тебя накричали в войс чате после смерти")

RadioGroupBox1 = QGroupBox("Варики ответов")

btn_ant11 = QRadioButton("пишешь «sorry, my bad» или «gg next»")
btn_ant12 = QRadioButton("молчишь, но внутри кипишь")
btn_ant13 = QRadioButton("пишешь «ты сам 0-7. Сам же бездарь»")
btn_ant14 = QRadioButton("пишешь «gg end» на 2-й минуте")

RadioGroup2 = QButtonGroup()
RadioGroup2.addButton(btn_ant11)
RadioGroup2.addButton(btn_ant12)
RadioGroup2.addButton(btn_ant13)
RadioGroup2.addButton(btn_ant14)

def check_answer2():
    selected1 = RadioGroup2.checkedButton()
    if not selected1:
        QMessageBox.warning(main_win1, 'Ошибка', 'Выбери вариант!')
        return
    if selected1 == btn_ant11:
        show_variant11()
    elif selected1 == btn_ant12:
        show_variant12()
    elif selected1 == btn_ant13:
        show_variant13()
    elif selected1 == btn_ant14:
        show_variant14()
    main_win1.close()
    main_win2.show()
btn_OK2 = QPushButton("Ответить")
btn_OK2.clicked.connect(check_answer2)

layoutH11 = QHBoxLayout()
layoutH12 = QHBoxLayout()
layoutH13 = QHBoxLayout()
layoutH11.addWidget(frage1, alignment= Qt.AlignCenter)
layoutH12.addWidget(btn_ant11, alignment= Qt.AlignCenter)
layoutH12.addWidget(btn_ant12, alignment= Qt.AlignCenter)
layoutH13.addWidget(btn_ant13, alignment= Qt.AlignCenter)
layoutH13.addWidget(btn_ant14, alignment= Qt.AlignCenter)
layout_main1 = QVBoxLayout()
layout_main1.addLayout(layoutH11)
layout_main1.addLayout(layoutH12)
layout_main1.addLayout(layoutH13)

layout_main1.addStretch(2)
layout_main1.addWidget(btn_OK2, alignment = Qt.AlignCenter)

main_win1.setLayout(layout_main1)




#ВОПРОС НОМЕР 3

main_win2 = QWidget()
main_win2.setWindowTitle("КАКОЙ ТЫ УРОВЕНЬ ТОКСИКА В ИГРЕ")
main_win2.resize(900, 700)

frage2 = QLabel("Твой тиммейт забрал у тебя последний хит на 300 золота и написал «sorry bro»")

RadioGroupBox2 = QGroupBox("Варики ответов")

btn_ant111 = QRadioButton("пишешь «np, good luck» и продолжаешь играть")
btn_ant122 = QRadioButton("молчишь, но внутри тебя всё кипит")
btn_ant133 = QRadioButton("пишешь «ты серьёзно? это мой фарм был»")
btn_ant144 = QRadioButton("начинаешь спамить «???», «report this cunt», «delete game»")

RadioGroup3 = QButtonGroup()
RadioGroup3.addButton(btn_ant111)
RadioGroup3.addButton(btn_ant122)
RadioGroup3.addButton(btn_ant133)
RadioGroup3.addButton(btn_ant144)

def check_answer3():
    selected2 = RadioGroup3.checkedButton()
    if not selected2:
        QMessageBox.warning(main_win2, 'Ошибка', 'Выбери вариант!')
        return
    if selected2 == btn_ant111:
        show_variant111()
    elif selected2 == btn_ant122:
        show_variant122()
    elif selected2 == btn_ant133:
        show_variant133()
    elif selected2 == btn_ant144:
        show_variant144()
    main_win2.close()

btn_OK3 = QPushButton("Ответить")
btn_OK3.clicked.connect(check_answer3)

layoutH111 = QHBoxLayout()
layoutH122 = QHBoxLayout()
layoutH133 = QHBoxLayout()
layoutH111.addWidget(frage2, alignment= Qt.AlignCenter)
layoutH122.addWidget(btn_ant111, alignment= Qt.AlignCenter)
layoutH122.addWidget(btn_ant122, alignment= Qt.AlignCenter)
layoutH133.addWidget(btn_ant133, alignment= Qt.AlignCenter)
layoutH133.addWidget(btn_ant144, alignment= Qt.AlignCenter)
layout_main2 = QVBoxLayout()
layout_main2.addLayout(layoutH111)
layout_main2.addLayout(layoutH122)
layout_main2.addLayout(layoutH133)

layout_main2.addStretch(2)
layout_main2.addWidget(btn_OK3, alignment = Qt.AlignCenter)

main_win2.setLayout(layout_main2)

main_win.show()

app.exec_()