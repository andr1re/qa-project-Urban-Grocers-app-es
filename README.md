# Proyecto Urban Grocers 

Andrea Salcedo Morales, grupo 18, Sprint 7. Introducción a la automatización de pruebas. 

-Descripción del proyecto: revisión de la creación de kits de productos en la aplicación Urban Grocers a partir de una lista de comprobación.

-Fuente de documentación: apidoc

-Tecnologías utilizadas e instalación: 
*Python
  https://www.python.org/downloads/
*PyCharm
  https://www.jetbrains.com/pycharm/download/?section=windows#section=windows
*Pytest
Existen dos métodos para instalar Pytest:
  1️⃣ Usando el comando "pip" en la terminal:
En la terminal/consola se ingresa el comando "pip install pytest" (o "pip3", si "pip" no funciona).
  2️⃣ En PyCharm en la pestaña "Python Packages":
En el proyecto de PyCharm en el panel inferior seleccionar la pestaña "Python Packages".
Introducir "Pytest" en el campo de búsqueda. Luego seleccionar el paquete "Pytest" de la lista y hacer clic en el botón "Install".
*Librería requests
Se puede instalar de 2 maneras:
  1️⃣ Usando "pip", el gestor de paquetes de Python
En la terminal/consola se ingresa el comando "pip install requests" para instalar varios paquetes ya integrados en Python.
Si el comando pip no funciona, usar pip3 en su lugar.
  2️⃣ Mediante la pestaña "Python Packages"
En PyCharm en el panel inferior seleccionar la pestaña "Python Packages”. Escribir "requests" en la barra de búsqueda, seleccionar el paquete de la lista e instalar.

-Ejecución de pruebas
Hay 2 opciones para ejecutarlas, ya sea, directamente desde la consola de PyCharm o utilizando su interfaz gráfica.
1️⃣ Desde la terminal de PyCharm
En la pestaña "Terminal" en la parte inferior de PyCharm para ejecutar todas las pruebas del proyecto se escribe: pytest
Luego ejecuta las pruebas desde el archivo create_kit_name_kit_test.py con: pytest create_kit_name_kit_test.py
