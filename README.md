# Dispensador de Comida para mascotas 🐱 🐶
## Autores :fountain_pen:
- Diego Steven Peña Cortes :mechanic:
- Daniel Machado Roa :technologist:
- Andrés Felipe Rodríguez Contreras :office_worker:  :shipit:

Este es el repositorio del proyecto final de la asignatura Sistemas Emebidos del semestre 2021-II (Universidad Nacional de Colombia - Sede Bogotá). A continuación se mostrará el proyecto de un Dispensador de Comida conformado por una arquitectura de SoC, donde a partir de un micropocesador y diferentes periféricos se realizan operaciones que permiten al dispensador vincularse con un dispositivo movil para configurar la alimentación de la mascota.
 
 ## Proyecto :open_file_folder:
 El proyecto consiste en un dispensador de comida para mascotas que dispone de funcionalidades como la comunicación con una app movil que permite la configuración del dispositivo y el funcionamiento del mismo. Dentro del funcionamiento se encuentra la programación de los horarios de alimentación, asi como la interacción entre el usuario-dispositivo-mascota.
 
Por otro lado, el dispositivo cuenta con sensores que permiten detectar si la mascota está comiendo, además de los horarios que frecuenta el dispositivo. Y de esta manera, puede realizar un análisis de los datos y retroalimentar al usuario por medio de la actualización de los comportamientos de su mascota frente al dispositivo. Permitiendo que no se pierda la conexión que tiene el usuario con su mascota.  
 
 ## [Motivacion](/Motivacion/) :thought_balloon:
 
 Con el fin de de justificar el proyecto, se definieron los viajes tanto del cliente como de la mascota y del como intervenía nuestro proyecto en cada uno de los trayectos. Esto permitio resaltar las funcionalidades directas o indirectas que debe cumplir el dispositivo a desarrollar. De esta forma se definieron los periféricos necesarios, además del módulo-procesador que se van a utilizar.
 
 
 ## Flujo de procesos
 ![Screenshot](/Imagenes/DiaPEmb1.png)
 

 
 ## [Sistema embebido](/SoC/)  :computer:
 
 El sistema embebido se definio gracias al análisis previo de las funcionalidades directas e indirectas del dispositivo, las cuales permitieron decidir los periféricos necesitados para cumplir cada una de las funcionalidades del proyecto.
 
### Perifericos

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)
 
 ![Screenshot](/Imagenes/SoCEmb.png)
 
  ## Finalidad coordinacion de perifericos :nut_and_bolt:
  
  La idea es construir un dispositvo que a determinadas horas del dia ponga a disposición una porcion de comida para nuestra mascota. Esta meta se cumple con las prestaciones que nos ofrece cada uno de los componentes a ensamblar:
  
  - Tarjeta basada en ESP32: Encargada de la coordinación de los périfericos y la comunicación inalámbrica con una App.
  - App: Encargada de la retroalimentación del usuario sobre el estado de la mascota, además de la posibilidad de programar los horarios de comida que el usuario desée para su mascota.
  - Motor: Encargado de la rotación del plato en el cual estan alojadas cada una de las porciones de comida.
  - OLED: Encargado de dar una retroalimentación visual, en el dispositivo, del estado de la mascota.
  - DFP y Parlante: Encargados de reproducir una pista de audio que avise a la mascota cuando llegue la hora de comer.
  - PIR: Encargado de detectar si la mascota se acerca al dispositivo dispensador de comida, para evaluar indirectamente su estado de ánimo.
  - Infrarrojo: Encargado de detectar si la mascota ha comido alguna parte de su ración, para evaluar indirectamente su estado de ánimo.
 
Al tener todo coordinado se espera que se cumpla la finalidad del proyecto satisfactoriamente.
  

## [Firmware](/Firmware) :man_technologist:
El firmware de todo el proyecto se desarrolla en micropython, el cual es una version renderizada de python para poder ejecutarse en microcontroladores como lo es el ESP32. Se decidio utilizar micropython debido a su practicidad y la documentación amplia que tiene en distintos repositorios. Con respecto al ESP32 cabe destacar que se debe flashear con micropython para que todos los códigos en python que se deseen emplear se ejecuten a la perfección. Para más información sobre el manejo de micropython junto al ESP32 por favor remitase a [micropython-esp32](https://docs.micropython.org/en/latest/esp32/tutorial/index.html).

## [App](/App) :calling:

Para poder manejar el dispensador de alimentos para mascotas se creó una aplicación, la cual permita modificar los valores de tiempo en que se servirán las comidas y a su vez saber el estado en que se encuentra la mascota.

## [Diseño Caja](/Rcaja) :triangular_ruler: :package:

Se diseñó un contenedor (carcasa o caja) la cual permitiera tener el dispensador dentro de una estructura con el fin de almacenar el plato con la comida y el sistema embebido, por lo tanto, se tomaron las diferentes medidas de los periféricos para poder crear los planos en *CorelDraw* y crear la carcasa en madera gracias al proceso de corte láser.

## [Ensamble](/Ensamble) :wrench:

En esta sección se muestra el paso a paso de la unión del sistema embebido y el plato que contiene la comida con la carcasa por medio de imágenes que dan evidencia de este proceso. 


## Pruebas de funcionamiento


