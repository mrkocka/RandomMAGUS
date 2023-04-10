from tkinter import *
import tkinter as tk

main = Tk()

#Ablak tulajdonságok
main.title('RandomGenerator')
main.configure(bg="#121411")
main.geometry('440x700')
main.resizable(False, False)

#Ablak elemek

#----Szöveg----
text = Label(main, text="Véletlen találkozások generátor", bg="#121411", fg="#ffffff", font=("Arial", 14, "bold"))

#----Kép----
# Képfájl betöltése
image_path = "./img/magus_logo2.png"
photo_image = tk.PhotoImage(file=image_path)
# Label widget létrehozása a képpel
label = tk.Label(main, image=photo_image, bg="#121411")

#MEGJELENÍTENDŐ ELEMEK
label.pack()
text.pack()


main.mainloop()