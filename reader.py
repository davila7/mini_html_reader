from bs4 import BeautifulSoup
import re

def extraer_preguntas(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontrar todas las secciones
    secciones = soup.find_all('div', class_='well well-sm')
    
    # Abrir archivo para escribir
    with open('preguntas_examen.txt', 'w', encoding='utf-8') as f:
        # Procesar cada sección
        for seccion in secciones:
            # Extraer pregunta
            pregunta = seccion.find('h4', class_='color-primary')
            if pregunta:
                texto_pregunta = pregunta.text.strip()
                # Limpiar el texto de la pregunta (eliminar "Guardar")
                texto_pregunta = re.sub(r'Guardar', '', texto_pregunta).strip()
                
                # Escribir la pregunta
                f.write(f"\nPREGUNTA:\n{texto_pregunta}\n\n")
                f.write("OPCIONES:\n")
                
                # Encontrar y escribir las opciones
                opciones = seccion.find_all('li', class_='col-xs-12')
                for opcion in opciones:
                    texto_opcion = opcion.find('a').text.strip()
                    es_correcta = 'active' in opcion.get('class', [])
                    marca = "✓" if es_correcta else " "
                    f.write(f"[{marca}] {texto_opcion}\n")
                
                f.write("\n" + "="*50 + "\n")  # Separador entre preguntas

# Leer el archivo HTML
with open('html.parser', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Procesar el contenido
extraer_preguntas(html_content)
print("¡Archivo preguntas_examen.txt creado exitosamente!")
