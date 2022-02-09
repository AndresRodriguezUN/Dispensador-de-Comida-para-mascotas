# Circuito Impreso
El circuito impreso se desarrolla teniendo en cuenta las adecuaciones y acondicionamientos que necesitan tanto el ESP32, los reguladores de tension y los perifericos. Para el desarrollo del esquematico y la PCB se utilizo el software de kiCAD, al cual fue necesario adicionarle las librerias correspondiente al esquematico del ESP32-WROOM y el footprint para la PCB.

## Esquematico - KiCAD
Despues de realizar el analisis de los distintos componentes y de los acondicionamientos necesarios, se realizo el esquematico en KiCAD de todo el proyecto. Incluyendo otras partes necesarias en hardware para la sujecion y conexion del sistema embebido.

### ESP32-WROOM
- Conexiones en general del microcontrolador.
<p align="center">
  <img src="esp32esq.png" align="center" width = 450>
</p>
- Acondicionamiento del ESP32.
-
  

### Motor paso a paso
- Configuracion del ULN2003 y caja negra del driver del motor paso a paso.
<p align="center">
  <img src="/Perifericos/Motor/uln2003.png" align="center" width = 350>
</p>



## PCB - KiCAD
