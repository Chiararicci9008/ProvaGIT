# Creare una finestra colorata di 4 righe che al premere di un bottone fa comparire il
# numero delle righe che la compongono.

import tkinter as tk

def mostra_numero_righe():  # funzione che viene poi chiamata quando viene premuto il bottone della finestra
    numero_righe = 4
    risultato.config(text=f"La finestra ha {numero_righe} righe")

root = tk.Tk()  #creazione di un Tkinter
root.title("Finestra con numero righe")
root.geometry("700x500")  # dimensioni della finestra (cambiabili se non si rende la finestra fissa)
root.resizable(width=False, height=False)  # questo codice rende la finestra fissa

riga1 = tk.Frame(root, height=90, bg="red") # creazione 4 frame colorati per rappresentare le righe
riga2 = tk.Frame(root, height=90, bg="blue")
riga3 = tk.Frame(root, height=90, bg="pink")
riga4 = tk.Frame(root, height=90, bg="yellow")

riga1.pack(fill=tk.X)   # posizionamento dei frame nella finestra principale
riga2.pack(fill=tk.X)
riga3.pack(fill=tk.X)
riga4.pack(fill=tk.X)

mostra_bottone = tk.Button(root, text="Mostra il numero delle righe", command=mostra_numero_righe)
mostra_bottone.pack()   # creazione del bottone per mostrare il numero delle righe

risultato = tk.Label(root, text="", pady=10)    # creazione di un'etichetta iniziale per mostrare il risultato
risultato.pack()

root.mainloop() # avviamento del ciclo