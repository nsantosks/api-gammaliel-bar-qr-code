# API de Generación de Códigos de Barras y QR

> Una API unificada y fácil de usar, construida con FastAPI, para generar códigos de barras y códigos QR sobre la marcha.

Este proyecto ofrece una solución robusta y de alto rendimiento para la creación dinámica de imágenes de códigos de barras (Code128, EAN13, etc.) y códigos QR totalmente personalizables. Ideal para integrar en sistemas de inventario, aplicaciones de ticketing, marketing digital o cualquier proyecto que requiera la generación de códigos visuales.


## 🚀 Características Principales

*   **✅ Endpoint Unificado:** Accede a la generación de códigos de barras y QR a través de una sola API.
*   **GENERACIÓN DE CÓDIGOS DE BARRAS:** Soporte para múltiples estándares de la industria (Code128, EAN13, etc.) gracias a la librería `python-barcode`.
*   **🎨 Creación de Códigos QR Personalizables:** Genera códigos QR ajustando el tamaño, borde y colores para que coincidan con la identidad de tu marca.
*   **📚 Documentación Interactiva Automática:** Gracias a FastAPI, la API incluye una documentación interactiva (Swagger UI y ReDoc) disponible en los endpoints `/docs` y `/redoc` para probar la API directamente desde el navegador.
*   **🛡️ Manejo de Errores Robusto:** La API gestiona entradas inválidas y errores internos de forma elegante, devolviendo códigos de estado HTTP claros y mensajes descriptivos.

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python 3
*   **Framework:** FastAPI
*   **Servidor ASGI:** Uvicorn
*   **Generación de QR:** `qrcode`
*   **Generación de Códigos de Barras:** `python-barcode`

## 📦 Instalación y Puesta en Marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

**1. Clona el Repositorio**
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

**2. Crea y Activa un Entorno Virtual**
Es una buena práctica trabajar dentro de un entorno virtual.
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instala las Dependencias**
Este proyecto necesita un archivo `requirements.txt`. Si no lo tienes, créalo con el siguiente contenido:

**`requirements.txt`**:
```txt
fastapi
uvicorn[standard]
python-barcode[images]
qrcode[pil]
```

Luego, instala las dependencias con pip:
```bash
pip install -r requirements.txt
```

**4. Ejecuta la API**
Usa `uvicorn` para iniciar el servidor.
```bash
uvicorn main:app --reload
```
El flag `--reload` reiniciará el servidor automáticamente cada vez que hagas cambios en el código.

**5. ¡Prueba la API!**
Abre tu navegador y ve a [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs) para ver la documentación interactiva de Swagger UI y empezar a generar códigos.

## 📜 Endpoints de la API

Aquí tienes ejemplos de cómo usar los endpoints directamente:

#### Generar un Código de Barras (EAN-13)
```
http://127.0.0.1:8000/generate-barcode/?data=123456789012&barcode_type=ean13
```

#### Generar un Código QR Personalizado
```
http://127.0.0.1:8000/generate-qr/?data=https://www.linkedin.com/in/ingnsantos/&fill_color=navy&back_color=%23EEEEEE
```

## ✍️ Sobre el Autor

Este proyecto fue creado con ❤️ por **Ing. Nestor Santos**.

¡Conectemos! Puedes encontrarme en:
*   **LinkedIn:** [https://www.linkedin.com/in/ingnsantos/](https://www.linkedin.com/in/ingnsantos/)
*   **GitHub:** [tu-perfil-de-github] (¡No olvides añadirlo!)