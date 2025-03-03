import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def cesar_cipher(lang, k, text, dir):
    if lang.lower() == 'р':
        lower_start = ord('а')
        upper_start = ord('А')
        len_alph = 32 #Сделал 32, так как не учитывается ё
    elif lang.lower() == 'а':
        lower_start = ord('a')
        upper_start = ord('A')
        len_alph = 26
    else:
        messagebox.showerror("Ошибка", "Неверно выбран язык")
        return ""

    if dir.lower() == 'ш':
        k = k
    elif dir.lower() == 'д':
        k = -k
    else:
        messagebox.showerror("Ошибка", "Неверно выбрано направление")
        return ""

    new_text = ''
    for i in range(len(text)):
        if text[i].isalpha():
            cur_ord = ord(text[i])

            if text[i].islower():
                start = lower_start
            else:
                start = upper_start

            new_ord = ((cur_ord - start + k) % len_alph) + start
            new_chr = chr(new_ord)
            new_text += new_chr
        else:
            new_text += text[i]

    return new_text

def encrypt_decrypt():
    direction = direction_var.get()
    language = language_var.get()
    try:
        rot = int(rot_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный шаг сдвига. Введите целое число.")
        return
    user_text = input_text.get("1.0", "end-1c")  # Получаем текст из текстового поля
    result = cesar_cipher(language, rot, user_text, direction)
    output_text.delete("1.0", "end")  # Очищаем текстовое поле вывода
    output_text.insert("1.0", result)  # Вставляем результат

# Создаем главное окно
window = tk.Tk()
window.title("Шифр Цезаря")

# Создаем фрейм для направления
direction_frame = ttk.LabelFrame(window, text="Направление")
direction_frame.grid(row=0, column=0, padx=10, pady=10, sticky="we")

# Переменная для хранения выбранного направления
direction_var = tk.StringVar()
direction_var.set("ш")  # По умолчанию шифрование

# Радиокнопки для выбора направления
encrypt_radio = ttk.Radiobutton(direction_frame, text="Шифрование", variable=direction_var, value="ш")
decrypt_radio = ttk.Radiobutton(direction_frame, text="Дешифрование", variable=direction_var, value="д")
encrypt_radio.pack(side="left", padx=5)
decrypt_radio.pack(side="left", padx=5)

# Создаем фрейм для языка
language_frame = ttk.LabelFrame(window, text="Язык")
language_frame.grid(row=1, column=0, padx=10, pady=10, sticky="we")

# Переменная для хранения выбранного языка
language_var = tk.StringVar()
language_var.set("р")  # По умолчанию русский

# Радиокнопки для выбора языка
russian_radio = ttk.Radiobutton(language_frame, text="Русский", variable=language_var, value="р")
english_radio = ttk.Radiobutton(language_frame, text="Английский", variable=language_var, value="а")
russian_radio.pack(side="left", padx=5)
english_radio.pack(side="left", padx=5)

# Создаем фрейм для шага сдвига
rot_frame = ttk.LabelFrame(window, text="Шаг сдвига")
rot_frame.grid(row=2, column=0, padx=10, pady=10, sticky="we")

# Метка и поле ввода для шага сдвига
rot_label = ttk.Label(rot_frame, text="Шаг:")
rot_label.pack(side="left", padx=5)
rot_entry = ttk.Entry(rot_frame)
rot_entry.pack(side="left", padx=5)
rot_entry.insert(0, "3") #Значение по умолчанию

# Создаем фрейм для ввода текста
input_frame = ttk.LabelFrame(window, text="Ввод текста")
input_frame.grid(row=3, column=0, padx=10, pady=10, sticky="we")

# Текстовое поле для ввода текста
input_text = tk.Text(input_frame, width=40, height=10)
input_text.pack(padx=5, pady=5)

# Создаем фрейм для вывода текста
output_frame = ttk.LabelFrame(window, text="Вывод текста")
output_frame.grid(row=4, column=0, padx=10, pady=10, sticky="we")

# Текстовое поле для вывода текста
output_text = tk.Text(output_frame, width=40, height=10)
output_text.pack(padx=5, pady=5)

# Кнопка для шифрования/дешифрования
button = ttk.Button(window, text="Выполнить", command=encrypt_decrypt)
button.grid(row=5, column=0, padx=10, pady=10)

# Запускаем главный цикл
window.mainloop()
