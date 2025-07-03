# main.py

# --- 1. IMPORTACIONES COMBINADAS ---
# Librerías comunes
import io
from fastapi import FastAPI, Response, Query, HTTPException

# Librerías específicas para QR
import qrcode

# Librerías específicas para Códigos de Barras
import barcode
from barcode.writer import ImageWriter


# --- 2. CREACIÓN DE LA APLICACIÓN (Ahora con un título más general) ---
app = FastAPI(
    title="API de Generación de Códigos",
    description="Una API centralizada para generar Códigos de Barras y Códigos QR.",
    version="2.0.0",  # ¡Subimos de versión!
)


# --- 3. ENDPOINT PARA CÓDIGOS DE BARRAS (El que ya tenías) ---
@app.get("/generate-barcode/", 
         tags=["Generador de Códigos"],
         summary="Genera un código de barras (Code128, EAN, etc.).")
def generate_barcode(
    data: str = Query(..., description="El texto o número a codificar."),
    barcode_type: str = Query("code128", description="El tipo de código de barras (ej. code128, ean13).")
):
    """
    Genera una imagen de código de barras y la devuelve como PNG.
    """
    try:
        # Busca la clase del código de barras solicitado
        barcode_class = barcode.get_barcode_class(barcode_type)
        
        # Genera la instancia del código de barras con un ImageWriter
        barcode_instance = barcode_class(data, writer=ImageWriter())
        
        # Escribe la imagen en un buffer en memoria
        buffer = io.BytesIO()
        barcode_instance.write(buffer)
        buffer.seek(0)
        
        # Devuelve la imagen como respuesta
        return Response(content=buffer.getvalue(), media_type="image/png")
        
    except barcode.errors.BarcodeNotFoundError:
        raise HTTPException(status_code=400, detail=f"El tipo de código de barras '{barcode_type}' no es válido.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocurrió un error al generar el código de barras: {str(e)}")


# --- 4. ENDPOINT PARA CÓDIGOS QR (Tu código, casi sin cambios) ---
@app.get("/generate-qr/", 
         tags=["Generador de Códigos"],
         summary="Genera un código QR personalizado.")
def generate_qr_code(
    data: str = Query(..., description="El texto o URL a codificar en el QR."),
    box_size: int = Query(10, ge=1, le=100, description="Tamaño de cada 'caja' del QR."),
    border: int = Query(4, ge=0, le=50, description="Grosor del borde del QR."),
    fill_color: str = Query("black", description="Color del código QR (nombre o hexadecimal)."),
    back_color: str = Query("white", description="Color del fondo (nombre o hexadecimal).")
):
    """
    Genera un código QR con personalización y lo devuelve como una imagen PNG.
    """
    if not data:
        raise HTTPException(status_code=400, detail="El parámetro 'data' no puede estar vacío.")

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        return Response(content=buffer.getvalue(), media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocurrió un error al generar el QR: {str(e)}")