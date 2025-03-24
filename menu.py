
import subprocess
from termcolor import colored
import json


def buscar_subdominios(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado.stdout)

        with open("ListadoURL.txt", "w") as archivo:
            print(resultado.stdout, file=archivo)

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

def buscar_conf_template(titleTemplate, opcionTemplate):
    
    try:

        # Cargar el archivo JSON
        with open("templatesconf.json", "r") as file:
            data = json.load(file)

         # Verificar si el título existe en los datos
        if titleTemplate in data:
            
            templates = data[titleTemplate]

            for template in templates:
            
                if int(template.get("numero")) == int(opcionTemplate):

                    return {
                        "path": template.get("path"),
                        "idtemplate": template.get("idtemplate")
                    }
                
        print("No se encontró el template solicitado.")
        return None
        
    except FileNotFoundError:
        print("El archivo templates.json no se encuentra.")
    except json.JSONDecodeError:
        print("El archivo templates.json tiene un formato incorrecto.")
    except Exception as e:
        print(f"Error inesperado: {e}")


 
def ejecutar_comando_linux(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def ejecutar_template(comando,titleTemplate):
    try:
    
        
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

        if(resultado.stdout.__contains__(titleTemplate)):
            print("-----------------------------------------------------------------------------------------------")
            print(colored("Se identificaron las siguientes vulnerabilidades: ", "black","on_red"))
            print("-----------------------------------------------------------------------------------------------")
            print(resultado.stdout)
            print("***********************************************************************************************")
        else:
            print("-----------------------------------------------------------------------------------------------")
            print(colored("No se encuentran vulnerabilidades en esta URL", "blue","on_green"))
            print("***********************************************************************************************")
       

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

def ejecutar_template_ByPassAuth(comando):
    try:
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

        if(resultado.stdout.__contains__("login-bruteforce-check")):
            print("-----------------------------------------------------------------------------------------------")
            print(resultado.stdout)
            print("***********************************************************************************************")
        elif(resultado.stdout.__contains__("sqli-boolean-based-post")):
            print("-----------------------------------------------------------------------------------------------")
            print(resultado.stdout)
            print("***********************************************************************************************")
        else:
            print("-----------------------------------------------------------------------------------------------")
            print(colored("No se encuentran vulnerabilidades en esta URL", "blue","on_green"))
            print("***********************************************************************************************")
       

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Realizar Crawling")
    print("2. SQL Inyection")
    print("3. ByPass Authentication")
    print("4. Path Traversal ")
    print("5. Access Control")
    print("6. Command Injection")
    print("7. XSS ")
    print("8. CSRF")
    print("9. Command Injection")
    
    opcion = input("Seleccione una opción (1-9): ")
    return opcion

def procesar_opcion(opcion):
    match opcion:
        case "1":
        
            dominio = input("Ingrese el dominio (ejemplo.com): ")
            comando = "katana -u "+ dominio
            
            buscar_subdominios(comando)

        case "2":
            print("Seleccionaste la opción 2: SQL Injection")

            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "SQLinjection"

            print("\nElija el tipo de ataque SQLi:")
            print("1. Basado en Payload clásicos (or 1=1 por ejemplo)")
            print("2. Basado en timmpo")

            opcion = input("Seleccione una opción (1-2): ")

            try:
                if opcion == "1":
                    print("Analizando Vulnerabilidades...")
                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']


                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+" -dast",idTemplate)
                elif opcion == "2":
                    print("Analizando Vulnerabilidades...")

                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']

                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+" -dast",idTemplate)

                else:
                    print("Opcion no valida")

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")



            #ejecutar_comando_linux("ping -c 3 google.com")

        case "3":
            
            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"

            print("\nElija el tipo de Bypass Authentication:")
            print("1. Basado en Fuerza Bruta")
            print("2. Basado Injección SQL para saltar autenticación")

            opcion = input("Seleccione una opción (1-2): ")

            try:
                if opcion == "1":

                    path = input("ingrese el path a evaluar (por ejemplo: login o index.php): ")  

                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template_ByPassAuth("nuclei -u "+URL+" -t /home/kali/Documents/tesisgit/Tesisviu2025/templatesNuclei/Authentication/login-bypass-detect.yaml -var endpoint=/"+path)
                else:
                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template_ByPassAuth("nuclei -u "+URL+" -t /home/kali/Documents/tesisgit/Tesisviu2025/templatesNuclei/Authentication/sqli-boolean-based-post.yaml")

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        case "4":
            print("Seleccionaste la opción 4")
        case "5":
            print("Seleccionaste la opción 5")
        case "6":
            print("Seleccionaste la opción 6")
        case "7":
            print("Seleccionaste la opción 7: XSS")
            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "XSS"

            print("\nElija el tipo de ataque XSS:")
            print("1. XSS reflejado")
            print("2. XSS based DOM")

            opcion = input("Seleccione una opción (1-2): ")

            try:
                if opcion == "1":
                    print("Analizando Vulnerabilidades...")
                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']


                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+"",idTemplate)
                elif opcion == "2":
                    print("Analizando Vulnerabilidades...")
                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']

                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+"",idTemplate)

                else:
                    print("Opcion no valida")

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        case "8":
            print("Seleccionaste la opción 8")
        case "9":
            print("Seleccionaste la opción 9")
        case _:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    opcion = mostrar_menu()
    procesar_opcion(opcion)
