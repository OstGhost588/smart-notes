import json

from PyQt5.QtWidgets import *

app = QApplication([])

notes = {}

window = QWidget()
WINDOW_BIG = QTextEdit()
window_small = QListWidget()
window_small2 = QListWidget()
list_of_notes_lbl = QLabel("Список заміток")
make_notes_btn = QPushButton("Створити замітку")
delete_notes_btn = QPushButton("Видалити замітку")
save_notes_btn = QPushButton("Зберегти замітку")
list_of_tegs_lbl = QLabel("Списщк тегів")
search_teg = QLineEdit("Знайти тег")
add_to_notes = QPushButton("Додати до заміток")
unfasten_notes = QPushButton("Відкріпити замітки")
search_notes_po_teg = QPushButton("Шукати замітки")

main_lain = QHBoxLayout()
h1 = QVBoxLayout()
h2 = QVBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()

window.setLayout(main_lain)
main_lain.addLayout(h1)
main_lain.addLayout(h2)



h1.addWidget(WINDOW_BIG)
h2.addWidget(window_small)
h2.addLayout(h3)
h3.addWidget(delete_notes_btn)
h3.addWidget(make_notes_btn)
h2.addWidget(save_notes_btn)
h2.addWidget(window_small2)
h2.addWidget(search_teg)
h2.addLayout(h4)
h4.addWidget(add_to_notes)
h4.addWidget(unfasten_notes)
h2.addWidget(search_notes_po_teg)

def read_data():
    global notes
    with open("database.json", "r", encoding="utf8",)as file:
        notes = json.load(file)

def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8")as file:
        json.dump(notes, file, ensure_ascii=False)
read_data()
window_small.addItems(notes)

def vmist_note():
    name = window_small.selectedItems()[0].text()
    WINDOW_BIG.setText(notes[name]["вміст"])

window_small.itemClicked.connect(vmist_note)
def change_note():
    name = window_small.selectedItems()[0].text()
    notes[name]["вміст"] = WINDOW_BIG.toPlainText()
    write_data()
def add_notes():
    res, ok = QInputDialog.getText(window,"Введення", "Введіть назву замітки")
    if ok:
        notes[res] = {
            "вміст":"",
            "теги": []
        }
        write_data()
save_notes_btn.clicked.connect(change_note)
make_notes_btn.clicked.connect(add_notes)
window.show()
app.exec()