
# OLED
## Componentes
Para el proyecto se usara un OLed de referencia **OLED-128O064D-BPP3N00000**.

<p align="center">
  <img src="/Imagenes/Elooled.png" align="center" width = 250>
</p>

## Estructura y funcionamiento 
La pantalla Oled funciona a partir de una alimentación de 3V (maximo 3.3V y minimo 2.8V) a su vez se logra trabajar con este componente gracias a la comunicación I2C, de esta manera como se logra ver en el siguiente apartado, el Oled posée dos pines para la comunicación que son SCL y SDA los cuales nos permiten la comunicación y trabajan de la siguiente forma (despues se describe con más detalle).
## Diagrama de conexiones
Por último, dado que se usara la comunicación I2C solo sera necesario usar 4 pines para la conexión del componente, VCC siendo la alimentación de 3V, GND el ground, SDL y SDA.

<p align="center">
  <img src="/Imagenes/ElOled.png" align="center" width = 350>
</p>

## Adecuación

La comunicación con el OLED es por medio de i2c, y el periférico de i2c ya viene acondicionado en el SoC que el fabricante ofrece para el ESP32. Por lo tanto, lo unico que se necesita es prestar para el OLED 4 pines:
- 2 pines de i2c
- 1 pin de Vcc a 3V3
- 1 pin de GND
