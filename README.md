# Dispensador de Comida para mascotas 馃惐 馃惗
## Autores :fountain_pen:
- Diego Steven Pe帽a Cortes :mechanic:
- Daniel Machado Roa :technologist:
- Andr茅s Felipe Rodr铆guez Contreras :office_worker:  :shipit:

Este es el repositorio del proyecto final de la asignatura Sistemas Emebidos del semestre 2021-II (Universidad Nacional de Colombia - Sede Bogot谩). A continuaci贸n se mostrar谩 el proyecto de un Dispensador de Comida conformado por una arquitectura de SoC, donde a partir de un micropocesador y diferentes perif茅ricos se realizan operaciones que permiten al dispensador vincularse con un dispositivo movil para configurar la alimentaci贸n de la mascota.
 
 ## Proyecto :open_file_folder:
 El proyecto consiste en un dispensador de comida para mascotas que dispone de funcionalidades como la comunicaci贸n con una app movil que permite la configuraci贸n del dispositivo y el funcionamiento del mismo. Dentro del funcionamiento se encuentra la programaci贸n de los horarios de alimentaci贸n, asi como la interacci贸n entre el usuario-dispositivo-mascota.
 
Por otro lado, el dispositivo cuenta con sensores que permiten detectar si la mascota est谩 comiendo, adem谩s de los horarios que frecuenta el dispositivo. Y de esta manera, puede realizar un an谩lisis de los datos y retroalimentar al usuario por medio de la actualizaci贸n de los comportamientos de su mascota frente al dispositivo. Permitiendo que no se pierda la conexi贸n que tiene el usuario con su mascota.  
 
 ## [Motivaci贸n](/Motivacion/) :thought_balloon:
 
 Con el fin de de justificar el proyecto, se definieron los viajes tanto del cliente como de la mascota y del como interven铆a nuestro proyecto en cada uno de los trayectos. Esto permitio resaltar las funcionalidades directas o indirectas que debe cumplir el dispositivo a desarrollar. De esta forma se definieron los perif茅ricos necesarios, adem谩s del m贸dulo-procesador que se van a utilizar.
 
 
 ## Flujo de procesos
 ![Screenshot](/Imagenes/DiaPEmb1.png)
 

 
 ## [Sistema embebido](/SoC/)  :computer:
 
 El sistema embebido se definio gracias al an谩lisis previo de las funcionalidades directas e indirectas del dispositivo, las cuales permitieron decidir los perif茅ricos necesitados para cumplir cada una de las funcionalidades del proyecto.
 
### Perif茅ricos

- [Pantalla OLED - I2C](/Perifericos/OLED)

- [Sensor de movimiento](/Perifericos/SensorMov)

- [Sensor infrarrojo](/Perifericos/SensorInfra)

- [Control motor - ULN2003](/Perifericos/Motor)

- [DFPlayer Mini](/Perifericos/DFPlayer)
 
 ![Screenshot](/Imagenes/SoCEmb.png)
 
  ## Finalidad coordinaci贸n de perif茅ricos :nut_and_bolt:
  
  La idea es construir un dispositvo que a determinadas horas del dia ponga a disposici贸n una porcion de comida para nuestra mascota. Esta meta se cumple con las prestaciones que nos ofrece cada uno de los componentes a ensamblar:
  
  - Tarjeta basada en ESP32: Encargada de la coordinaci贸n de los p茅rifericos y la comunicaci贸n inal谩mbrica con una App.
  - App: Encargada de la retroalimentaci贸n del usuario sobre el estado de la mascota, adem谩s de la posibilidad de programar los horarios de comida que el usuario des茅e para su mascota.
  - Motor: Encargado de la rotaci贸n del plato en el cual estan alojadas cada una de las porciones de comida.
  - OLED: Encargado de dar una retroalimentaci贸n visual, en el dispositivo, del estado de la mascota.
  - DFP y Parlante: Encargados de reproducir una pista de audio que avise a la mascota cuando llegue la hora de comer.
  - PIR: Encargado de detectar si la mascota se acerca al dispositivo dispensador de comida, para evaluar indirectamente su estado de 谩nimo.
  - Infrarrojo: Encargado de detectar si la mascota ha comido alguna parte de su raci贸n, para evaluar indirectamente su estado de 谩nimo.
 
Al tener todo coordinado se espera que se cumpla la finalidad del proyecto satisfactoriamente.
  

## [Firmware](/Firmware) :man_technologist:
El firmware de todo el proyecto se desarrolla en micropython, el cual es una version renderizada de python para poder ejecutarse en microcontroladores como lo es el ESP32. Se decidio utilizar micropython debido a su practicidad y la documentaci贸n amplia que tiene en distintos repositorios. Con respecto al ESP32 cabe destacar que se debe flashear con micropython para que todos los c贸digos en python que se deseen emplear se ejecuten a la perfecci贸n. Para m谩s informaci贸n sobre el manejo de micropython junto al ESP32 por favor remitase a [micropython-esp32](https://docs.micropython.org/en/latest/esp32/tutorial/index.html).

## [App](/App) :calling:

Para poder manejar el dispensador de alimentos para mascotas se cre贸 una aplicaci贸n, la cual permita modificar los valores de tiempo en que se servir谩n las comidas y a su vez saber el estado en que se encuentra la mascota.

## [Dise帽o Caja](/Rcaja) :triangular_ruler: :package:

Se dise帽贸 un contenedor (carcasa o caja) la cual permitiera tener el dispensador dentro de una estructura con el fin de almacenar el plato con la comida y el sistema embebido, por lo tanto, se tomaron las diferentes medidas de los perif茅ricos para poder crear los planos en *CorelDraw* y crear la carcasa en madera gracias al proceso de corte l谩ser.

## [Ensamble](/Ensamble) :wrench:

En esta secci贸n se muestra el paso a paso de la uni贸n del sistema embebido y el plato que contiene la comida con la carcasa por medio de im谩genes que dan evidencia de este proceso. 


## Pruebas de funcionamiento y videos de referencia :clapper:

### Videos de referencia
Para encontrar los videos que se recomiendan a lo largo del repositorio por favor dirijase a [videos proyectos pasados](https://www.youtube.com/channel/UCFcKXg10MjH98TOnZhloZSA).
  

### Pruebas de funcionamiento

Se realizaron las siguientes pruebas de funcionamiento del dispositivo y la App.

- [Prueba 1](https://youtu.be/kQyHtM4AsF8).
- [Prueba 2](https://youtu.be/hgBiyUTOZwg).


