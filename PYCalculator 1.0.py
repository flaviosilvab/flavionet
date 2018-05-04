print ("")
print ("")
print ("")
print ('''                       BEM VINDO A CALCULADORA DO FLAVIO 1,0v''')
ide = input("Digite seu nome:  ")
print ('''        
         Seja bem vindo,''',ide)

nome = input ('''      Por favor escolha sua operação:

            -------------------
            |       +         |
            |       -         |
            -------------------     
            ''')
if nome == "+":
    a = int (input("Digite aqui seu primeiro numero:   "))
    b = int (input ("Digite seu segundo numero:  "))
    print ("Resultado:",a + b)
elif nome == "-":
    c = int(input("Digite aqui seu primeiro numero:   "))
    d = int(input("Digite seu segundo numero:  "))
    print ( c - d )