### Guida agli argomenti trattati nel progetto

Questa guida raccoglie i concetti e le tecniche principali affrontati nel progetto, organizzati per step e tematiche.

---

### **1. Camel Case, Pascal Case e Snake Case**
- **Camel Case**: Le parole sono concatenate senza spazi, con la prima lettera in minuscolo e le successive parole con l'iniziale maiuscola (es. `camelCaseExample`).
- **Pascal Case**: Simile al Camel Case, ma la prima lettera della stringa è maiuscola (es. `PascalCaseExample`).
- **Snake Case**: Le parole sono separate da underscore `_` e tutte in minuscolo (es. `snake_case_example`).

---

### **2. Metodi stringa utili**
- **`.isupper()`**: Verifica se un carattere è maiuscolo.
  ```python
  char = "A"
  print(char.isupper())  # Output: True
  ```
- **`.lower()`**: Converte un carattere maiuscolo in minuscolo.
  ```python
  char = "A"
  print(char.lower())  # Output: "a"
  ```
- **`.strip()`**: Rimuove caratteri iniziali e finali specificati.
  ```python
  string = "_example_"
  print(string.strip("_"))  # Output: "example"
  ```
- **`.join()`**: Combina gli elementi di una lista in una stringa.
  ```python
  characters = ['h', 'e', 'l', 'l', 'o']
  print(''.join(characters))  # Output: "hello"
  ```

---

### **3. Cicli tradizionali**
- Utilizzo di un ciclo `for` per iterare sui caratteri di una stringa e costruire una lista:
  ```python
  input_string = "CamelCase"
  snake_cased_char_list = []
  
  for char in input_string:
      if char.isupper():
          snake_cased_char_list.append("_")
          snake_cased_char_list.append(char.lower())
      else:
          snake_cased_char_list.append(char)
  print(snake_cased_char_list)
  # Output: ['c', 'a', 'm', 'e', 'l', '_', 'c', 'a', 's', 'e']
  ```

---

### **4. Concatenazione di metodi (Method Chaining)**
- Eseguire più operazioni in un'unica istruzione:
  ```python
  snake_cased_string = ''.join(snake_cased_char_list).strip('_')
  print(snake_cased_string)  # Output: "camel_case"
  ```

---

### **5. List Comprehension**
- Costruzione di una lista con una sintassi compatta:
  ```python
  snake_cased_char_list = [
      "_" + char.lower() if char.isupper() else char
      for char in pascal_or_camel_cased_string
  ]
  ```
- **Vantaggi**:
  - Codice più conciso e leggibile.
  - Maggiore efficienza rispetto ai cicli tradizionali.

---

### **6. Integrazione del progetto**
Unione di tutti i concetti per costruire un programma completo che converta una stringa da **Camel Case** o **Pascal Case** a **Snake Case**:

```python
# Input string in Camel Case or Pascal Case
pascal_or_camel_cased_string = "PascalCase"

# Use a list comprehension to convert to Snake Case
snake_cased_char_list = [
    "_" + char.lower() if char.isupper() else char
    for char in pascal_or_camel_cased_string
]

# Join the characters into a single string and remove extra underscores
clean_snake_cased_string = ''.join(snake_cased_char_list).strip('_')

print(clean_snake_cased_string)  # Output: "pascal_case"
```

---
