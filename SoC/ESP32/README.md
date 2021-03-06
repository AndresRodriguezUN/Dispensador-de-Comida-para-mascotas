# Microcontrolador ESP32-WROOM

El microcontrolador ESP32 es un SoC basado en un procesador Xtensa LX6, el cual gracias a su hardware presta la funcionalidad de comunicacion inalámbrica gracias a su módulo de WiFi y Bluetooth. Por lo tanto se decidio utilizar especificamente la version ESP32-WROOM del mismo ya que se acomodaba justamente a las necesidades de hardware que se requerian para el funcionamiento del dispositivo dispensador de comida para mascotas.

<p align="center">
  <img src="esp32wroom.jpg" align="center" width = 250>
</p>

El ESP32-WROOM32 cuenta con 38 pines de los cuales se emplearan UART's, pines digitales y analogicos. Para mas informacion sobre la descripcion de los pines remitirse a [esp32wroom](/Datasheets/esp32-wroom-32_datasheet_en.pdf).

## Adecuación

Si bien el SoC del ESP32-WROOM viene con la adecuación de sus periféricos internos y los módulos que implementa para funcionar. Es necesario realizar la adecuación de este por medio de una serie de resistencias y capacitores para poderlo trabajar correctamente en la práctica. Muchos de los acondicionamientos que se van a listar aqui pueden funcionar para cualquier ESP32, sin embargo cabe resaltar que se realizan para el ESP32-WROOM (para más información puede tomar de guía [esp32wroom](/Datasheets/esp32-wroom-32_datasheet_en.pdf)).

- PIN 2: Este Pin es importante que este en PULL-DOWN cuando el ESP32 se necesite que este en BOOT-MODE, por lo que se conecta una resistencia de 10kOhm para llevarlo a GND.

<p align="center">
  <img src="io2.png" align="center" width = 200>
</p>

- PIN 0: Este Pin es de booteo, por lo tanto de acuerdo a lo recopilado de distintos repositorios, se requiere implementar un botón que al ser presionado ponga al PIN 0 en PULL-DOWN.

<p align="center">
  <img src="boot.png" align="center" width = 300>
</p>

- PIN EN: Este Pin es el ENABLE, y tiene que estar en PULL-UP todo el tiempo. Sin embargo para cuando sea necesario resetear el ESP32 tiene que estar en PULL-DOWN. Por lo tanto se implementa un botón que realiza la misma función que el de Booteo y tiene la siguiente arquitectura.

<p align="center">
  <img src="enable.png" align="center" width = 300>
</p>

- PIN 3V3: Se implementa un capacitor ByPass de 100pF para filtrar todo el ruido que pueda afectar la alimentación del ESP32 (este capacitor se debe procurar que esté lo suficientemente cerca de el pin 3V3).

<p align="center">
  <img src="bypass.png" align="center" width = 200>
</p>


## Programación

La programación del ESP32 se realizara por medio de el periférico UART0 que ya presta el SoC. Sin embargo es necesario utilziar un conversor USB-UART para poder cumplir con el fin de comunicación entre el PC y el ESP32. 

<p align="center">
  <img src="usbserial.png" align="center" width = 300>
</p>

Y para el manejo del Firmware que se utilizara para coordinar los diferentes periféricos y el ESP32 se decidio utilizar MicroPython debido a su simplicidad y la amplia gama de información que se puede encontrar en repositorios para alguna funcionalidad en especifico que esa necesaria utilizar. Para más información remitase a [Firmware](/Firmware). 

<p align="center">
  <img src="strappingPins.png" align="center" width = 500>
</p>

Según lo que indica el datasheet, la coordinación de los pines IO0 y EN para ponerlo en BOOT-MODE debe ser la siguiente, a partir de la distribución de botones que se utilizó:
- Se deben presionar los dos botones BO y EN a la vez y se deben mantener presionados.
- Luego hay que dejar de presionar el EN, y mantener presionado el BO.
- Cuando se verifique que el firmware se este subiendo, o que se ha generado una buena conexion entre el PC y el ESP32 se puede dejar de presionar el BO.


