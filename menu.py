
import subprocess
from termcolor import colored
import json


def buscar_Crawling(comando):
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

def ejecutar_template(comando,titleTemplate):
    try:
    
        print(comando)

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


def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Realizar Crawling")
    print("2. SQL Injection")
    print("3. ByPass Authentication")
    print("4. Path Traversal ")
    print("5. XSS ")
    print("6. CSRF")
    
    opcion = input("Seleccione una opción (1-6): ")
    return opcion

def procesar_opcion(opcion):
    match opcion:
        case "1":
        
            dominio = input("Ingrese el dominio (ejemplo.com): ")
            comando = "katana -u "+ dominio
            
            buscar_Crawling(comando)

        case "2":
            print("Seleccionaste la opción 2: SQL Injection")

            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "SQLinjection"

            print("\nElija el tipo de ataque SQLi:")
            print("1. Basado en Payload clásicos (or 1=1 por ejemplo)")
            print("2. Basado en tiempo")

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


        case "3":
            
            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "BypassAuthentication"

            print("\nElija el tipo de Bypass Authentication:")
            print("1. Basado en Fuerza Bruta")
            print("2. Basado Injección SQL para saltar autenticación")

            opcion = input("Seleccione una opción (1-2): ")

            try:
                if opcion == "1":

                    path = input("ingrese el path a evaluar (por ejemplo: login o index.php): ")

                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']

                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+" -var endpoint="+path,idTemplate)
                
                elif opcion == "2":
                    
                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']

                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate,idTemplate)

                else:
                    print("Opcion no valida")

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        case "4":
            
            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "PathTraversal"
            opcion = 1

            try:
                    confTemplate = buscar_conf_template(titulovuln,opcion)

                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']
                
                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate,idTemplate)
               

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        case "6":
            print("Seleccionaste la opción 6: CSRF")
            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"
            titulovuln = "CSRF"

            print("\nLa url necesita cookie de sesion:")
            print("1. SI")
            print("2. NO")

            opcion = input("Seleccione una opción (1-2): ")

            try:
                if opcion == "1":
                    cookieSession = input("Ingrese cookie (nombre=valor;nombre=valor):")
                    confTemplate = buscar_conf_template(titulovuln,opcion)
                    PathTemplate = confTemplate['path']
                    idTemplate = confTemplate['idtemplate']
                    print("Analizando Vulnerabilidades...")


                    # Intentar abrir el archivo en modo lectura
                    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                    # Leer línea por línea e imprimir
                        for linea in archivo:
                            URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                            ejecutar_template("nuclei -u "+URL+" -t "+PathTemplate+" -H Cookie:"+cookieSession,idTemplate)
                
                elif opcion == "2":

                    print("Analizando Vulnerabilidades...")
                    confTemplate = buscar_conf_template(titulovuln,"1")

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
        case "5":
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
        case _:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    opcion = mostrar_menu()
    procesar_opcion(opcion)
