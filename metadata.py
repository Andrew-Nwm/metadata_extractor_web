from exif import Image

def extract_metadata(file_path):
    try:
        with open(file_path, 'rb') as file:
            img = Image(file)
            if img.has_exif:
                metadata = {}
                for attribute in dir(img):
                    if not attribute.startswith('_') and attribute != 'get':
                        value = getattr(img, attribute)
                        if value:
                            metadata[attribute] = value
                return metadata
            else:
                return {"error": "No se encontraron metadatos EXIF en la imagen."}
    except Exception as e:
        return {"error": f"Error al extraer metadatos: {str(e)}"}