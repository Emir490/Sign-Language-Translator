import numpy as np
import os


path = os.path.join('src','data','categories')

# ABC
actions = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 
                    'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

np.save(os.path.join(path,'abc'),actions)

# Adjetivos, pronombres, preposiciones y articulos
actions = np.array(['adjetivo','algo','ante','articulo','cada','conmigo','contigo_v1','contigo_v2','contra','de',
                    'el-ella','ellos','en','entre_v1','entre_v2','esa-ese-eso','mi-mio','mismo','ni','nos-nosotros-nuestro',
                    'para','por','primero','propio','suyo','tambien','todavia','todo','tú','tuyo','ustde','yo_v1','yo_v2',
                    ])

np.save(os.path.join(path,'adjetivos'),actions)

# Alimentos
actions = np.array(['aceite','agrio','agua','alimento','apetito','arroz','asar','atole','avena','azucar','bacardi','bistec',
                    'cafe','caldo','acrne','catsup','cena_v1','cena_v2','cereal','cerveza','chicle','chocolate','chorizo',
                    'coca cola','comida_v1','comida_v2','crema','delicioso','desayuno_v1','desayuno_v2','dona','dulce',
                    'enchiladas','ensalada','espagueti','fideo','galleta','gelatina','grasa','hambre','hamburguesa','harina',
                    'helado','hot dog','huevo','jamon','leche','legumbres','licor','limonada','mantequilla','mayonesa',
                    'mermelada','miel_v1','miel_v2','mole','mostaza','ordeñar','paleta_v1','paleta_v2','pan','pastel','pay',
                    'picoso','piloncillo','pimineta','pizza_v1','pizza_v2','polvo','postre_v1','postre_v2','pulque_v1','pulque_v2',
                    'quesadilla_v1','quesadilla_v2','queso','refresco','rico','sabroso','sal','salchicha','salsa','sandwich',
                    'satisfecho_v1','satisfecho_v2','sed','sopa','sope','taco','tamal','té','torta','tortilla','vinagre','vino',
                    'whisky','yogur'])

np.save(os.path.join(path,'alimentos'),actions)

# Animales
actions = np.array(['abeja','aguila','ala','alacran','almeja','animal','araña','ardilla','asno','avestruz','avispa','becerro',
                    'borrego','buey','bufalo','buho','burro','caballo','cabra','calamar','camaron','camello','canguro','caracol',
                    'cebra','chango_v1','chango_v2','chivo','cisne','cochino','cocodrilo','conejo','cordeo','delfin','elefante',
                    'flamenco','foca','gallo','gato','gorila','guajolote','gusano','hipopotamo','hormiga','iguana-lagarto','jabali',
                    'jirafa','leon','liebre','lobo','mariposa_v1','mariposa_v2','mono','mosca','mosquito','mula','murcielago',
                    'oso','ostion','pajaro','paloma','pantera','pato','pavo real','pelicano','perico','perro','pez','pingüino',
                    'pollo','puerco','puerco espin','pulpo','rana','raton','rinoceronte','sapo','tiburon_v1','tiburon_v2',
                    'tigre','toro','tortuga','vaca','vampiro','venado','vivora','zorrillo','zorro'])

np.save(os.path.join(path,'animales'),actions)

# Antonimos
actions = np.array(['abajo_v1','abajo_v2','abrir','acompañado','adentro','afuera','agarrar','alegre','alto','amable','antes',
                    'antonimo','apagar','aparecer','aplastar','arriba_v1','arriba_v2','bajar','bajo','bien','bonito','buena suerte',
                    'bueno','calma','caminar','caro','cerrar','chico','cierto','con','construir','contestar','corto','dar','debajo',
                    'dejar','delante','derecha','derrumbar','desaparecer','despacio','despues','detener','detras','dificil','duro',
                    'empezar','enano','encender','encima','encotrar_cosas','encontrar_personas','entrar','exaltacion','expandir',
                    'facil_v1','facil_v2','falso','felicitar','feo','ganar','gigante_v1','gigante_v2','grande','gratis','grosero',
                    'guapo','imposible','izquierda','jamas','largo','limpio','lleno','llorar','luz','mal','mala suerte','malo','mas',
                    'mejor','menos_v1','menos_v2','mentira','mojado_v1','mojado_v2','mucho','no','no saber','nunca','olvidar',
                    'oscrudiad','pedir','peor','perder','pobre','poco','poner','preguntar','prender','quitar','rapido','recordar',
                    'regañar','reir','responder','rico','saber','salir','seco','serio','sí','siempre','sin','sinonimo','solo','suave',
                    'subir','sucio','terminar','triste','vacio','verdad'])

np.save(os.path.join(path,'antonimos'),actions)

# Calendario
actions = np.array(['lunes','martes','miercoles','jueves','viernes','sabado','domingo',
                    'enero','febrero','marzo','abril','mayo','junio','julio','agosto',
                    'septimebre','octubre','noviembre','diciembre','primavera','verano',
                    'otoño','invierno','hoy','ayer','mañana','presente','pasado','futuro',
                    'buenos dias','buenas tardes','buenas noches','amanecer','antiguo_v1',
                    'antiguo_v2','año','dia','mediodia','mes','noche','semana','tarde','temprano'])

np.save(os.path.join(path,'calendario'),actions)

# Casa
actions = np.array(['almohada','azotea','azucarera','baño','barrer','basura','batidora','bote','buzon',
                    'cacerola','cajon','cama','candelero','casa_v1','casa_v2','cazuela',
                    'cepillo de dientes','cepillo de pelo','champu','charola','chimenea','chupon',
                    'cobertor','cocina','coladera','colador','colcha','comal','comedor','comoda','condominio',
                    'copa','corredor','corriente','cortina','cuarto','cuchara','cuchillo','departamento',
                    'destapador','direccion_dar la','direccion_dirigir','edificio','electricidad',
                    'escalera_v1','escalera_v2','escritorio','escusado','espejo','estufa','florero',
                    'foco','fogata-fuego','frutero','garage','hogar','horno','jabon','jardin','jerga','lampara',
                    'lavabo','lavadora','licuadora','llava_abrir','llave_cerrar','mamila','mantel',
                    'maquina de coser','maquina de escribir','mesa','molde','mueble','olla','olla expres',
                    'pared','parque','parrilla','pasta de dientes','patio','pimienta','pimientero','piso_v1'
                    'piso_v2','plato','puerta_v1','puerta_v2','rasurar','refrigerador','regadera','reja',
                    'reloj','ropero','sabana','sala','salero','sarten','secadora_manos','secadora_cabello',
                    'servilleta','silla','sotano','tapadera','tapete','tapiz','tenedor','tijeras','timbre',
                    'tina','toalla','tocador','tostador','trapeador','trapo','trastes','tubo','vaso','vecindad',
                    'vela','ventana','vidrio','vitrina'])

np.save(os.path.join(path,'casa'),actions)

# Colores
actions = np.array(['amarillo','anaranjado','azul','azul rey','blanco','brillante','bronce','café','claro',
                    'color','gris','morado','negro','oscuro','oro','plata','rojo_v1','rojo_v2','rosa',
                    'rosa mexicana','verde','verde limon'])

np.save(os.path.join(path,'colores'),actions)
# Cuerpo humano
actions = np.array(['barba','barbilla','bigote','boca','brazo','cadera','cara','ceja','codo','cuello','diente',
                    'espalda','estomago','frente','garganta','hombro','hueso','labios','lengua','mano','mejilla',
                    'muñeca','nariz','ojo','oreja','pecho','pelo','pestañas','pulgar','uña'])

np.save(os.path.join(path,'cuerpo_humano'),actions)

# Escuela
actions = np.array(['antropologia','bandera','calificaion','campana_v1','campana_v2','certificado','campás',
                    'computacion','cuaderno','dibujo','diccionario_v1','diccionario_v2','escala','escuadra',
                    'escuela','estudiante','goma','lapiz','leccion','mapa','microscopio','papel','parrafo',
                    'perspectiva','pizarron','pluma','politecnico','premio','preparatoria','primaria','preuba',
                    'quimica','sacapuntas','secundaria','tecnologico'])

np.save(os.path.join(path,'escuela'),actions)

# Familia
actions = np.array(['abuela','abuelo','adulto','ahijada','ahijado','amante','amiga','amigo','amistad','anciana',
                    'anciano','bebe','bisabuela','bisabuelo','bisnieta','bisnieto','boda','caballero','cariño',
                    'casada','casado','comadre','compadre','compañera','compañero','concuñada','concuñado',
                    'cosuegra','consuegro','cuates','cuñada','cuñado','dama_v1','dama_v2','divorciada_v1',
                    'divorciada_v2','divorciado_v1','divorciado_v2','esposa','esposo','familia','femenino',
                    'gemelos','generacion','herencia','hermana','hermano','hija','hijastra','hijastro','hijo',
                    'hombre','huerfana','huerfano','joven','juvenil','juventud','madrastra_v1','madrastra_v2',
                    'madre','madrina','mama','masculino','matrimonio','media hermana','medio hermano','mujer',
                    'nieta','nieto','niña','niño','novia','novio','nuera','padrasttro','padre','padres','padrino',
                    'papá','pareja_v1','pareja_v2','persona','prima','primo','señor','señora','señorita','separada',
                    'separado','sobrina','sobrino','soltera','soltero','suegra','suegro','tatarabuela','tatarabuelo',
                    'tia','tio','tutor','union libre','vieja','viejo','viuda','viudo','yerno'])

np.save(os.path.join(path,'familia'),actions)

# Frutas y verduras
actions = np.array(['aceituna_v1','aceituna_v2','acelga','aguacate_v1','aguacate_v2',
                    'ajo','alcachofa','almendra','berenjena','betabel','cacahuate',
                    'calabacita','calabaza','camote','caña','cabolla','cereza_v1',
                    'cereza_v2','champiñon','chayote','chicharo','chile','cilantro',
                    'ciruela','coco_v1','coco_v2','col','coliflor','durazno',
                    'ejote','elote','esparrago','espinaca','fresa',
                    'frijol','fruta','granada','guayaba','haba','higo',
                    'hongo','jamaica','jicama','jitomate','lechuga','lima',
                    'limon_v1','limon_v2','maiz','mamey','mandarina','mango_v1',
                    'mango_v2','manzana','melon','naranja','nopal',
                    'nuez','papa','papaya','pasa','pepino','pera',
                    'perejil','piña','piñon','platano','sandia','tamarindo',
                    'tejocote','tomate','toronja','tuna','uva','verdura_v1',
                    'verdura_v2','zanahoria','zapote'])

np.save(os.path.join(path,'frutas_verduras'),actions)

# Numeros
actions = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    '11', '12', '13', '14', '15_v1', '15_v2', '16', '17', '18', '19', 
                    '20', '25_v1', '25_v2', '30', '40', '50', '60', '70', '80', '90',
                    '100', '200', '300', '400', '500', '600', '700', '800', '900',
                    '1000', '2000', '3000', 'MILLON',
                    'PRIMERO', 'SEGUNDO', 'TERCERO', 'CUARTO', 'QUINTO', 'SEXTO'])

np.save(os.path.join(path,'numeros'),actions)

# Numeros - Palabras relacionadas
actions = np.array(['circulo','conjunto','contar',
                    'cuadrado','diagonal','division','doble','dolar','esfera',
                    'froma','grupo','horizontal','lado','linea_v1','linea_v2',
                    'matematicas','millonario','mitad','multiplicacion','numero','raiz cuadrada',
                    'rectangulo','resta','suma','triangulo','ultimo','vertical'])

np.save(os.path.join(path,'palabras_relacionadas'),actions)

# Republica Mexicana
actions = np.array(['Acapulco','Aguascalientes','Baja California','Baja California Sur','Campeche','Chetumal',
                    'Chiapas','Chihuahua','Chilpancingo','ciudad','Ciudad Victoria',
                    'Coahuila','Colima','Cuernavaca','Culiacan','Distrito Federal','Durango',
                    'estado','Guadalajara','Guanajuato','Guerrero','Hermosillo','Hidalgo',
                    'Jalisco','La Paz','Merida','Mexicali','México',
                    'Michoacan','Monterrey','Morelia','Morelos','Nayarit',
                    'Nuevo Leon','Oaxaca','Pachuca','Puebla','Queretaro',
                    'Quintana Roo','Saltillo','San Luis Potosi','Sinaloa','Sonora',
                    'Tabasco','Tamaulipas','Tampico','Tepic','Tijuana','Tlaxcala',
                    'Toluca','Tuxtla Gutierrez','Veracruz','Villahermosa',
                    'Xalapa','Yucatan','Zacatecas'])

np.save(os.path.join(path,'republica_mexicana'),actions)

# Otras palabras
actions = np.array(['abandonar','abrazar','acceso','aceptar',
                    'acostumbrar','adios','ahí','ahora','alabar','allá',
                    'amolado','antifaz','apestoso','aprender','aprisa',
                    'aprobado','aqui','arete','asomar','ayudar','bailar',
                    'balon','barreras','besarse','bilingüe','bombero','bondad',
                    'bostezar','breve','calavera','calendario','castigar','centro',
                    'coger','coma','conde','conocer','convertir',
                    'coqueto','coraje','cortar','criticar','cuál','cuidado',
                    'curioso','defender','depender','descansar','diablo','diferente',
                    'dinero','Dios','discirminar','duda','dueño','en medio',
                    'enfrente','enojado','enrollar','entregar','envidia','escoger',
                    'espiritu','esquina','estacionar','estar','eterno',
                    'fabrica-motor','favor','fin','flor','frente',
                    'frio','frontera','fuera','golpear',
                    'guardar','hacer','hipocrita','iglesia','infeccion','invitar',
                    'judio','jugar','jugar canicas','libertad','libre','libro',
                    'liso','luna','manejar','Virgen Maria','microfono','moda',
                    'momento','motocicleta','nada','nadar','necesitar','negocio',
                    'nivel','no esta-no hay','no sirve','nombre','oir',
                    'ojala','otra vez','otro','pala','palabra','panteon',
                    'partir','pasos','paz','pelota','pena','pensar',
                    'perfume','permanecer','pero','pesos','piano','pistola',
                    'plural','popote','presidente','principe','pronto','proteger',
                    'pueblo','punto','querer','radio','rebanar','regresar',
                    'resumen','rey','saludar','sangre','sentir','sentar',
                    'ser','sexo','sintesis','socio','soltar','soñar',
                    'soplar','sostener','sudar','superar','taxi','teatro',
                    'temperatura','tener','tienda','tobogan','tocar','tomar',
                    'traducir','transformar','unido','untar','urgente','usar',
                    'util','vago','valioso','ver','vez','volar',
                    'voleivol','votar','voz','zapato'])

np.save(os.path.join(path,'otras_palabras'),actions)
