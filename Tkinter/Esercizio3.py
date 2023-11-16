# Creare una calcolatrice che esegue le somme. La calcolatrice deve usare dei bottoni
# numerati per prendere in ingresso gli input, gli input vanno mostrati in una casella
# di testo e quando si preme uguale nella stessa casella di testo deve comparire il
# risultato della somma. Insomma… una calcolatric :) .

import tkinter as tk

def aggiungi_input(carattere):  # funzione per aggiungere un numero all'input
    input_text.insert(tk.END, carattere)

def calcola_risultato():    # funzione per aggiungere un numero o un operatore all'input
    espressione = input_text.get()
    try:
        risultato = eval(espressione)  # esegue il calcolo dell'espressione
        input_text.delete(0, tk.END)  # cancella l'input attuale
        input_text.insert(tk.END, str(risultato))  # mostra il risultato
    except Exception:
        input_text.delete(0, tk.END)
        input_text.insert(tk.END, "Errore")

root = tk.Tk()
root.title("Calcolatrice")

input_text = tk.Entry(root, font=("Arial", 18))
input_text.pack(fill=tk.BOTH, expand=True)

# definisce i numeri da 0 a 9 come se fosse una calcolatrice vera
numeri = "7894561230"

#cCrea i bottoni numerati
for numero in numeri:
    tk.Button(root, text=numero, font=("Arial", 18), command=lambda n=numero: aggiungi_input(n)).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# crea i bottoni degli operatori
operatori = "+-*/"
for operatore in operatori:
    tk.Button(root, text=operatore, font=("Arial", 18), command=lambda o=operatore: aggiungi_input(o)).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# bottone per il risultato
tk.Button(root, text="=", font=("Arial", 18), command=calcola_risultato).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()