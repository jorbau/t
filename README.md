# Pasos para Annita

## Poner en funcionamiento el contenedor

1 - Descargarse el repositorio
```
git clone https://github.com/LibreTranslate/LibreTranslate
```
2 - Montar el contenedor
```
docker build -f docker/Dockerfile --build-arg with_models=true -t libretranslate .
```
3 - Poner en funcionamiento el contenedor
```
docker run -it -p 5000:5000 libretranslate
```
## Usar la API

1 - Descargarse el archivo Translate.py que está en este repositorio

2 - Guardarlo en la carpeta donde esté el código de python con el que estás trabajando

EJEMPLO DE USO
```python
from Translate import Translate

Translate = Translate()

print(Translate.translate(text="Texto a traducir", only_text=True))
```

Por defecto ya detecta el idioma de origen y traduce al inglés, si pones only_text=True devuelve unicamente el texto traducido, si pones only_text=False devuelve el texto traducido, el idioma detectado y la confianza.




