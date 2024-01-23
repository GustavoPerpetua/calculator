from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="#F4F4F4")  # Configura el color de fondo

# Entry
e_text = Entry(window, font=("Helvetica", 24), borderwidth=5)
e_text.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=20, ipady=20)

# Funciones
def click_button(valor):
    if valor == "=":
        try:
            result = eval(e_text.get())
            e_text.delete(0, END)
            e_text.insert(0, str(result))
        except Exception:
            e_text.delete(0, END)
            e_text.insert(0, "Error")
    elif valor == "AC":
        e_text.delete(0, END)
    else:
        current_text = e_text.get()
        e_text.delete(0, END)
        e_text.insert(0, current_text + valor)

# Botones
button_texts = [
    ["AC", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "-"],
    ["0", ".", "="]
]

# Crear botones con estilo personalizado
for row_idx, row in enumerate(button_texts):
    for col_idx, label in enumerate(row):
        button = Button(window, text=label, width=5, height=2, command=lambda label=label: click_button(label), font=("Helvetica", 16))
        button.grid(row=row_idx + 1, column=col_idx, padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()
