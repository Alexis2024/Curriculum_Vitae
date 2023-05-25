from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Función para convertir HTML a PDF
def convert_html_to_pdf(html_file, pdf_file, context):
    # Configurar el entorno de Jinja2
    env = Environment(loader=FileSystemLoader(os.path.dirname(html_file)))

    # Cargar el archivo HTML y renderizar con el contexto
    template = env.get_template(os.path.basename(html_file))
    rendered_html = template.render(context)

    # Convertir HTML a PDF
    with open(pdf_file, 'w+b') as file:
        pisa_status = pisa.CreatePDF(rendered_html, dest=file)

    if not pisa_status.err:
        print("PDF creado correctamente")
    else:
        print(f"Error al crear el PDF: {pisa_status.error}")


def select_photo():
    # Abre el cuadro de diálogo de selección de archivo
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def taller_23_pdf():
    usuario = {}
    usuario['Nombres'] = input("Ingrese sus nombres: ")
    usuario['Apellidos'] = input("Ingrese sus apellidos: ")
    usuario['Cedula'] = input("Ingrese su número de cédula: ")
    usuario['Sexo'] = input("Ingrese su sexo: ")
    usuario['Fexha_nacimiento'] = input("Ingrese su fecha de nacimiento: ")
    usuario['Correo'] = input("Ingrese su correo electrónico: ")
    usuario['Estado_Civil'] = input("Ingrese su estado civil: ")
    usuario['Domicilio'] = input("Ingrese su domicilio: ")
    usuario['Formacion1'] = input("Ingrese su formación académica (primaria): ")
    usuario['Formacion2'] = input("Ingrese su formación académica (secundaria): ")
    usuario['Formacion3'] = input("Ingrese su formación académica (universidad): ")
    usuario['Curso1'] = input("Ingrese su carrera y semestre cursando: ")
    usuario['Firma1'] = input("Ingrese su firma: ")

    # Seleccionar ruta de la foto
    foto_path = select_photo()
    usuario['Foto'] = foto_path

    context = {'usuario': usuario}

    # Ruta del archivo HTML de destino
    html_file = 'index.html'
    # Ruta del archivo PDF de destino
    pdf_file = 'archivo.pdf'
    # Convertir HTML a PDF con el contexto
    convert_html_to_pdf(html_file, pdf_file, context)


taller_23_pdf()
