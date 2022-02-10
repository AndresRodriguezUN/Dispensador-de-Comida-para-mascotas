# Firmware :man_technologist:
El firmware de todo el proyecto se desarrolla en micropython, el cual es una version renderizada de python para poder ejecutarse en microcontroladores como lo es el ESP32. Se decidio utilizar micropython debido a su practicidad y la documentacion amplia que tiene en distintos repositorios. Con respecto al ESP32 cabe destacar que se debe flashear con micropython para que todos los códigos en python que se deseen emplear se ejecuten a la perfección. Adicionalmente, cabe aclarar que el archivo nombrado como **main.py** será el que se ejecute siempre que se reinicia el microcontrolador.

## Funcionalidad deseada

- Motor: Encargado de la rotación del plato en el cual estan alojadas cada una de las porciones de comida.
- OLED: Encargado de dar una retroalimentación visual, en el dispositivo, del estado de la mascota.
- DFP y Parlante: Encargados de reproducir una pista de audio que avise a la mascota cuando llegue la hora de comer.
- PIR: Encargado de detectar si la mascota se acerca al dispositivo dispensador de comida, para evaluar indirectamente su estado de ánimo.
- Infrarrojo: Encargado de detectar si la mascota ha comido alguna parte de su ración, para evaluar indirectamente su estado de ánimo.

## main.py

<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>


<p align="center">
  <img src="f1.png" align="center" width = 450>
</p>

## wlan.py

## OLED.py

## DFP.py

## motor.py





