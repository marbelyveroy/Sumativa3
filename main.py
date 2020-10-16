# -*- coding: utf-8 -*-
from base_datos import *

def main(argv):
    base_datos= Base_datos();
    base_datos.setCredenciales("HOST", "USUARIO_BD", "PASSWORD_BD", "NOMBRE_BD")



    #SELECT
    select=base_datos.select("usuario", [
        {"campo":"id", "condicion":"=", "valor":"1"}
    ]);
    print(select);
    
    #INSERT
    base_datos.insert("usuario", ["nombre", "edad", "direccion"], ["'José Perez'","70","'Monterrey, México'"]);
	
    #UPDATE
    base_datos.update("usuario", {"nombre":"'fake'"}, {"id":"1"});
	
    #DELETE
    base_datos.delete("usuario", {"id":"1"});

if __name__ == "__main__":
    main(sys.argv)
















