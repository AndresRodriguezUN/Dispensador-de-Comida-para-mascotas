
# Motor
## Componentes
Los componentes que se van a utilizar para este periférico serán:

- Motor unipolar 28BYJ-48
- Driver ULN2003A

<p align="center">
  <img src="/Perifericos/Motor/componentesMotor.png" align="center" width = 850>
</p>

## Estructura y funcionamiento
El funcionamiento del motor paso a paso 28BYJ-48 se basa en la activación de las distintas bobinas que tiene interiormente por medio de señales digitales. Para ajustar magneticamente la posición angular del rotor. Sin embargo esto no se puede realizar simplemente con las salidas digitales del ESP32 ya que no poseen la suficiente corriente para alimentar el motor paso a paso, por lo tanto se implementa el driver ULN2003 que es un arreglo de transistores en configuracion darlington que permiten una salida de corriente de hasta 500mA. PAra mas informacion remitase a nuestro video de youtube [Motor paso a paso - FPGA](https://www.youtube.com/watch?v=wyz6QGYnmfk).

<p align="center">
  <img src="/Perifericos/Motor/estyfuncMotor.png" align="center" width = 850>
</p>

## Diagrama de conexiones
La idea es que las salidas digitales que se obtienen del ESP32 con las que se desea controlar el motor vayan primero al driver ULN2003 para que sea posible controlar el motor con la corriente necesaria. Por lo tanto se sigue el diagrama que está a continuación, para poderlo replicar en la tarjeta que se elaboara en la sección de circuito impreso.

<p align="center">
  <img src="/Perifericos/Motor/conexionesMotor.png" align="center" width = 850>
</p>

## Adecuación
La adecuación que necesita el circuito impreso es tener implementado un driver ULN2003, el cual se seleccionó para este caso de montaje superficial, pero además de eso es necesario utilizar un capacitor de Bypass a la entrada de tensión de 5V del driver para filtrar cualquier ruido que pueda interferir en el diseño. Por lo tanto se define lo siguiente:

<p align="center">
  <img src="/Perifericos/Motor/uln2003.png" align="center" width = 450>
</p>

- 4 pines digitales.
- 1 pin Vcc de 5V exclusivo para el ULN2003.
- 1 pin de GND. 
