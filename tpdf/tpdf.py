import os
import comtypes.client
import argparse
from colorama import init, Fore
from tqdm import tqdm
import time  # Para simular un progreso (esto se puede quitar en un caso real)

# Inicializa colorama
init(autoreset=True)

def convert_word_to_pdf(word_file, pdf_file):
    """
    Convierte un archivo de Word (.docx) a PDF.
    
    Args:
        word_file (str): Ruta del archivo de Word.
        pdf_file (str): Ruta donde se guardará el PDF.
    """
    # Asegúrate de que las rutas son absolutas
    word_file = os.path.abspath(word_file)
    pdf_file = os.path.abspath(pdf_file)
    
    # Inicia la aplicación de Word
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False  # Word se ejecuta en segundo plano
    
    # Abre el documento
    doc = word.Documents.Open(word_file)
    
    # Simula una barra de progreso (esto es solo un ejemplo, puedes ajustar el progreso real)
    print(Fore.YELLOW + "Iniciando conversión... Esto puede tardar unos segundos.")
    
    # Barra de progreso para la conversión
    for _ in tqdm(range(100), desc="Convirtiendo", ncols=100, bar_format=Fore.LIGHTBLUE_EX+"{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.03)  # Simula el proceso (remover o ajustar este `sleep` en producción)

    # Exporta como PDF
    doc.SaveAs(pdf_file, FileFormat=17)  # 17 es el formato para PDF
    
    # Cierra el documento y Word
    doc.Close()
    word.Quit()

def main():
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description='Convierte un archivo DOCX a PDF.')
    parser.add_argument('word_file', help='Ruta del archivo DOCX a convertir')
    
    args = parser.parse_args()
    
    # Determina la ruta del archivo PDF de salida
    word_file_path = args.word_file
    if not word_file_path.endswith('.docx'):
        print(Fore.RED + "El archivo debe tener extensión .docx")
        return
    
    # Define el nombre del archivo PDF (sin la extensión .docx)
    pdf_file_path = os.path.splitext(word_file_path)[0] + '.pdf'
    
    # Llama a la función para convertir el archivo
    convert_word_to_pdf(word_file_path, pdf_file_path)
    
    # Mensaje de éxito con color verde
    print(Fore.GREEN + f"El archivo se ha convertido a: {pdf_file_path}")

if __name__ == "__main__":
    main()
