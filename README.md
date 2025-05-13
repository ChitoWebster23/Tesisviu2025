# Tesisviu2025

# 🔍 Automatización de Detección de Vulnerabilidades Web con Nuclei y Katana

Este proyecto forma parte del Trabajo de Fin de Máster en Ciberseguridad (2025) de Luis Webster y Fabián Morales. Consiste en una herramienta desarrollada en Python que permite automatizar la detección de vulnerabilidades web mediante el uso de Nuclei y Katana, dos herramientas Open Source ampliamente adoptadas en entornos de ciberseguridad ofensiva.

## 📌 Funcionalidades Principales

- Interfaz en Python para facilitar la interacción.
- Integración con Nuclei para pruebas de:
  - SQL Injection (SQLi)
  - Bypass Authentication
  - Path Traversal
  - Cross-Site Scripting (XSS)
  - CSRF
- Integración con Katana para crawling de URLs objetivo.
- Análisis masivo sobre múltiples URLs.
- Uso de plantillas YAML personalizadas y configurables.
- Presentación interactiva de resultados en consola.

## 🧰 Tecnologías utilizadas

- Python 3.x
- Nuclei (ProjectDiscovery)
- Katana (ProjectDiscovery)
- Golang
- JSON

## ⚙️ Requisitos del sistema

- Python 3.x
- Go 1.20 o superior
- Git (opcional)
- Sistemas operativos compatibles:
  - Windows 7/8/10/11 (64-bit)
  - Linux (Ubuntu, Debian, Kali, etc.)

## 🚀 Instalación

```bash
# Instalar Go si no está instalado
# Luego instalar Katana y Nuclei
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Clonar el repositorio
git clone https://github.com/ChitoWebster23/Tesisviu2025.git
cd Tesisviu2025
🛠️ Configuración
Asegúrate de tener la carpeta templatesNuclei con los templates necesarios.

Configura el archivo templatesconf.json con las rutas completas de los templates.

Coloca ListadoURL.txt en el mismo directorio de Menu.py (para URLs a analizar).

▶️ Ejecución
bash
Copiar
Editar
python Menu.py
Desde el menú puedes:

Realizar crawling con Katana

Ejecutar pruebas específicas de vulnerabilidad con Nuclei

Visualizar los resultados directamente en la terminal

📂 Estructura del Proyecto
bash
Copiar
Editar
Tesisviu2025/
│
├── Menu.py                 # Interfaz principal
├── templatesconf.json      # Configuración de templates
├── ListadoURL.txt          # URLs objetivo
├── templatesNuclei/        # Plantillas YAML personalizadas
└── README.md               # Este archivo
📖 Casos de uso
Auditoría rápida de aplicaciones web

Participación en programas de Bug Bounty

Análisis automatizado en entornos de pruebas y formación (DVWA, HackTheBox, etc.)

👥 Autores
Luis Webster – @ChitoWebster23
Fabián Morales - @Elffabi

📝 Licencia
Este proyecto se entrega como parte de un trabajo académico. Uso libre para fines educativos y de investigación. Para propósitos comerciales, contactar con los autores.
