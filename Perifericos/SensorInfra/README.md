
# Sensor infrarrojo

## Componentes

Los componentes que se van a utilizar para este periferico seran:

- Módulo Sensor Infrarrojo FC-51.

<p align="center">
  <img src="/Perifericos/SensorInfra/componentesIR.png" align="center" width = 250>
</p>

## Estructura y funcionamiento

El sensor infrarrojo es un dispositivo optoelectrónico capaz de medir la radiación electromagnética infrarroja de los cuerpos en su campo de visión. Todos los cuerpos emiten una cierta cantidad de radiación, esta resulta invisible para nuestros ojos pero no para estos aparatos electrónicos, ya que se encuentran en el rango del espectro justo por debajo de la luz visible. 

<p align="center">
  <img src="/Perifericos/SensorInfra/estyfunc1IR.png" align="center" width = 450>
</p>

## Diagrama de conexiones
El sensor infrarrojo se puede utilizar como un medidor de distancia o un detector de obstaculos, por lo que presta dos salidas, una salida analógica y otra digital. Para el fin de nuestro proyecto se utilziara la salida digital para detectar si hay comida o no en el recipiente. De modo que solo se utilizara el pin digital y el analógico se dejará sin conexión alguna.

<p align="center">
  <img src="/Perifericos/SensorInfra/conexionesIR.jpeg" align="center" width = 350>
</p>

## Adecuación

La comunicación con el infrarrojo es por medio de un pin digital. Por lo tanto lo unico que se necesita es prestar para el infrarrojo 3 pines:

- 1 pin digital de recepcion de datos.
- 1 pin de Vcc de 3V3.
- 1 pin de GND.
