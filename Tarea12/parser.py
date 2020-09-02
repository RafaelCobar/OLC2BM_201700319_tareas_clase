import gramatica as g

x = 0
def newTemp():
    global x
    x += 1
    temp = "t"+str(x)
    return temp

def recorrerAST(nodo):
    if isinstance(nodo, str):
        return (nodo, "")
    else:
        izqTMP, izqC3D = recorrerAST(nodo.opIzq)
        derTMP, derC3D = recorrerAST(nodo.opDer)
        signo = nodo.signo
        temporal = newTemp()
        return (temporal, izqC3D + derC3D + "\n"+temporal+" = "+izqTMP + " "+signo+" "+derTMP)


ast = g.parse("a+b*c/d+g*j")
tmp, c3d = recorrerAST(ast)
print(c3d)
