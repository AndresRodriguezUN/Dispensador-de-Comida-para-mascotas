# Dispensador de Comida para mascotas 🐱 🐶
## Autores :fountain_pen:
- Diego Steven Peña Cortes :mechanic:
- Daniel Machado Roa :technologist:
- Andrés Felipe Rodríguez Contreras :office_worker:  :shipit:

Este es el repositorio del proyecto final de la asignatura Sistemas Emebidos del semestre 2021-II (Universidad Nacional de Colombia - Sede Bogotá). A continuación se mostrará el proyecto de un Dispensador de Comida conformado por una arquitectura de SoC, donde a partir de un micropocesador y diferentes periféricos se realizan operaciones que permiten al dispensador vincularse con un dispositivo movil para configurar la alimentación de la mascota.
 
 ## Proyecto
 El proyecto consiste en un dispensador de comida para mascotas que dispone de funcionalidades como la comunicacion con una app movil que permite la configuracion del dispositivo y el funcionamiento del mismo. Dentro del funcionamiento se encuentra la programacion de los horarios de alimentacion, asi como la interaccion entre el usuario-dispositivo-mascota.
 
Por otro lado, el dispositivo cuenta con sensores que permiten detectar si la mascota esta comiendo, ademas de los horarios que frecuenta el dispositivo. Y de esta manera, puede realizar un analisis de los datos y retroalimentar al usuario por medio de la actualizacion de los comportamientos de su mascota frente al dispositivo. Permitiendo que no se pierda la conexion que tiene el usuario con su mascota.  
 
 ## [Motivacion](/Motivacion/)
 
 Con el fin de de justificar el proyecto, se definieron los viajes tanto del cliente como de la mascota y del como intervenia nuestro proyecto en cada uno de los trayectos. Esto permitio resaltar las funcionalidades directas o indirectas que debe cumplir el dispositivo a desarrollar. De esta forma se definieron los perifericos necesarios, ademas del modulo-procesador que se van a utilizar.
 
 
 ## Flujo de procesos
 ![Screenshot](/Imagenes/DiaPEmb1.png)
 

 
 ## [Sistema embebido](/SoC/)
 
 El sistema embebido se definio gracias al analisis previo de las funcionalidades directas e indirectas del dispositivo, las cuales permitieron decidir los perifericos necesitados para cumplir cada una de las funcionalidades del proyecto.
 
### Perifericos

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)
 
 ![Screenshot](/Imagenes/SoCEmb.png)
 
  ## Finalidad coordinacion de perifericos :nut_and_bolt:
  
  La idea es construir un dispositvo que a determinadas horas del dia ponga a disposicion una porcion de comida para nuestra mascota. Esta meta se cumple con las prestaciones que nos ofrece cada uno de los componentes a ensamblar:
  
  - Tarjeta basada en ESP32: Encargada de la coordinacion de los perifericos y la comunicacion inalambrica con una App.
  - App: Encargada de la retroalimentacion del usuario sobre el estado de la mascota, ademas de la posibilidad de programar los horarios de comida que el usuario desee para su mascota.
  - Motor: Encargado de la rotacion del plato en el cual estan alojadas cada una de las porciones de comida.
  - OLED: Encargado de dar una retroalimentacion visual, en el dispositivo, de el estado de la mascota.
  - DFP y Parlante: Encargados de reproducir una pista de audio que avise a la mascota cuando llegue la hora de comer.
  - PIR: Encargado de detectar si la mascota se acerca al dispositivo dispensador de comida, para evaluar indirectamente su estado de animo.
  - Infrarrojo: Encargado de detectar si la mascota ha comido alguna parte de su racion, para evaluar indirectamente su estado de animo.
 
Al tener todo coordinado se espera que se cumpla la finalidad del proyecto satisfactoriamente.
  

## [Firmware](/Firmware) :computer:

El firmware de todo el proyecto se desarrolla en micropython, el cual es una version renderizada de python para poder ejecutarse en microcontroladores como lo es el ESP32. Se decidio utilizar micropython debido a su practicidad y la documentacion amplia que tiene en distintos repositorios. Con respecto al ESP32 cabe destacar que se debe flashear con micropython para que todos los codigos en python que se deseen emplear se ejecuten a la perfeccion. Para mas informacion sobre el manejo de micropython junto al ESP32 por favor remitase a [micropython-esp32](https://docs.micropython.org/en/latest/esp32/tutorial/index.html).

## [App](/App) :calling:

## [Diseño Caja](/Rcaja) :triangular_ruler: :package:

## [Ensamble](/Ensamble) :wrench:

## Pruebas de funcionamiento



