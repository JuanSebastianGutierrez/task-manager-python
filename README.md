# 📝 Gestor de Tareas en Python

Un proyecto de consola (CLI) modular desarrollado en Python para gestionar tareas diarias. Este programa permite crear, visualizar, completar y eliminar tareas, guardando la información de forma persistente utilizando formato JSON.

## ✨ Características Principales

* **Operaciones CRUD Completas:**
  * **Crear:** Agrega nuevas tareas a tu lista.
  * **Leer:** Visualiza todas las tareas con su ID, descripción y estado (Pendiente/Completada).
  * **Actualizar:** Marca tareas específicas como completadas.
  * **Borrar:** Elimina tareas del registro.
* **Persistencia de Datos:** La información sobrevive al cierre del programa gracias a la lectura y escritura automática en un archivo `tareas.json`.
* **Arquitectura Limpia:** Separación de responsabilidades en diferentes módulos.

## 🗂️ Estructura del Proyecto

El código fuente se encuentra dentro de la carpeta `src/` y se divide en:

* `main.py`: Punto de entrada de la aplicación. Contiene el menú interactivo para el usuario.
* `tasks.py`: Contiene la lógica principal de la aplicación y la ejecución de las funciones.
* `database.py`: Se encarga exclusivamente de la conexión, lectura y guardado de datos en el archivo JSON.

## 🚀 Cómo ejecutar el proyecto

### Requisitos previos
* Python 3.x instalado en tu sistema.

### Pasos
1. Clona este repositorio en tu computadora:
   ```bash
   git clone [https://github.com/JuanSebastianGutierrez/task-manager-python.git](https://github.com/JuanSebastianGutierrez/task-manager-python.git)