# TextQL
DSL con el propósito de hacer consultas sobre un texto.

Para el desarrollo del lenguaje, fue utilizado PLY, que es una implementación de Python de las populares herramientas de construcción de compiladores lex y yacc. PLY es permanece fiel a la forma en que funcionan las herramientas tradicionales lex y yacc. Esto incluye admitir el análisis sintáctico LALR(1), así como proporcionar una amplia validación de entrada, informes de errores y diagnósticos.

## Primeros pasos
Para ejecutar un script de TextQL:

```
python TextQLCompiler.py <file_path>
```
La forma correcta de comenzar un script de TextQL es usando el keyword ```USE```, seguido de el tipo de documento (puede ser ```doc``` o también ```pdf```) y luego la dirección donde se encuentra, así se carga el documento sobre el cual se efectuarán las consultas:

```
USE doc 'data.docx';
```
Tenga en cuenta que cada una de las líneas en el script debe de terminar con ```;```.

Se tienen tres tipos base, ```string```, ```number```, ```boolean```. Para hacer una declaración se utiliza ```define```, de la siguiente forma:

```
define string name = 'Joe';
define number max = 100;
define boolean ready = false;
```

## Consultas
Para hacer una consulta se utiliza ```QUERY```, y luego el nombre de la función que queremos ejecutar:

```
QUERY LENGTH 5;
```
Se tienen distintas funciones:

- Filtros: 
  - ```JUSTWORD```: Elimina los signos de puntuación y deja solamente palabras.

  - ```LENGTH```: Toma hasta la cantidad especificada de cadenas.

- Modificadores: 
  - ```_slice```: Recorta cada palabra hasta la cantidad especificada de caracteres.
  
  - ```_touppercase```: Lleva todo a mayúsculas.
  
  - ```_tolowercase```: LLeva todo a minúsculas.

## Operadores
Se tienen operadores aritméticos y booleanos, lo que nos permite utilizar expresiones en nuestro lenguaje:

```
define number sum = 4 + 5 + 6;
define boolean small = 10 < 20;
```

## Condicionales

Uso de condicionales con ```IF```, ```THEN``` y ```ELSE```, por ejemplo:

```
define number max = 100;
define number sum = 4 + 5 + 6;
define boolean small = 10 < 20;

define string ite = IF 10 < (@max * @sum) - 1 THEN 'small' ELSE 4;
```

## Visión general
Podemos encontrar tres directorios en la organización del proyecto:

- ```builtins```: en este directorio tenemos las funciones builtins con las que cuenta el lenguaje.

- ```dsl```: en este directorio está la lógica principal del lenguaje, se encuentran definidos aquí ```lexer```, ```parser``` e ```interpreter```, así como los errores que maneja el lenguaje.

- ```ply```: dos módulos separados, ```lex``` y ```yacc``` que conforman PLY.

## PLY
PLY consta de dos módulos. El módulo ```lex.py``` se usa para 'tokenizar' el texto de entrada, a partir de reglas de expresión regular. El módulo ```yacc.py``` se utiliza para reconocer la sintaxis del lenguaje que se ha especificado en forma de gramática libre de contexto. 

Proporciona la validación de la gramática, la compatibilidad con producciones vacías, tokens de error y resolución de ambigüedades a través de reglas de precedencia.

El nombre "yacc" significa "Yet Another Compiler Compiler" y está tomado de la herramienta Unix del mismo nombre.