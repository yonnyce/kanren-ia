from kanren import * # Relation, facts, var, run, eq, etc...

# Definición de las funciones
def progenitor(A, B):  # agrupa a padres y madres como progenitores
    #evalúa la disyunción: Progenitor(x,y) <- Padre(x,y) OR Madre(x,y)
    return conde([padre(A,B)],[madre(A,B)]) 

def hermano(A, B):
    X = var()
    #evalúa la conjunción Hermano(x,y) <- Progenitor(z,x) AND Progenitor (z,y). La cláusula x <> y se debe evaluar en el código python después del llamado
    return conde((progenitor(X,A), progenitor(X,B)))  
   
# Definición de las relaciones básicas
padre = Relation()
madre = Relation()

# Lista de hechos (facts)
facts(padre, ("Homero", "Bart"),("Homero", "Lisa"),("Homero", "Maggie"),("Abraham","Homero"),("Clancy", "Marge"),("Clancy", "Patty"),("Clancy", "Zelma"),("Homero","Hugo"))
facts(madre, ("Marge", "Bart"),("Marge", "Lisa"),("Marge", "Maggie"),("Jacqueline", "Marge"),("Jacqueline", "Zelma"),("Jacqueline", "Patty"),("Mona","Homero"),("Selma","Ling"),("Marge","Hugo"))



b=var()
nombre="Zelma"
salida =run(0,b,hermano(b,nombre))
hermanos = [x for x in salida if x != nombre]
print (hermanos)

