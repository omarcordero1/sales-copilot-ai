# 🚀 Sales Copilot AI

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Asistente de IA para ventas B2B** que analiza prospectos, genera estrategias personalizadas y crea emails de alto impacto. Desarrollado con Streamlit y OpenAI.

## 📖 Descripción

**Sales Copilot AI** es una herramienta inteligente diseñada para equipos comerciales que buscan optimizar su proceso de prospección. A partir de datos básicos de un prospecto (nombre, empresa, cargo, industria), la aplicación:

- Analiza el perfil y contexto del prospecto.
- Identifica puntos de dolor y oportunidades de valor.
- Genera una estrategia de acercamiento personalizada.
- Redacta un email comercial listo para enviar.

Ideal para vendedores B2B que desean escalar su personalización sin perder tiempo.

## ✨ Características principales

- 🔍 **Análisis inteligente** de prospectos usando IA.
- 📧 **Generación automática** de emails personalizados.
- 🧠 **Estrategias de venta** basadas en el contexto del prospecto.
- ⚡ Interfaz rápida y amigable con **Streamlit**.
- 🔐 Manejo seguro de claves de API mediante variables de entorno.
- 🚀 Listo para desplegar en **Streamlit Cloud**, **Railway** o cualquier servidor.

## 🗂️ Estructura del proyecto
sales-copilot-ai/
├── app.py # Aplicación principal de Streamlit
├── ai_analyzer.py # Lógica de análisis con OpenAI
├── email_generator.py # Generación de emails personalizados
├── config_example.py # Ejemplo de archivo de configuración
├── requirements.txt # Dependencias del proyecto
├── .github/workflows/ # (Opcional) CI/CD con GitHub Actions
├── LICENSE # Licencia MIT
└── README.md # Este archivo

text

## 📋 Requisitos previos

- Python 3.9 o superior.
- Una cuenta de [OpenAI](https://platform.openai.com/) con una API Key válida.
- (Opcional) Cuenta en Streamlit Cloud para despliegue gratuito.

## 🛠️ Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/omarcordero1/sales-copilot-ai.git
   cd sales-copilot-ai
Crea y activa un entorno virtual (recomendado)

bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
Instala las dependencias

bash
pip install -r requirements.txt
Configura las variables de entorno

Copia el archivo de ejemplo:

bash
cp config_example.py config.py
Edita config.py y añade tu API Key de OpenAI:

python
OPENAI_API_KEY = "sk-..."
⚠️ Importante: No subas config.py al repositorio. Está en el .gitignore.

Ejecuta la aplicación

bash
streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador en http://localhost:8501.

🖥️ Uso
En la interfaz de Streamlit, completa los datos del prospecto:

Nombre

Empresa

Cargo

Industria

Haz clic en "Generar estrategia y email".

La IA analizará la información y te mostrará:

Un análisis detallado del prospecto.

Una estrategia de venta personalizada.

Un borrador de email comercial listo para copiar.

https://via.placeholder.com/800x400?text=Captura+de+pantalla+de+la+app
(Reemplaza esta imagen con una captura real de tu app)

☁️ Despliegue en la nube
Puedes desplegar esta aplicación fácilmente en Streamlit Cloud:

Sube tu repositorio a GitHub.

Ve a share.streamlit.com y haz clic en "New app".

Selecciona el repositorio, la rama y el archivo principal (app.py).

Añade tu OPENAI_API_KEY como secreto en la configuración del despliegue.

Haz clic en "Deploy".

La aplicación estará disponible en una URL pública.

🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

Haz un fork del repositorio.

Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').

Sube tus cambios (git push origin feature/nueva-funcionalidad).

Abre un Pull Request.

Por favor, asegúrate de que el código pase las verificaciones y sigue las buenas prácticas de Python.

📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

👤 Autor
Omar Said Cordero Lugo
GitHub

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella en GitHub!
📫 ¿Preguntas o sugerencias? Abre un issue o contacta al autor.
