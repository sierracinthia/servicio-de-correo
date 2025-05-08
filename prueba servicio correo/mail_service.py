from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def home():
    return render_template('formulario_prueba.html')  # Asegúrate de que el archivo esté en la carpeta 'templates'

# Ruta para procesar el formulario y enviar el correo
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']  # Este es el correo del destinatario
        seleccion = request.form['seleccion']

        # Crear el asunto y el cuerpo del correo
        subject = seleccion  # El asunto será lo que se seleccionó en el formulario
        intro_text = "Gracias por ponerte en contacto con nosotros. A continuación, te enviamos los detalles de tu solicitud:\n\n"
        body = intro_text + f"Nombre: {nombre}\nCorreo: {correo}\nOpción seleccionada: {seleccion}"
        
        # Definir el archivo PDF a enviar basado en la selección
        if seleccion == "analisis clinicos":
            filename = 'clinicosMaterias.pdf'
        elif seleccion == "analisis de sistemas":
            filename = 'sistemasMaterias.pdf'
        elif seleccion == "administracion contable":
            filename = 'contableMaterias.pdf'
        elif seleccion == "gestion ambiental y salud":
            filename = 'gestionMaterias.pdf'
        else:
            filename = None

        print(f"Seleccion: {seleccion}")
        print(f"Archivo a enviar: {filename}")
        print(f"Nombre: {nombre} | Correo: {correo}")

        # Enviar el correo con el archivo adjunto
        send_email(subject, body, 'cinthiasierra999@gmail.com', [correo], 'cmxbtyuazsvdwaan', filename)

        return 'Formulario enviado con éxito!'

# Función para enviar el correo con archivo adjunto
def send_email(subject, body, sender, recipients, password, filename=None):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Cuerpo del correo
    msg.attach(MIMEText(body, 'plain','utf-8'))

    if filename:
        # Adjuntar el archivo PDF
        filepath = os.path.join('plan_de_estudios', filename)
        try:
            with open(filepath, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(part)
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no fue encontrado en la carpeta 'plan_de_estudios'.")

    # Enviar el correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print(f"\n[+] Email sent Successfully!\n")

if __name__ == '__main__':
    print(">>> Iniciando servidor Flask...")
    app.run(debug=True)
