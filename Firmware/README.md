# Firmware :man_technologist:
El firmware de todo el proyecto se desarrolla en micropython, el cual es una version renderizada de python para poder ejecutarse en microcontroladores como lo es el ESP32. Se decidio utilizar micropython debido a su practicidad y la documentacion amplia que tiene en distintos repositorios. Con respecto al ESP32 cabe destacar que se debe flashear con micropython para que todos los códigos en python que se deseen emplear se ejecuten a la perfección. Adicionalmente, cabe aclarar que el archivo nombrado como **main.py** será el que se ejecute siempre que se reinicia el microcontrolador.

## Funcionalidad deseada

- Motor: Encargado de la rotación del plato en el cual estan alojadas cada una de las porciones de comida.
- OLED: Encargado de dar una retroalimentación visual, en el dispositivo, del estado de la mascota.
- DFP y Parlante: Encargados de reproducir una pista de audio que avise a la mascota cuando llegue la hora de comer.
- PIR: Encargado de detectar si la mascota se acerca al dispositivo dispensador de comida, para evaluar indirectamente su estado de ánimo.
- Infrarrojo: Encargado de detectar si la mascota ha comido alguna parte de su ración, para evaluar indirectamente su estado de ánimo.

## main.py

En primer lugar se adjuntan las librerias necesarias para el desarrollo del programa, asi como los modulos creados externamente que permiten reducir la cantidad de codigo gracias a la dinamica de programacion orientada a objetos.

<p align="center">
  <img src="/Imagenes/f1.png" align="center" width = 450>
</p>

Se plantean todas las variables globales que se utilizaran en el codigo para poder editarlas en cada una de las funciones y se puedan utilizar en todo el desarrollo del codigo.


<p align="center">
  <img src="/Imagenes/f2.png" align="center" width = 450>
</p>

En esta seccion se configuran los distintos perifericos de acuerdo a la necesidad que dictaban las correspondientes adecuaciones ya mencionadas.

<p align="center">
  <img src="/Imagenes/f3.png" align="center" width = 450>
</p>

Dado que se utilizo un Broker Mosquito para la comunicacion con la aplicacion, es necesario plantear la logica de recepcion de datos.

<p align="center">
  <img src="/Imagenes/f4.png" align="center" width = 450>
</p>

Asi mismo es importante establecer la conexion con el Broker MQTT, planteando un usuario y unos topicos de recepcion como de transmision de datos.

<p align="center">
  <img src="/Imagenes/f5.png" align="center" width = 450>
</p>

Este bloque de codigo permite extraer el reloj UTC de la web, y luego se acondiciona con condicionales para ajustarlo a la zona horaria en la cual estamos ubicados.

<p align="center">
  <img src="/Imagenes/f6.png" align="center" width = 450>
</p>



<p align="center">
  <img src="/Imagenes/f7.png" align="center" width = 450>
</p>




## wlan.py

El modulo wlan.py importa las librerias pertienentes para establecer la conexion WiFi, por medio de la clave y la contraseña del proveedor del usuario.

## OLED.py

El modulo OLED.py se ajusta de acuerdo al tamaño del OLED que se esta implementando, asi como un buffer que permite imprimir todo en el OLED al mismo tiempo.

## DFP.py

El modulo DFP.py se transcribio desde una referencia de un proyecto anteriormente realizado por el grupo. Y se adecuo al entorno de python para que funcionara el envio de datos al DFPlayer Mini.

## motor.py

El modulo motor.py coordina la activacion de las bobinas del motor paso a paso, segun lo indicado en los videos de referencia del proyecto.




