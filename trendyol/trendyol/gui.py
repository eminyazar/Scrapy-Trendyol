import json
import tkinter as tk
from tkinter import ttk

# Tkinter penceresi oluştur
window = tk.Tk()
window.title("Scrapy Verileri")

# Pencere boyutunu ayarla (genişlik, yükseklik)
window.geometry("800x600")  # Daha büyük boyut

# Yatay kaydırma çubuğu ekleyin
scrollbar_x = ttk.Scrollbar(window, orient=tk.HORIZONTAL)  # Yatay kaydırıcı
scrollbar_y = ttk.Scrollbar(window, orient=tk.VERTICAL)  # Dikey kaydırıcı

# Listbox oluştur ve kaydırıcıları bağla
listbox = tk.Listbox(window, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set, width=100, height=30)
scrollbar_x.config(command=listbox.xview)  # Yatay kaydırıcıyı Listbox ile eşleştir
scrollbar_y.config(command=listbox.yview)  # Dikey kaydırıcıyı Listbox ile eşleştir

# JSON dosyasını UTF-8 ile oku
with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Verileri GUI'de göstermek için Listbox kullan
for item in data:
    product_titles = item.get("product_titles", [])
    product_names = item.get("product_names", [])
    product_prices = item.get("product_prices", [])

    for i in range(len(product_names)):
        listbox.insert(tk.END, f"{product_titles[i]} - {product_prices[i]} - {product_names[i]}")

# Kaydırıcıları ve Listbox'ı pencerede yerleştirin
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)  # Yatay kaydırıcı altta
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)  # Dikey kaydırıcı sağda
listbox.pack(fill=tk.BOTH, expand=True)  # Listbox alanı doldursun

# Tkinter penceresini başlat
window.mainloop()
