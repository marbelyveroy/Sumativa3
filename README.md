
# Query Builder Python
Generador de consultas: MySQL/MariaDB

## Dependencias
* pip install pymysql
* pip3 install pymysql


## Base de datos - Ejemplo
Base de datos: **db**

Tabla: **usuario**

| Type | Name |
| ------ | ----------- |
|integer|id|
|varchar(50)|nombre|
|integer|edad|
|varchar(100)|direccion|



## Ejemplo de conexión 
* Importar la clase **Base_datos**
	*  ```from base_datos import * ```

* Crear una instancia de la clase: 
	* ```base_datos= Base_datos();```

* Establecer las credenciales para conectarse a la base de datos: 
	* ```base_datos.setCredenciales("HOST", "USUARIO_BD", "PASSWORD_BD", "NOMBRE_BD")```

### SELECT 
El método select recibe dos parámetros: 
* **table** (str): nombre de la tabla a la que se le quiere hacer la consulta
* **where** (list) [**OPCIONAL**]: lista con los filtros que tendrá la consulta, tomando en cuenta que cada elemento de la lista, debe tener el siguiente formato:
	*  ```{"campo":"", "condicion":"", "valor":""}```
	* condición puede aceptar: 
		* ```=```
		* ```>=```
		* ```<=```
		* ```<>```
* Ejemplo: extraer todos los registros de la tabla **usuario**
	* Similar a: ```SELECT * FROM usuario```
```python
		select=base_datos.select("usuario");
		print(select);
```
* Ejemplo: consulta a la tabla **usuario** con la condición que id=1
	* Similar a: ```SELECT * FROM usuario WHERE id=1```

```python
		select=base_datos.select("usuario", [
			{"campo":"id", "condicion":"=", "valor":"1"}
		]);
		print(select);
```

* Ejemplo: consulta a la tabla **usuario** con la condición de que edad >=50 y que id < 100
	* Similar a: ```SELECT * FROM usuario WHERE edad>=50 AND id<100```

```python
		select=base_datos.select("usuario", [
			{"campo":"edad", "condicion":">=", "valor":"50"},
			{"campo":"id", "condicion":"<", "valor":"100"}
		]);
		print(select);
```

### INSERT
El método insert recibe 3 parámetros:
* **tabla** (str): nombre de la tabla a la que se le quiere hacer el insert
* **campos** (list): lista con el nombre de los campos que se tomarán en cuenta en el insert
* **valores** (list): lista con los valores de los campos que se tomarán en cuenta en el insert
* Ejemplo de insert: 
	* Similar a: ```INSERT INTO usuario('nombre', 'edad', 'direccion') VALUES(''José Perez', 70, 'Monterrey, México')```
```python
	base_datos.insert("usuario", ["nombre", "edad", "direccion"],["'José Perez'","70","'Monterrey, México'"]);
```

### UPDATE
El método update recibe 3 parámetros: 
* **tabla** (str): nombre de la tabla a la que se le quiere hacer el UPDATE
* **edicion** (list): lista con el nombre de los campos que se tomarán en cuenta en el insert
* **valores** (list): lista con el nombre de los valores de los campos que se tomarán en cuenta en el insert
* Ejemplo de update: 
	* Similar a: ```UPDATE usuario SET nombre='fake' WHERE id=1```
```python
	base_datos.update("usuario", {"nombre":"'fake'"}, {"id":"1"});
```

### DELETE
El método delete recibe 2 parámetros: 
* **tabla** (str): nombre de la tabla a la que se le quiere hacer el DELETE
* **where** (dict): Diccionario con las claves valor de los campos y su contenido que se utilizará como filtro para eliminar registros
* Ejemplo delete:
	* Similar a: ```DELETE FROM usuario WHERE id=1```
```python
	base_datos.delete("usuario", {"id":"1"});
```
## Version v1.0.0

## Autor
* [G. Mizael Mtz Hdz](https://www.google.com/search?q=G.+Mizael+Mtz+Hdz)
