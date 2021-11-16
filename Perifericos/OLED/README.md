
# OLED
## Componentes
Para el proyecto se usara un OLed de referencia **OLED-128O064D-BPP3N00000**.

![Screenshot](/Imagenes/Elooled.png)

## Estructura y funcionamiento 
La pantalla Oled funciona a partir de una alimentación de 3V (maximo 3.3V y minimo 2.8V) a su vez se logra trabajar con este componente gracias a la comunicación I2C, de esta manera como se logra ver en el siguinte apartado, el Oled posee dos pines para la comunicación que son SCL y SDA los cuales nos permiten la comunicación y trabajan de la siguiente forma (despues decribo esto mas a detalle)
## Diagrama de conexiones
Por ultimo, dado que se usara la comunicación I2C solo sera necesario usar 4 pines para la concexion del componente, VCC siendo la alimentación de 3V, GND el ground, SDL y SDA.

![Screenshot](/Imagenes/ElOled.png)
