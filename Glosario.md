#### Glosario

-  **Tag** : Es una etiqueta asignada a una version especifica o a una variante de una imagen de Docker. Las etiquetas son utiles para versionamiento, identificar
      diferentes configuraciones y hacce facil administrar y distribuir imagenes Docker.
- **Imagen Docker**: es una plantilla estática y autocontenida que contiene todo lo necesario para ejecutar una aplicación o un conjunto de servicios dentro de un    contenedor Docker.  
    En términos simples, es una instantánea de un sistema de archivos que incluye el código de una aplicación, sus dependencias y el entorno de tiempo de ejecución
    necesario, todo empaquetado en una única unidad.
- **Aplicacion**: Una aplicación, también conocida como software o programa, es un conjunto de instrucciones y datos que realizan una tarea específica o conjunto de  
  tareas en una computadora u otro dispositivo electrónico y esta destinada a ser utilizada directamente por los usuarios.  
- **Servicio**: es una función o conjunto de funciones que se ejecutan en segundo plano y están destinados a ser utilizados por otras aplicaciones para proporcionar funcionalidades o recursos específicos.
- **Dockerfile**:  Archivo de texto que contienen las instrucciones para construir un ambiente de aplicación conteneirizado. Las imagenes docker se construyen con docker files.  
Cada vez que construyes una imagen usando un dockerfile puedes asignarle una etiqueta.
- **Contenedor**:Los contenedores son una tecnología de virtualización a nivel de sistema operativo, que permite empaquetar una aplicación y sus dependencias en un paquete único, aislado del sistema host y otros contenedores que se estén ejecutando en el mismo sistema.
- **Dependencia**: es un componente externo o una biblioteca que es necesario para que una aplicación funcione correctamente. Estas dependencias pueden ser librerías de código, módulos, paquetes o incluso otras aplicaciones que se utilizan dentro de un proyecto de desarrollo.
- La principal diferencia entre un **entorno virtual** y una **imagen Docker** es que el entorno virtual aísla las dependencias de un proyecto dentro de un directorio 
 separado, mientras que la imagen Docker empaqueta todas las dependencias y configuraciones de una aplicación en una plantilla autocontenida que se puede ejecutar en   cualquier sistema con Docker instalado. Ambas tecnologías son útiles para gestionar dependencias y lograr aislamiento, pero Docker ofrece una mayor portabilidad y una 
 solución más completa para la creación y distribución de aplicaciones.
- **Maquina Virtual**: es un entorno virtual completo que emula un sistema operativo y hardware completo dentro de un sistema operativo anfitrión.
Una máquina virtual permite ejecutar múltiples sistemas operativos simultáneamente en una misma máquina física.
Cada máquina virtual tiene su propio kernel, sistema operativo, aplicaciones y recursos asignados, lo que proporciona un aislamiento casi completo del sistema anfitrión.
- **Entorno virtual**:ofrece un aislamiento más ligero dentro de un mismo sistema operativo para gestionar las dependencias de una aplicación específica y evitar   conflictos entre proyectos
- **Discouraged tag**: Etiqueta desaconsejada por obsolescencia, por antiguedad o porque existe una alternativa mas moderna. Su uso puede no ser optimo.
- **Deprecated tag**: Eqtiqueta en desuso u obsoleta. Elementos obsoletso que seran eliminados en versiones futuras.
- **Alpine**: Alpine Linux es una distribución de Linux diseñada para ser ligera, eficiente y segura, lo que la convierte en una opción popular para la creación de imágenes de contenedores Docker
- Una versión **"slim"** de una imagen Docker se refiere a una versión ligera y minimalista de esa imagen. Estas imágenes están diseñadas para ser lo más pequeñas posible al eliminar componentes y dependencias innecesarias, pero aún proporcionando la funcionalidad necesaria para ejecutar la aplicación o servicio.
- **Uvicorn**: es un servidor web asincrónico de alto rendimiento diseñado específicamente para aplicaciones web basadas en Python.
  Su capacidad de manejar conexiones concurrentes de manera eficiente y su compatibilidad con los protocolos HTTP y WebSockets lo hacen una excelente opción para aplicaciones web modernas y de alto rendimiento en Python.
- **HTTP** es un protocolo de solicitud-respuesta sin estado adecuado para comunicaciones básicas, cada vez que un cliente realiza una solicitud HTTP, el servidor responde con una única respuesta y luego se cierra la conexión. Esta naturaleza "sin estado" hace que HTTP sea adecuado para comunicaciones de una sola vía o de ida y vuelta básicas.
- **WebSocket**: es un protocolo bidireccional y de comunicación en tiempo real que permite una comunicación continua y eficiente entre el cliente y el servidor sin necesidad de establecer nuevas conexiones. WebSocket es más adecuado para aplicaciones que requieren interacciones bidireccionales y en tiempo real, como chats, juegos en línea y aplicaciones colaborativas en tiempo real.
- **Servidor web asíncrono**: es un tipo de servidor que está diseñado para manejar múltiples conexiones concurrentes de manera eficiente y escalable utilizando programación asíncrona.
- **Servidor**: es un equipo o programa que proporciona servicios o recursos a otros dispositivos o programas, permitiendo la comunicación y el acceso a recursos compartidos a través de una red. Existen varos tipos de servidores segun la funcion: servidores web, servidores de correo electronico, servidores de juegos, servidor de bases de datos, servidor de archivos, servidor de impresion, servidor DNS.
- **Gunicorn (Green Unicorn)**: es un servidor web para aplicaciones Python que implementa el protocolo WSGI (Web Server Gateway Interface).
- **WSGI** es una especificación que define cómo un servidor web puede comunicarse con una aplicación Python para servir páginas web de manera eficiente y estándar.
- **API** (Application Programming Interface): es un conjunto de reglas y protocolos que permite que distintos componentes de software se comuniquen y se integren entre sí de manera eficiente. Es una interfaz que define la forma en que un programa puede interactuar con otro para obtener datos, acceder a funcionalidades o solicitar servicios.
- Un ejemplo común de API es la API de Google Maps. Google Maps proporciona una API que permite a los desarrolladores externos integrar y utilizar las funcionalidades de mapas y geolocalización en sus propias aplicaciones y sitios web.
- **FastAPI**: es un infraestructura de trabajo web moderno, rápido (de alto rendimiento) para construir APIs con Python.

  
 
