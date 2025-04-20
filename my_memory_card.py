# Подключение библиотек
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QVBoxLayout, QHBoxLayout,
                             QMessageBox, QRadioButton, QGroupBox,
                             QButtonGroup)

# Создание класса для вопросов
class Question:
    def __init__(self, text, answers, right_answer):
        self.text = text  # Текст вопроса
        self.answers = answers  # Список вариантов ответа
        self.right_answer = right_answer  # Правильный ответ

# Функция для отображения результата
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

# Функция для отображения вопроса
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    
    # Перемешиваем ответы
    shuffle(current_question.answers)
    
    # Устанавливаем текст кнопок
    rbtn_1.setText(current_question.answers[0])
    rbtn_2.setText(current_question.answers[1])
    rbtn_3.setText(current_question.answers[2])
    rbtn_4.setText(current_question.answers[3])
    
    # Сбрасываем выбор радиокнопок
    rbtn_1.setAutoExclusive(False)
    rbtn_2.setAutoExclusive(False)
    rbtn_3.setAutoExclusive(False)
    rbtn_4.setAutoExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rbtn_1.setAutoExclusive(True)
    rbtn_2.setAutoExclusive(True)
    rbtn_3.setAutoExclusive(True)
    rbtn_4.setAutoExclusive(True)

# Функция для проверки ответа
def check_answer():
    global current_question
    checked_button = None
    
    # Определяем выбранную кнопку
    if rbtn_1.isChecked():
        checked_button = rbtn_1
    elif rbtn_2.isChecked():
        checked_button = rbtn_2
    elif rbtn_3.isChecked():
        checked_button = rbtn_3
    elif rbtn_4.isChecked():
        checked_button = rbtn_4
        
    # Проверяем правильность ответа
    if checked_button is not None and checked_button.text() == current_question.right_answer:
        result.setText("Правильно!")
    else:
        result.setText("Неправильно!")

# Функция для обработки нажатия кнопки
def test():
    if button.text() == 'Ответить':
        check_answer()
        show_result()
    else:
        next_question()

# Функция для перехода к следующему вопросу
def next_question():
    global current_index, current_question
    current_index += 1
    if current_index < len(questions):
        current_question = questions[current_index]
        question.setText(current_question.text)
        show_question()
    else:
        print("Вопросы закончились")

# Инициализация приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

# Группировка радиокнопок
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Группировка результатов
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('')  # Результат "Правильно" или "Неправильно"
right_answer_label = QLabel('')  # Показывает правильный ответ
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment=Qt.AlignCenter)
layout_res.addWidget(right_answer_label, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

# Кнопка для ответа
button = QPushButton('Ответить')

# Вопросы
question = QLabel('Какой национальности не существует?')
questions = [
    Question('Какой национальности не существует?', ['Энцы', 'Смурфы', 'Чулымцы', 'Алеуты'], 'Смурфы'),
    Question('Какой язык программирования был создан первым?', ['Python', 'C++', 'Fortran', 'Java'], 'Fortran'),
    Question('Какой корень у числа 36?', ['4','5','6','7'], '6'),
    Question('Сколько лапок у паука?', ['2','4','6','8'], '8'),
    Question('На каком языке создан этот проект?', ['C++','C#','JavaScript','Python'],'Python'),
    Question('Какой фрукт желтого цвета любят обезьяны?', ['Яблоко','Ананас','Картошка','Банан'],'Банан'),
    Question('Какой самый главный грех?', ['Жадность','Лень','Гнев','Гордыня'],'Гордыня'),
    Question('В каком городе вы читаете этот вопрос?', ['Владивосток','Тула','Москва','Тюмень'],'Тюмень'),
    Question('Сколько будет 4/(6-2)x2?', ['1','2','6','4'],'2'),
    Question('Какая столица Франции?', ['Париж', 'Лондон', 'Берлин', 'Рим'], 'Париж')
]
current_index = 0
current_question = questions[current_index]

# Отображение первого вопроса
show_question()

# Главная компоновка
line1 = QHBoxLayout()
line1.addWidget(question, alignment=Qt.AlignCenter)
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
line3.addWidget(button, alignment=Qt.AlignCenter)

glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

main_win.setLayout(glav)
AnsGroupBox.hide()

# Соединение сигналов и слотов
button.clicked.connect(test)

# Запуск приложения
main_win.show()
app.exec_()
# alignment = Qt.AlignHCenter
# alignment = Qt.AlignVCenter


# main_win.resize(400, 200)

# rbtn_3.clicked.connect(show_win)
# rbtn_1.clicked.connect(show_defeat)
# rbtn_2.clicked.connect(show_defeat)
# rbtn_4.clicked.connect(show_defeat)
# VBox.addLayout(line1)
# VBox.addLayout(line2)
# VBox.addLayout(line3)

# layout_line.addStretch(1)
# layout_line.addWidget(btn_OK, stretch=2)
# layout_line.addStretch(1)



# def show_win():
#     victory_win.setText('Верно! Вы выиграли гироскутер')
#     victory_win.exec_()
# def show_defeat():
#     victory_win.setText('Нет, в 2015 году. Вы выиграли фирменный плакат')
#     victory_win.exec_()