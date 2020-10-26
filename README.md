# microservice_API_Twitter

Microservicio desarrollado en pyhton.

- Una vez ejecutado el DockerFile, el programa se pone en funcionamiento.
- Se manda una JSON en petición POST a un servidor RESTFUL que está escuchando en mi localhost:5001 con la información necesaria.
- En dicha información hay una palabra clave sobre la cual se realizará un análisis de sentimiento.
- Este análisis de sentimiento se realizará, primero conectándose a la API de Twitter con unas credenciales, y posteriormente descargándose todos los tweets que se hayan subido en un intervalo de tiempo con la palabra a analizar.
- Posteriormente se guardarán dichas búsquedas en una base de datos a la que nos conectamos con analysis_twitter_handler.py

