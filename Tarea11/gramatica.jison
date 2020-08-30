 
// Importaciones
%{
    const tmp = require('./acciones').tmp;
%}

// LEXICO
%lex
%options case-sensitive
%%

([a-zA-Z_])([a-zA-Z0-9_])*  {return 'tk_id'}
"+"                 %{ return 'tk_sumar'; %}
"-"                 %{ return 'tk_restar';%}
"*"                 %{ return 'tk_multiplicar';%}
"/"                 %{ return 'tk_dividir'%}
"("                 %{  return 'tk_pi';  %}
")"                 %{  return 'tk_pd';  %}
[ \t\r\n\f]+         {}

<<EOF>>     {  return 'EOF';   }

.	       { console.log('Error Lexico: ' + yytext ); }
  

/lex

%left tk_mas tk_menos
%left tk_multiplicar tk_division
%left tk_pa tk_pc

%start S
%% 

S   :   E EOF   { return $1.C3D}
    ;

E   :   E tk_sumar T    { temp=tmp.nuevoTemp(); $$ = { TMP: temp, C3D: $1.C3D + $3.C3D + "\n"+ temp+ "="+$1.TMP +"+"+ $3.TMP } }
    |   E tk_restar T  { temp=tmp.nuevoTemp(); $$ = { TMP: temp, C3D: $1.C3D + $3.C3D + "\n"+ temp+ "="+$1.TMP +"-"+ $3.TMP } }
    |   T   { $$ = {TMP: $1.TMP, C3D: $1.C3D} } 
    ;

T   :   T tk_multiplicar F  { temp=tmp.nuevoTemp(); $$ = { TMP: temp, C3D: $1.C3D + $3.C3D + "\n"+ temp+ "="+$1.TMP +"*"+ $3.TMP } }
    |   T tk_dividir F      { temp=tmp.nuevoTemp(); $$ = { TMP: temp, C3D: $1.C3D + $3.C3D + "\n"+ temp+ "="+$1.TMP +"/"+ $3.TMP } }
    |   F   { $$ = {TMP: $1.TMP, C3D: $1.C3D} }
    ;

F   :   tk_pi E tk_pd   { $$ = {TMP: $2.TMP, C3D: $2.C3D} }
    |   tk_id   { $$ = {TMP: $1, C3D: ''} }
    ;