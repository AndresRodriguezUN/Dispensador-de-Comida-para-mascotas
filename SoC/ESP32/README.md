# Microcontrolador ESP32-WROOM

El microcontrolador ESP32 es un SoC basado en un procesador Xtensa LX6, el cual gracias a su hardware presta la funcionalidad de comunicacion inalambrica gracias a su modulo de WiFi y Bluetooth. Por lo tanto se decidio utilizar especificamente la version ESP32-WROOM del mismo ya que se acomodaba justamente a las necesidades de hardware que se requerian para el funcionamiento del dispositivo dispensador de comida para mascotas.

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>

El ESP32-WROOM32 cuenta con 38 pines de los cuales se emplearan UART's, pines digitales y analogicos. Para mas informacion sobre la descripcion de los pines remitirse a [esp32wroom](/Datasheets/esp32-wroom-32_datasheet_en.pdf).

## Adecuacion

Si bien el SoC del ESP32-WROOM viene con la adecuacion de sus perifericos internos y los modulos que implementa para funcionar. Es necesario realizar la adecuacion de este por medio de una serie de resistencias y capacitores para poderlo trabajar correctamente en la practica. Muchos de los acondicionamientos que se van a listar aqui pueden funcionar para cualquier ESP32, sin embargo cabe resaltar que se realizan para el ESP32-WROOM (para mas informacion puede tomar de guia [esp32wroom](/Datasheets/esp32-wroom-32_datasheet_en.pdf)).

- PIN 2: Este Pin es importante que este en PULL-DOWN cuando el ESP32 se necesite que este en BOOT-MODE, por lo que se conecta una resistencia de 10kOhm para llevarlo a GND.

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>

- PIN 0: Este Pin es de booteo, por lo tanto de acuerdo a lo recopilado de distintos repositorios, se requiere implementar un boton que al ser presionado ponga al PIN 0 en PULL-DOWN.

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>

- PIN EN: Este Pin es el ENABLE, y tiene que estar en PULL-UP todo el tiempo. Sin embargo para cuando sea necesario resetear el ESP32 tiene que estar en PULL-DOWN. Por lo tanto se implementa un boton que realiza la misma funcion que el de Booteo y tiene la siguiente arquitectura.

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>

- PIN 3V3: Se implementa un capacitor ByPass de 100pF para filtrar todo el ruido que pueda afectar la alimentacion del ESP32 (este capacitor se debe procurar que este lo suficientemente cerca de el pin 3V3).

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>


## Programacion 
