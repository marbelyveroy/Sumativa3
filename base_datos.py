# -*- coding: utf-8 -*-
import pymysql
class Base_datos:
    """ 
        @name Base_Datos
        @description clase Modelo para realizar conexiones a bases de datos: MySQL/MariaDB
        @author G. Mizael Mtz Hdz
        @link http://witsoftplus.com/
    """	
	def __init__(self):
		""" Constructor para iniciar la clase de Base_datos
		Returns: void
		"""	
		self.__host="";
		self.__usuario="";
		self.__password="";
		self.__bd="";
		self.__conector=None
	def setCredenciales(self, host, usuario, password, bd):
		""" Método para establecer las credenciales para conectarse al servidor de base de datos
		    Parameters:
			    host (str): nombre del host (servidor)
			    usuario (str): nombre del usuario
			    password (str): password del usuario del host (servidor)
			    bd (str): nombre de la base de datos a la cual se quiere realizar la conexión
		    Returns: void
		"""
		self.__host=host;
		self.__usuario=usuario;
		self.__password=password;
		self.__bd=bd;
	def __conectar(self):
		""" Método privado para conectarse con el servidor y establecer la variable self.__connect con la conexión activa
		    Returns: void
		"""
		if self.__conector is None: 
			try:
				self.__conector = pymysql.connect(
					host=self.__host,
					user=self.__usuario,
					password=self.__password,
					db=self.__bd)
				self.__conector.autocommit(True)
			except ():
				self.__conector=None
	def select(self, tabla, where=None):
		""" Método para realizar una consulta a la base de datos
		    Parameters:
			    tabla (str): nombre de la tabla a la que se le quiere hacer la consulta
			    where (list): lista con los filtros que tendrá la consulta, tomando en cuenta que cada elemento de la lista, debe tener el siguiente formato: 
					{
						"campo",
						"condicion",
						"valor"
					}
		    Returns: resultado(list | None): resultado de realizar la consulta a la tabla proporcionada y a los filtros proporcionados
		"""
		resultado=None
		try:
			self.__conectar();
			try:
				str_where="";
				if(where is not None):
					for fila in where:
						str_where=str_where+fila["campo"]+fila["condicion"]+fila["valor"]+" AND "
					str_where=str_where[:-4]
				with self.__conector.cursor() as cursor:
					query="SELECT * FROM %s"%(tabla);
					if(str_where!=""):
						query=query+" WHERE %s"%(str_where);
					print(query)
					cursor.execute(query)
					resultado = cursor.fetchall()
			except Exception as e:
				print(e)
			finally:
				pass#self.__conector.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return resultado
	def insert(self, tabla, campos, valores):
		""" Método para realizar un insert a la tabla proporcionada en la base de datos
		    Parameters:
			    tabla (str): nombre de la tabla a la que se le quiere hacer el insert
			    campos (list): lista con str, con el nombre de los campos que se tomarán en cuenta en el insert
			    valores (list): lista con str, con el nombre de los valores de los campos que se tomarán en cuenta en el insert
		    
		    Returns: resultado(list | None): resultado de realizar la consulta a la tabla proporcionada y a los filtros proporcionados
		"""
		try:
			self.__conectar();
			with self.__conector.cursor() as cursor:
				str_campos=", ".join(campos);
				str_valores=", ".join(valores);
				consulta = "INSERT INTO %s(%s) VALUES (%s)"%(tabla,str_campos, str_valores)
				print(consulta);
				cursor.execute(consulta)
				self.__conector.commit()
		finally:
			pass#self.__conector.close()
	def update(self, tabla, edicion, where):
		""" Método para realizar una edición a uno o más registros de una tabla
		    Parameters:
			    tabla (str): nombre de la tabla a la que se le quiere hacer el UPDATE
			    edicion (list): lista con str, con el nombre de los campos que se tomarán en cuenta en el insert
			    valores (list): lista con str, con el nombre de los valores de los campos que se tomarán en cuenta en el insert
		    
		    Returns: resultado(list | None): resultado de realizar la consulta a la tabla proporcionada y a los filtros proporcionados
		"""
		try:
			self.__conectar();
			with self.__conector.cursor() as cursor:
				str_edicion="";
				for campo in edicion:
					str_edicion=str_edicion+campo+"="+edicion[campo]+","
				str_edicion=str_edicion[:-1]
				str_where="";
				for campo in where:
					str_where=str_where+campo+"="+where[campo]+","
				str_where=str_where[:-1]
				consulta = "UPDATE %s SET %s WHERE %s"%(tabla, str_edicion, str_where)
				print(consulta);
				cursor.execute(consulta)
				self.__conector.commit()
		finally:
			pass#self.__conector.close()
	def delete(self, tabla, where):
		""" Método para eliminar registro(s) de una tabla en específico
		    Parameters:
			    tabla (str): nombre de la tabla a la que se le quiere hacer el DELETE
			    where (dict): Diccionario con las claves valor de los campos y su contenido que se utilizará como filtro para eliminar registros
		    
		    Returns: void
		"""
		try:
			self.__conectar();
			str_where="";
			for campo in where:
				str_where=str_where+campo+"="+where[campo]+","
			str_where=str_where[:-1]
			with self.__conector.cursor() as cursor:
				consulta = "DELETE FROM %s WHERE %s"%(tabla, str_where)
				print(consulta);
				cursor.execute(consulta)
				self.__conector.commit()
		finally:
			pass#self.__conector.close()
	def close_connection(self):
		""" Método para cerrar la conexión con el servidor de base de datos
		    Returns: void
		"""
		if(self.__conector is not None):
			self.__conector.close();






