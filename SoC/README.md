# Sistema embebido :computer:


## [Microcontrolador ESP32](/SoC/ESP32/)
Se implementó un microcontrolador ESP32-WROOM, el cual se encargara de coordinar los diferentes periféricos a implementar. Igualmente, gracias a su periférico de WiFi se podrán utilizar las comunicaciones inalámbricas en lo que respecta a la conexión con la App de control.

- [Adecuación y acondicionamiento](/SoC/ESP32#adecuaci%C3%B3n)
- [Programación](/SoC/ESP32#programacion)

## Periféricos

En base al sistema embebido definido previamente, se llegó a la conclusión que los periféricos necesarios para cumplir con las funcionalidades directas del dispositivo son:

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)

## [Regulación de tensión](/Regulador)

Dado que en proyecto se utiliza un ESP32-WROOM, este necesita una tensión de 3.3V para funcionar y por otro lado se necesitan 5V para poner en funcionamiento un motor paso a paso que se encargara de las prestaciones mecanicas del dispositivo. Por lo tanto se implementan dos reguladores de tension en la tarjeta que se desarrolle.


## [Circuito Impreso](/SoC/CircuitoImpreso)

Para el proyecto se decidio implementar un circuito impreso, el cual debera contar con el microcontrolador y los diferentes acondicionamientos necesarios para el manejo y control de los distintos periféricos a emplear.

- [Esquematico](/SoC/CircuitoImpreso#esquematico---kicad)
- [Asignacion de Footprints](/SoC/CircuitoImpreso#asignacion-de-footprints)
- [PCB](/SoC/CircuitoImpreso#pcb---kicad)
- [Pedido](/SoC/CircuitoImpreso#pedido---fabricante-chino)

## [Soldadura y Resultado](/SoC/Soldadura)

Con el circuito impreso entregado por el fabricante, se procede a realizar la soldadura de cada uno de los componentes comprados para el dispositivo dispensador de comida para mascotas.
