from PyQt5.QtWidgets import *

app = QApplication([])

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


window.show()
app.exec()