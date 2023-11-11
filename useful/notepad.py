from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']


def change_fonts(fontss):
    text_field['font'] = fonts[fontss]['font']


def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()


root = Tk()
root.title('Text editor')
root.geometry('600x700')
root.iconbitmap('notepad.ico')

main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Close', command=notepad_exit)
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Theme', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('Comic'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('Times'))
view_menu.add_cascade(label='Font...', menu=font_menu_sub)
root.config(menu=view_menu)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

fonts = {
    'Arial': {
        'font':'Arial 10'
    },
    'Comic': {
        'font': ('Comic Sans MS', 10)
    },
    'Times': {
        'font': ('Times New Roman', 10)
    }
}

text_field = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Arial 10'
                 )
text_field.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()
