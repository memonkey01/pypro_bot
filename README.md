<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/">
    <img src="https://www.pypro.mx/static/material/img/logo_45px.png" alt="Logo" height="45px">
  </a>

  <h3 align="center">PyPro Bot</h3>

  <p align="center">
    Un framework de trabajo y ejecución para Trading Algorítmico.
    <br />
    <a href=""><strong>Documentación »</strong></a>
    <br />
    <br />
    <a href="https://www.pypro.mx/premium/curso-trading-algoritmico">Ver Curso</a>
    ·
    <a href="">Reportar Bug</a>
    ·
    <a href="">Solicitar Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Tabla de Contenidos</h2></summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="#software-y-ambientes">Software y Ambientes</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Instalación Local</a>
      <ul>
        <li><a href="#requisitos">Requisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#pasos-iniciales">Pasos Iniciales</a></li>
    <li><a href="#contribuir">Contribuir</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#agradecimientos">Agradecimientos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del Proyecto

PyPro Bot es un framework de trabajo y ejecución para estrategias de trading algoritmico. 

En la parte principal del motor de ejecución se usa Apache Airflow para orquestar las funciones que representan estrategias de trading. Dichas estrategias de trading siguen una serie de pasos tales como: extracción de datos, generación de señales, validación de señales, reglas de posición, ejecución de ordenes en exchange, registro de datos.

Estructura dentro del folder dags (que es el directorio raíz):

-- api
-- settings
-- strategies
-- trading_bot


[![Product Name Screen Shot][product-screenshot]](https://pypro.mx/)


### Software y Ambientes

* Docker []()
* MySQL []()
* Python 3.7[]()
* Apache Airflow []()



<!-- GETTING STARTED -->
## Instalación Local

Para instalar el proyecto solo hay que seguir los siguientes pasos.

### Requisitos

Necesitaras tener los siguientes softwares instalados
* Git: https://git-scm.com/downloads
* Docker: https://docs.docker.com/docker-for-windows/install/
* VsCode: https://code.visualstudio.com/download
* DBBeaver: https://dbeaver.io/download/
* OR Other DB Explorer
* MySQL Workbench: https://dev.mysql.com/downloads/workbench/
* Anaconda: https://www.anaconda.com/products/individual

Ya que tengas instalados todos los requerimientos necesarios puedes seguir los siguientes pasos para ejecutar el Framework de Trabajo.


##### Exchanges

Por el momento se encuentra código y librerias para el exchange de ByBit

* Bybit: https://rb.gy/ovjvny

### Instalación

1. Clona el repositorio
   ```sh
   git clone https://github.com/memonkey01/trading_bot_pypro
   ```
2. Ejecuta Docker-Compose
   ```sh
   docker-compose up
   ```
3. Ve a http://localhost:8080 para visualizar el administrador de tareas (Apache Airflow)


<!-- USAGE EXAMPLES -->
## Pasos Iniciales

Una vez descargado usar docker-compose para levantar el ambiente de desarrollo.

   ```sh
    docker-compose up

    docker-compose down

   ```
   
Despues podremos modificar el archivo config.py con nuestras variables iniciales (Api Keys y Montos)

Finalmente dentro de la interfaz podemos activar nuestros DAGs que representan la ejecución de nuestra estrategia.

Para modificar las estrategias solamente tienes que agregar tus estrategias en las carpetas adecuadas de la estructura de trabajo, seguido tendrás que crear el archivo de ejecución siguiendo los pasos recomendados (extracción de datos, generación de señales, validación de señales, reglas de posición, ejecución de ordenes en exchange, registro de datos).

Como paso final para agregar tu estrategia deberás crear un archivo llamado dag_nombre_estrategia, para que este pueda ser leido por Apache Airflow.

<!-- CONTRIBUTING -->
## Contribuir

Para contribuir en el proyecto debes de realizar los siguientes pasos para que tu request  **sea propiamente manejado**.

1. Haz un Fork del proyecto
2. Crea una Branch con tu Feature(`git checkout -b feature/AmazingFeature`)
3. Haz Commit a tus cambios(`git commit -m 'Add some AmazingFeature'`)
4. Haz Push al Branch correspondiente (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request


<!-- CONTACT -->
## Contacto

Guillermo Izquierdo - [@cryptomonkey01](https://twitter.com/cryptomonkey01) - info@pypro.mx

Project Link: [https://github.com/memonkey01/trading_bot_pypro](https://github.com/memonkey01/trading_bot_pypro)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username

## Agradecimientos

Un agradecimiento a todos los miembros de PyPro que con su membresia han apoyado la creación de este contenido y a todos los miembros de Youtube.

También un enorme agradecimiento a Puckel por su imagen de Apache Airflow que ha servido como base para la estructura de este repositorio.

