SERVICIO DE CORREO CON FLASK
============================

Descripción:
------------
Este proyecto utiliza Flask (un microframework de Python) para crear un servidor web 
que muestra un formulario HTML. Cuando el usuario completa el formulario y lo envía, 
el servidor envía un correo electrónico con los datos ingresados.

Estructura del proyecto:
------------------------
prueba servicio correo/
├── mail_service.py              --> Script principal del servidor Flask
├── templates/
│   └── formulario_prueba.html   --> Formulario HTML

Requisitos:
-----------
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Flask

Pasos para ejecutar el servidor:
--------------------------------
1. Abrí una terminal y navegá a la carpeta del proyecto.
2. (Opcional pero recomendado) Crear y activar un entorno virtual:

   Linux/macOS:
   > python3 -m venv mi_entorno
   > source mi_entorno/bin/activate

3. Instalar Flask:
   > pip install flask

4. Ejecutar el servidor:
   > python mail_service.py

5. Abrir el navegador en:
   http://127.0.0.1:5000

Configuración del correo:
-------------------------
Dentro de mail_service.py, buscá la función send_email() y asegurate de configurar:
- El correo del remitente (el que envía el mensaje)
- Una contraseña de aplicación (no tu contraseña de Gmail normal)

Ejemplo:
send_email(asunto, cuerpo, 'tucorreo@gmail.com', [correo_destino], 'contraseña_app')

IMPORTANTE:
-----------
- Si usás Gmail, activá la verificación en dos pasos y generá una contraseña de aplicación:
  https://myaccount.google.com/apppasswords

- Para Hotmail/Outlook, podés usar smtp.office365.com con TLS en vez de SSL.

Notas adicionales:
------------------
- El formulario HTML debe estar en la carpeta "templates" para que Flask lo encuentre.
- El servidor es solo para pruebas, no para producción.
- Si el correo no llega, revisá:
  - Carpeta de SPAM
  - Contraseña incorrecta
  - Error en consola

///////////////////////////////////////////////////////////////////////////////
con deactivate salis del entorno
