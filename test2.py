# А ЭТО МАСТЕР-ЛОМАСТЕР УЖЕ

from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk

def exchange():
    code = combobox.get() # Получить валюту из поля
    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            data = response.json() # Преобразовали в JSON

            if code in data["rates"]:
                exchange_rates = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rates:.1f} {code} за 1 доллар")

        except Exception as er:
            mb.showerror("Ошибка", f"Произошла ошибка{er}")

window = Tk()
window.title("Конвертер валют")
window.geometry("400x500")

Label(text = "Введите код валюты").pack(pady = 10)

#entry = Entry()
#entry.pack(pady = 10)

popular_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "RUB"]
combobox = ttk.Combobox(values = popular_cur)
combobox.pack(pady = 10)

ttk.Button(text = "Получить курс обмена к доллару", command = exchange).pack(pady = 10)




window.mainloop()