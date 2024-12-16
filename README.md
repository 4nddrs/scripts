# 🚀 Scripts de Python para Automatizar Tareas

Bienvenido a mi colección de scripts de Python diseñados para automatizar diversas tareas. Estos scripts están pensados para ser simples, eficientes y fácilmente accesibles directamente desde la terminal mediante el uso de archivos `.bat` y variables de entorno del sistema.

---

## 📑 Índice

1. [Características](#-características)
2. [Como Funciona](#-como-funciona)
   - [Crea un Script de Python](#1️⃣-crea-un-script-de-python)
   - [Genera un Archivo `.bat`](#2️⃣-genera-un-archivo-bat)
   - [Añade el Archivo `.bat` a una Variable del Sistema](#3️⃣-añade-el-archivo-bat-a-una-variable-del-sistema)
   - [Invoca desde la Terminal](#4️⃣-invoca-desde-la-terminal)
3. [Estructura del Repositorio](#-estructura-del-repositorio)
4. [Ejemplos](#-ejemplos)
   - [Ejemplo: Automatizar una Tarea de Limpieza de Archivos 🗑️](#ejemplo-automatizar-una-tarea-de-limpieza-de-archivos-)
5. [Añadir Tus Propios Scripts](#-añadir-tus-propios-scripts)
6. [Contribuir](#-contribuir)

---

## ✨ Características
- ⚡ **Automatiza tareas repetitivas** con Python.
- 🖥️ **Invocación rápida** desde la terminal usando comandos personalizados.
- 🛠️ **Flexible y extensible** para diferentes casos de uso.

---

## 🛠️ Como Funciona

> **TIP:** Sigue estos pasos para integrar los scripts de manera eficiente en tu sistema. 🌟

### 1️⃣ Crea un Script de Python
Escribe un script de Python para automatizar una tarea específica. Cada script está diseñado para ejecutarse desde la línea de comandos y puede recibir argumentos necesarios.

### 2️⃣ Genera un Archivo `.bat`
Dentro de la misma carpeta donde se encuentra el script de Python, crea un archivo `.bat` para ejecutarlo. Por ejemplo, para un script llamado `ejemplo.py`:

```bat
@echo off
python "%~dp0\ejemplo.py" %*
```
> 💡 **Nota:** 
> - `%~dp0` asegura que el archivo `.bat` pueda encontrar el script Python dentro de su misma carpeta.  
> - `%*` permite que el archivo `.bat` pase todos los argumentos al script de Python.

### 3️⃣ Añade el Archivo `.bat` a una Variable del Sistema

🔗 **Windows:**
- Haz clic derecho en "Este Equipo" o "Mi PC" y selecciona "Propiedades."
- Ve a "Configuración avanzada del sistema" y haz clic en "Variables de entorno."
- Busca la variable `Path`, edítala y agrega el directorio que contiene el archivo `.bat`.

### 4️⃣ Invoca desde la Terminal
Usa el nombre del archivo `.bat` (sin la extensión) para ejecutar tu script directamente desde la terminal. Por ejemplo:

```bash
ejemplo arg1 arg2
```

---

## 📂 Estructura del Repositorio

```plaintext
.
├── script1/
│   ├── script1.py        # Script de Python
│   └── script1.bat       # Archivo .bat para el script
├── script2/
│   ├── script2.py        # Script de Python
│   └── script2.bat       # Archivo .bat para el script
├── README.md             # Documentación
└── LICENSE               # Información de licencia
```

---

## 📖 Ejemplos

### Ejemplo: Automatizar una Tarea de Limpieza de Archivos 🗑️

1️⃣ Crea un script `limpieza.py` dentro de la carpeta `limpieza/`:
```python
import os
import sys

def limpieza(carpeta):
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.tmp'):
            os.remove(os.path.join(carpeta, archivo))
            print(f"Eliminado: {archivo}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: limpieza <carpeta>")
        sys.exit(1)

    carpeta = sys.argv[1]
    limpieza(carpeta)
```

2️⃣ Crea un archivo `.bat` dentro de la misma carpeta llamado `limpieza.bat`:
```bat
@echo off
python "%~dp0\limpieza.py" %*
```

3️⃣ Añade la carpeta `limpieza/` a tu `PATH` e invoca el comando desde la terminal:
```bash
limpieza C:\temp
```

---

## ✍️ Añadir Tus Propios Scripts

1️⃣ **Crea una carpeta** para tu script.  
2️⃣ Guarda tu script de Python y el archivo `.bat` correspondiente dentro de esa carpeta.  
3️⃣ Agrega la carpeta al `PATH` del sistema para invocar el script desde cualquier lugar.  

> **TIP:** Mantén nombres descriptivos para tus carpetas y scripts para una gestión más sencilla. 🗂️

---

## 🧑‍🤝‍🧑 Contribuir
¡Las contribuciones son bienvenidas! Haz un fork de este repositorio, crea una rama con tus cambios y envía un pull request. 🙌

---

🌟 ¡Gracias por explorar este proyecto! Espero que estos scripts te ayuden a automatizar tus tareas de manera eficiente.
