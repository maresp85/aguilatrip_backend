**1. DESCRIPCIÓN**

Proyecto desarrollado con Django Framework, el cual permite a través de Servicios Web; Crear, listar, Actualizar y realizar distintas operaciones para la gestión de viajes.
Se estructuró una base de datos con diferentes modelos que permiten tener una aplicación escalable, por ejemplo para manejar registro de usuarios, ciudades, códigos de estado,
países, entre otros.
  
**2. VERSIONAMIENTO**

* django v. 2.2.11
* django rest framework v. 3.11.0
* psycopg2 v. 2.8.4
* postgresql v. 11

**3. CONFIGURACIÓN - DESPLIEGUE LOCAL**

Clonar el proyecto, tener en cuenta la configuración para la conexión a la base de datos, efectuar la migración con el comando: *python manage.py migrate*.
Arrancar el proyecto: *python manage.py runserver* 

**4. MODELOS**
1. Country
2. City
3. Car
4. Status_trip
5. Check_code
6. Trip
7. Start_trip
8. Stop_trip
9. Driver_location
10. User
11. UserType
12. UserProfile
 

Tener en cuenta los siguientes datos para los modelos (estos datos se pueden ingresar a través del aplicativo admin de Django):

STATUS_TRIP:
1- OnWay. 2- Near, 3- Started, 4- End

USER_TYPE:
1- Driver, 2- Passenger
   
CITY:
1- Bogotá, 2- Medellín, 3-Cali...

COUNTRY:
1- Colombia

**5. URIs**

* GET  -> localhost:8000/trips/ (listar todos los viajes - con paginación)
* POST -> localhost:8000/trips/ (crear un viaje)
* PUT  -> localhost:8000/trips/{param}/ (Actualizar un viaje)
* GET  -> localhost:8000/trips/count/ (consultar el total de viajes)
* GET  -> localhost:8000/trips/countcity/{param}/ (Consultar el total de viajes por ciudad)
* POST -> localhost:8000/trips/driver_location/ (Crear o actualizar la ubicación del conductor)
* PUT  -> localhost:8000/trips/end/{param}/ (Finalizar un viaje)

   
**6. TESTING**

Se efectuaron pruebas con el aplicativo POSTMAN de cada una de las URI con sus correspondientes métodos.
