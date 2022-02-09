# Sistema embebido


## [Microcontrolador ESP32](/SoC/ESP32/)
Se implemento un microcontrolador ESP32-WROOM, el cual se encargara de coordinar los diferentes perifericos a implementar. Igualmente, gracias a su periferico de WiFi se podran utilizar las comunicaciones inalambricas en lo que respecta a la conexion con la App de control.

- [Adecuacion y acondicionamiento](/SoC/ESP32)
- [Programacion](/SoC/ESP32)

## Perifericos

En base al sistema embebido definido previamente se llego a la conclusion que los perifericos necesarios para cumplir con las funcionalidades directas del dispositivo son:

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)

## [Regulacion de tension](/Regulador)

Dado que en proyecto se utiliza un ESP32-WROOM, este necesita una tension de 3.3V para funcionar y por otro lado se necesitan 5V para poner en funcionamiento un motor paso a paso que se encargara de las prestaciones mecanicas del dispositivo. Por lo tanto se implementan dos reguladores de tension en la tarjeta que se desarrolle.


## [Circuito Impreso](/SoC/CircuitoImpreso)

Para el proyecto se decidio implementar un circuito impreso, el cual debera contar con el microcontrolador y los diferentes acondicionamiento necesarios para el manejo y control de los distintos perifericos a emplear.

- [Esquematico](/SoC/CircuitoImpreso)
- [Asignacion de Footprints](/SoC/CircuitoImpreso)
- [PCB](/SoC/CircuitoImpreso)
- [Pedido](/SoC/CircuitoImpreso)

## [Soldadura y Resultado](/SoC/Soldadura)

Con el circuito impreso entregado por el fabricante, se procede a realizar la soldadura de cada uno de los componentes comprados para el dispositivo dispensador de comida para mascotas.
