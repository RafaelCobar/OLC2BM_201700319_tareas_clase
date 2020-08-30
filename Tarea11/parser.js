var fs = require('fs'); 
var parser = require('./gramatica');
var ast
var i

fs.readFile('./entrada.txt', (err, cotenido) => {
    i = 0
    if (err) throw err;
    ast = parser.parse(cotenido.toString());
    console.log(ast)
    // leerAST(ast)
});


