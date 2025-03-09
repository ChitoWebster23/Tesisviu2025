import requests
import dns.resolver
import subprocess
from termcolor import colored


def buscar_subdominios(dominio, lista_subdominios, archivo_salida):
    subdominios_encontrados = []
    
    for sub in lista_subdominios:
        subdominio = f"{sub}.{dominio}"
        try:
            # Verifica si el subdominio responde con DNS
            dns.resolver.resolve(subdominio, "A")
            print(f"[+] Subdominio encontrado: {subdominio}")
            subdominios_encontrados.append(subdominio)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
            pass
    
    # Guarda los subdominios en un archivo
    with open(archivo_salida, "w") as f:
        for sub in subdominios_encontrados:
            f.write(sub + "\n")
    
    print(f"Subdominios guardados en {archivo_salida}")


 
def ejecutar_comando_linux(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def ejecutar_template_SQLi(comando):
    try:
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

        if(resultado.stdout.__contains__("sqli-boolean-based-get")):
            print("-----------------------------------------------------------------------------------------------")
            print(resultado.stdout)
            print("***********************************************************************************************")
        else:
            print("-----------------------------------------------------------------------------------------------")
            print(colored("No se encuentran vulnerabilidades", "blue","on_green"))
            print("***********************************************************************************************")
       

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Determinar Subdominios")
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
            archivo_salida = "subdominios_encontrados.txt"
    
            # Lista de subdominios comunes (se puede ampliarla)
            lista_subdominios = ["www", "mail", "ftp", "blog", "admin", "dev", "test", "cpanel", "webmail", "forum", "shop", "api", "beta", 
             "dashboard", "portal", "secure", "vpn", "help", "support", "cloud", "mobile", "static", "news", "office", "store", 
            "wiki", "status", "login", "monitor", "reports", "ads", "analytics", "assets", "billing", "chat", "cdn", "config", 
            "db", "download", "files", "git", "img", "invoice", "mailserver", "members", "my", "node", "panel", "partners", 
            "payments", "projects", "public", "services", "smtp", "staff", "staging", "sysadmin", "tools", "upload", "user", 
            "video", "vpn", "web", "www2", "app", "enterprise", "b2b", "devops", "internal", "sso", "auth", "assets", "marketing",
            "hr", "finance", "pay", "social", "training", "leads", "events", "prod", "testapi", "sandbox", "preprod", "development", 
            "live", "edge", "gateway", "authserver", "customer", "service", "preview", "backup", "old", "legacy", "new", "demo"]
            
            buscar_subdominios(dominio, lista_subdominios, archivo_salida)

        case "2":
            print("Seleccionaste la opción 2: SQL Injection")

            # Nombre del archivo (asegúrate de que exista en la misma carpeta o usa la ruta completa)
            nombre_archivo = "ListadoURL.txt"

            try:
                # Intentar abrir el archivo en modo lectura
                with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                # Leer línea por línea e imprimir
                    for linea in archivo:
                        URL = linea.strip()  # .strip() elimina los saltos de línea adicionales
                        ejecutar_template_SQLi("nuclei -u "+URL+" -t templatesNuclei/SQLi/SQLi.yaml -dast")

            except FileNotFoundError:
                print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
            except Exception as e:
                print(f"Error inesperado: {e}")



            #ejecutar_comando_linux("ping -c 3 google.com")

        case "3":
            print("Seleccionaste la opción 3")
        case "4":
            print("Seleccionaste la opción 4")
        case "5":
            print("Seleccionaste la opción 5")
        case "6":
            print("Seleccionaste la opción 6")
        case "7":
            print("Seleccionaste la opción 7")
        case "8":
            print("Seleccionaste la opción 8")
        case "9":
            print("Seleccionaste la opción 9")
        case _:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    opcion = mostrar_menu()
    procesar_opcion(opcion)
