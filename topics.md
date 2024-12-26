Ecco una guida completa e strutturata con tutti gli argomenti trattati in questo progetto. Ogni sezione include una spiegazione e un esempio pratico.

---

## **Guida Python: Argomenti Trattati**

### 📌 **1. Variabili**
Le variabili sono contenitori per memorizzare dati. 
- **Sintassi**: `nome_variabile = valore`

**Esempio**:
```python
nome = "Luca"
eta = 30
print(f"Mi chiamo {nome} e ho {eta} anni.")
```

---

### 📌 **2. Tipi di Dati**
1. **Stringhe (`str`)**:
   ```python
   messaggio = "Ciao, mondo!"
   print(messaggio)
   ```

2. **Numeri interi (`int`)**:
   ```python
   numero = 42
   print(numero)
   ```

3. **Numeri decimali (`float`)**:
   ```python
   prezzo = 19.99
   print(prezzo)
   ```

4. **Booleani (`bool`)**:
   ```python
   acceso = True
   print(acceso)
   ```

---

### 📌 **3. Operatori**
1. **Confronto**:
   - `==` (uguale), `!=` (diverso), `<`, `>`, `<=`, `>=`
   ```python
   print(5 > 3)  # True
   print(10 == 15)  # False
   ```

2. **Aritmetici**:
   - Somma `+`, Sottrazione `-`, Moltiplicazione `*`, Divisione `/`, Modulo `%`
   ```python
   print(10 % 3)  # 1 (resto della divisione)
   ```

---

### 📌 **4. Stringhe**
1. **Accesso ai caratteri**:
   ```python
   parola = "Python"
   print(parola[0])  # P
   print(parola[-1])  # n
   ```

2. **Slicing**:
   ```python
   parola = "Python"
   print(parola[0:3])  # Pyt
   ```

3. **Metodi utili**:
   - **`isalpha()`**: Verifica se tutti i caratteri sono lettere.
     ```python
     print("Python".isalpha())  # True
     print("Python3".isalpha())  # False
     ```
   - **`.find()`**: Trova la posizione di un carattere.
     ```python
     print("Hello".find("e"))  # 1
     ```

---

### 📌 **5. Funzioni**
Le funzioni sono blocchi di codice riutilizzabili.
- **Definizione**:
   ```python
   def saluta():
       print("Ciao!")
   saluta()
   ```

- **Con parametri**:
   ```python
   def somma(a, b):
       return a + b
   print(somma(3, 5))  # 8
   ```

- **Con valori predefiniti**:
   ```python
   def saluta(nome="Utente"):
       print(f"Ciao, {nome}!")
   saluta()  # Ciao, Utente!
   saluta("Luca")  # Ciao, Luca!
   ```

---

### 📌 **6. Scope delle Variabili**
1. **Globali**: Definite fuori dalle funzioni, visibili ovunque.
2. **Locali**: Definite dentro una funzione, visibili solo lì.

**Esempio**:
```python
x = 10  # Globale

def funzione():
    x = 5  # Locale
    print(x)  # 5

funzione()
print(x)  # 10
```

---

### 📌 **7. Cicli**
1. **Ciclo `for`**:
   ```python
   for i in range(5):
       print(i)  # Stampa da 0 a 4
   ```

2. **Ciclo con stringhe**:
   ```python
   for char in "Python":
       print(char)
   ```

3. **Condizioni nei cicli**:
   ```python
   for i in range(5):
       if i == 2:
           print("Trovato 2!")
       else:
           print(i)
   ```

---

### 📌 **8. Sequenze speciali**
1. **`pass`**: Segnaposto per il codice futuro.
   ```python
   def funzione_incompleta():
       pass
   ```

2. **`\n`**: Nuova riga.
   ```python
   print("Prima riga\nSeconda riga")
   ```

---

### 📌 **9. f-strings**
Permettono di interpolare valori nelle stringhe.
```python
nome = "Luca"
eta = 30
print(f"Mi chiamo {nome} e ho {eta} anni.")
```

---

### 📌 **10. Errori comuni**
1. **`TypeError`**: Tipo di dato non valido.
   ```python
   print("Ciao" + 5)  # Errore
   ```

2. **`NameError`**: Variabile non definita.
   ```python
   print(x)  # Errore
   ```

3. **`IndexError`**: Indice fuori dall'intervallo.
   ```python
   lista = [1, 2, 3]
   print(lista[5])  # Errore
   ```

---
