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
 ![Screenshot](/Imagenes/DiaPEmb.png)
 
 ## [System of Chip - SOC](/SoC/)
 
 El SoC se definio gracias al analisis previo de las funcionalidades directas e indirectas del dispositivo, las cuales permitieron decidir los perifericos necesitados para cumplir cada una de las funcionalidades del proyecto.
 
### Perifericos

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)
 
 ![Screenshot](/Imagenes/SoCEmb.png)


## [App](/App)

## [Diseño Caja](/Rcaja)



