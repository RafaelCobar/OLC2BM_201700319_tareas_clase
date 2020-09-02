
# Tarea12 Generacion de C3D con Ply 
Enunciado: Escriba un esquema de traducción dirigido por la sintaxis posfijo, para un analizador ascendente que reciba como entrada una expresión aritmética (*,+,-,/ y paréntesis) y genere para esta el código de tres direcciones equivalente.

Para esta tarea 12 se utilizó ply en donde realizo mi analisis léxico y sintáctico, donde en cada uno de las producciones obtengo su atributo sintetizado ya sea generando un nuevo cuando se realizan operaciones o solo obteniendo el id. 

En el archivo parser.py obtengo el ast que me genera la gramatica y recorro el ast en recorrido postorden para luego solo imprimir el código de C3D