# Aggiungere alla finestra precedente un campo e un bottone. Il bottone prende il
# valore del campo e stampa il valore + “è un tucano”.

import tkinter as tk

def mostra_numero_righe():  # funzione che viene poi chiamata quando viene premuto il bottone della finestra
    numero_righe = 4
    risultato.config(text=f"La finestra ha {numero_righe} righe")

def stampare_tucano():
    testo_input = campo_input.get()  # prende il testo inserito nel campo di input
    risultato.config(text=f"{testo_input} è un tucano")

root = tk.Tk()  # creazione di un Tkinter
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

campo_input = tk.Entry(root)    # si aggiunge il campo di input
campo_input.pack()

# si aggiunge ora il bottone per il tucano
stampare_tucano_bottone = tk.Button(root, text="Stampa Tucano", command=stampare_tucano)
stampare_tucano_bottone.pack()

# si riprende ora tutto l'esercizio, quello delle righe e quello del tucano

# si crea il bottone per mostrare il numero delle righe
mostra_bottone = tk.Button(root, text="Mostra il numero delle righe", command=mostra_numero_righe)
mostra_bottone.pack()

risultato = tk.Label(root, text="", pady=10)    # creazione di un'etichetta iniziale per mostrare il risultato
risultato.pack()

root.mainloop() # avviamento del ciclo