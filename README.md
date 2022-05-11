Prueba tecnica ingeniero de datos

* Se realizo todo el desarrollo con una base de datos Postgresql
  * Por favor añadir dentro de la base de datos postgres y dentro del schema
  * PUBLIC dos tablas llamadas
        * test -> columnas -> price, user_id, timestamp, execution_time
        * validation -> columnas -> total_count, average_value, min_value, max_value

Ejecutar un entorno virtual con el siguiente comando 
        *  python -m venv venv

Activar el entorno virtual con el siguiente comando
        * windows -> .\venv\Script\activate
        * linux -> /venv/bin/activate

Al activar el entorno virtual ejecutar el siguiente comando para que se instalen 
los paquetes necesarios y funcione
        * pip install -Ur requirements.txt   


Ejecutar el siguiente comando para que se active el servicio dentro de la siguiente
ruta
        ruta -> * /prueba_pragma/database
        comando ->  uvicorn main:app --reload 

Para que empiece a funcionar todo el pipeline ir a la siguiente ruta y ejecutar el
siguiente comando

        ruta -> * /prueba_pragma
        comando windows -> python .\main.py
        comando linux -> python ./main.py


Se puede validar que tenga o no datos por procesar luego de iniciarlo, los archivos
los deben dejar en la ruta

        ruta -> ./dataPruebaDataEngineer/
  