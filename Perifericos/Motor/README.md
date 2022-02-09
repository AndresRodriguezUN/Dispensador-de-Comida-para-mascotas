
# Motor
## Componentes
Los componentes que se van a utilizar para este periferico seran:

- Motor unipolar 28BYJ-48
- Driver ULN2003A

<p align="center">
  <img src="/Perifericos/Motor/componentesMotor.png" align="center" width = 850>
</p>

## Estructura y funcionamiento
El funcionamiento del motor paso a paso 28BYJ-48 se basa en la activacion de las distintas bobinas que tiene interiormente por medio de señales digitales. Para ajustar magneticamente la posicion angular del rotor. Sin embargo esto no se puede realizar simplemente con las salidas digitales del ESP32 ya que no poseen la suficiente corriente para alimentar el motor paso a paso, por lo tanto se implementa el driver ULN2003 que es un arreglo de transistores en configuracion darlington que permiten una salida de corriente de hasta 500mA. PAra mas informacion remitase a nuestro video de youtube [Motor paso a paso - FPGA](https://www.youtube.com/watch?v=wyz6QGYnmfk)

<p align="center">
  <img src="/Perifericos/Motor/estyfuncMotor.png" align="center" width = 850>
</p>

## Diagrama de conexiones

<p align="center">
  <img src="/Perifericos/Motor/conexionesMotor.png" align="center" width = 850>
</p>

## Adecuacion
