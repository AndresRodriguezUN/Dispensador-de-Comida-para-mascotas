# Circuito Impreso
El circuito impreso se desarrolla teniendo en cuenta las adecuaciones y acondicionamientos que necesitan tanto el ESP32, los reguladores de tension y los perifericos. Para el desarrollo del esquematico y la PCB se utilizo el software de kiCAD, al cual fue necesario adicionarle las librerias correspondiente al esquematico del ESP32-WROOM y el footprint para la PCB.

## Esquematico - KiCAD
Despues de realizar el analisis de los distintos componentes y de los acondicionamientos necesarios, se realizo el esquematico en KiCAD de todo el proyecto. Incluyendo otras partes necesarias en hardware para la sujecion y conexion del sistema embebido. Igualmente dentro del repositorio se incluye el archivo del esquematico al cual puede remitirse para verificar todo lo diseñado [kiCAD](/kiCAD). 

### ESP32-WROOM
- Conexiones en general del microcontrolador.
<p align="center">
  <img src="esp32esq.png" align="center" width = 450>
</p>

- PIN USER: Este Pin se utiliza para interactuar visualmente con el ESP32 y verificar si funciona correctamente tanto la recepcion, como transmision de datos.

<p align="center">
  <img src="pinuser.png" align="center" width = 200>
</p>

- PIN 2: Este Pin es importante que este en PULL-DOWN cuando el ESP32 se necesite que este en BOOT-MODE, por lo que se conecta una resistencia de 10kOhm para llevarlo a GND.

<p align="center">
  <img src="/SoC/ESP32/io2.png" align="center" width = 200>
</p>

- PIN 0: Este Pin es de booteo, por lo tanto de acuerdo a lo recopilado de distintos repositorios, se requiere implementar un boton que al ser presionado ponga al PIN 0 en PULL-DOWN.

<p align="center">
  <img src="/SoC/ESP32/boot.png" align="center" width = 300>
</p>

- PIN EN: Este Pin es el ENABLE, y tiene que estar en PULL-UP todo el tiempo. Sin embargo para cuando sea necesario resetear el ESP32 tiene que estar en PULL-DOWN. Por lo tanto se implementa un boton que realiza la misma funcion que el de Booteo y tiene la siguiente arquitectura.

<p align="center">
  <img src="/SoC/ESP32/enable.png" align="center" width = 300>
</p>

- PIN 3V3: Se implementa un capacitor ByPass de 100pF para filtrar todo el ruido que pueda afectar la alimentacion del ESP32 (este capacitor se debe procurar que este lo suficientemente cerca de el pin 3V3).

<p align="center">
  <img src="/SoC/ESP32/bypass.png" align="center" width = 200>
</p>
  

### Motor paso a paso
- Configuracion del ULN2003 y caja negra del driver del motor paso a paso.
<p align="center">
  <img src="/Perifericos/Motor/uln2003.png" align="center" width = 350>
</p>
<p align="center">
  <img src="cajanegraULN.png" align="center" width = 350>
</p>

### Regulacion y conexion Jack-DC

- Acondicionamiento de reguladores

<p align="center">
  <img src="/Regulador/ncp5.png" align="center" width = 350>
</p>
<p align="center">
  <img src="/Regulador/ncp3.png" align="center" width = 350>
</p>

- Conexion Jack-DC para cargador de 12V, en donde se deja una salida para conectar un interruptor que permita apagar y prender el dispositivo.

<p align="center">
  <img src="jackDC.png" align="center" width = 350>
</p>

### Conectores para los perifericos en general
Se utilizaron conectores de diferente cantidad de pines para poder ajustar los pines para cada uno de los perifericos.

<p align="center">
  <img src="perifGene.png" align="center" width = 550>
</p>

## Asignación de Footprints
Antes de continuar con la generacion de la PCB y la NetList, se asignan las footprint para cada uno de los elementos que se implementaron en el montaje del circuito impreso. En este paso se debe tener en cuenta los componentes que se van a comprar y las dimensiones, para que de esta forma se puedan realizar una correcta seleccion de cada uno de los footprints asociados (y que no vayan a haber problemas a futuro por una mal encuadre de dimensiones).

<p align="center">
  <img src="footasign.png" align="center" width = 850>
</p>

## PCB - KiCAD

Despues de realizar el diseño en kiCAD del esquematico, se procede a generar la PCB junto con las footprints asociadas previamente. En donde se cuadra la ubicacion de todos los componentes en el circuito impreso teniendo en cuenta una distribucion por potencia (separando por secciones imaginarias los componentes de mayor a menor potencia), asi como las recomendaciones de dimensiones minimas que podia implementar el fabricante. Del mismo modo se incluyen otras partes necesarias en hardware para la sujecion del sistema embebido. Igualmente dentro del repositorio se incluye el archivo de la PCB al cual puede remitirse para verificar todo lo diseñado [kiCAD](/kiCAD). 

<p align="center">
  <img src="PcbKi.png" align="center" width = 650>
</p>

Como se puede observar, se adicionaron o ajustaron ciertas cosas adicionales en la PCB como lo son:

- Orificios de sujecion, por lo cuales seria ideal ajustar la placa en el dispositivo.
- Segun la guia de diseño, es importante que para el correcto funcionamiento de la antena de el ESP32, se debe despejar el area de cualquier pista de cobre que pase por la seccion de la antena.
<p align="center">
  <img src="antenaEsp.png" align="center" width = 450>
</p>

- Se implementaron **vias** en las zonas donde no habian componentes, para reducir la capacitancia entre las caras asignadas a tierra del circuito impreso. 

## Pedido - fabricante CHINO

El pedido se realizo a un fabricante chino, especificamente a [JLCPCB](https://jlcpcb.com/), y el proceso que se realizo en resumidas cuentas es el siguiente:

- Subir el archivo del proyecto, no sin antes generar los archivos gerber y de perforacion del proyecto. Y en la pagina del fabricante se detallan las caracteristicas que el usuario prefiera para la fabricacion de su PCB.

<p align="center">
  <img src="orden1.png" align="center" width = 850>
</p>

- Posteriormente que se llene la informacion de las caracteristicas de la placa, se procede al carrito de compras y se verifica el precio estimado por la fabricacion de la cantidad que se halla exigido (la minima cantidad que se fabrica son 5 placas por $2 Dolares).

<p align="center">
  <img src="orden2.png" align="center" width = 850>
</p>

- Luego se procede con el diligenciamiento de la informacion respectiva a la residencia y de facturacion, para continuar con el metodo de envio. **El metodo de envio que recomendamos y que nos funciono a nosotros es el Standard Special Air Mail**. Ya que es el unico que hace envios a Colombia, por un precio razonable en un plazo de alrededor de 20 dias.

<p align="center">
  <img src="orden3.png" align="center" width = 850>
</p>

- Y luego de 20 dias asi llego la PCB.

<p align="center">
  <img src="pcbllego.jpeg" align="center" width = 750>
</p>

