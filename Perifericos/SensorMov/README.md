
# Sensor Movimiento

## Componentes
Los componentes que se van a utilizar para este periferico seran:

- Módulo Sensor Infrarrojo Piroeléctrico Mini HC-SR505.

<p align="center">
  <img src="/Perifericos/SensorMov/componentesPIR.png" align="center" width = 250>
</p>

## Estructura y funcionamiento

El sensor PIR es un sensor electrónico que mide la luz infrarroja (IR) radiada de los objetos situados en su campo de visión. Lo que le permite detectar el movimiento y es util para las funcionalidades que se requieren para el dispositivo.

<p align="center">
  <img src="/Perifericos/SensorMov/estyfuncSensorMov.png" align="center" width = 850>
</p>

## Diagrama de conexiones

El sensor PIR tiene una salida digital que indica si ha detectado o no movimiento, por lo tanto es necesario recibirla en el ESP32 para realizar el tratamiento de la informacion.

<p align="center">
  <img src="/Perifericos/SensorMov/conexionesPIR.png" align="center" width = 350>
</p>

## Adecuacion


