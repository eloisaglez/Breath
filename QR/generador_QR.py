import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, VerticalBarsDrawer, SquareModuleDrawer, GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

def generar_qr_con_logo(data, logo_path, output_path):
    # 1. Configuración del QR
    # Usamos error_correction=high para que el QR funcione aunque el logo tape el centro
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 2. Crear la imagen del QR con estilo de "puntos/diamantes"
    # El 'GappedSquareModuleDrawer' o 'CircleModuleDrawer' dan ese aspecto moderno
    img_qr = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=GappedSquareModuleDrawer(), # Esto crea el efecto de puntos separados
        color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 0, 0))
    ).convert('RGB')

    # 3. Cargar e integrar el logo
    logo = Image.open(logo_path)
    
    # Calcular el tamaño del logo (aprox 25% del tamaño del QR)
    width, height = img_qr.size
    logo_size = width // 4
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # Calcular posición central
    pos = ((width - logo_size) // 2, (height - logo_size) // 2)

    # Crear un fondo blanco para el logo (opcional, ayuda a la legibilidad)
    # Si tu logo ya tiene fondo, puedes pegar el logo directamente
    img_qr.paste(logo, pos)

    # 4. Guardar resultado
    img_qr.save(output_path)
    print(f"¡QR generado con éxito en: {output_path}!")

# --- Uso del programa ---
datos = "https://eloisaglez.github.io/Breath/"
archivo_logo = "logo_stem4.png" # Asegúrate de que el archivo esté en la misma carpeta
nombre_salida = "qr_personalizado.png"

generar_qr_con_logo(datos, archivo_logo, nombre_salida)