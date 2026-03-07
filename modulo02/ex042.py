s1 = int(input("primeiro seguimento: "))
s2 = int(input("Segundo seguimento: "))
s3 = int(input("Terceiro seguimento: "))

if s1 < s2 + s3 and s2 < s1 +s3 and s3 < s1 +s2:
    print("Os seguimentos acima podem formar um triangulo!")

    #equilatero -- todos os lados iguais
    if s1 == s2 and s1 == s3 and s3 == s1:
        print("Os seguimentos formam um triangulo EQUILATERO!")
    #isoscelis -- dois lados iguais
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Os seguimentos formam um triangulo ISOSCELIS")
    #escaleno -- todos os lados diferentes
    else:
        print("Os seguimentos formam um triangulo ESCALENO")

else:
    print("Os seguimentos acima não podem formar um triangulo!")
