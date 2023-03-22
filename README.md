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


