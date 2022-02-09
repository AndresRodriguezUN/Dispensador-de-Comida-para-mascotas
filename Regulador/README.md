
# Regulación de tension

El proyecto se utiliza un ESP32-WROOM, este necesita una tension de 3.3V para funcionar y por otro lado se necesitan 5V para poner en funcionamiento un motor paso a paso que se encargara de las prestaciones mecanicas del dispositivo. Por lo tanto se implementan dos reguladores de tension en la tarjeta que se desarrolle.
Con el fin de regular la tensión a 3.3 V y 5 V, se utilizan reguladores NCP1117-3.3 y NCP1117-5 con el empaquetado SOT-223.
<p align="center">
  <img src="/Imagenes/ncp1117.jpg" align="center" width = 450>
</p>

## Diagrama de conexiones

### 5 V - 3.3 V

![Screenshot](/Imagenes/ncp_2.PNG) 


