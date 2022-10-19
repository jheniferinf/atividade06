import os 


c: str
compra: float; cv: float; ct: float
compra = 0
cv = 0
cp = 0 
c =""

for n in range(1, 5):
    print(f"dados da {n} a venda")

    while(c != "v" and c != "p"):
        c = input(
            "digite o codigo da compra (V - á vista ou P - a prazo): ").upper()
        if c == "V" : 
            compra = float(input("digite o valor da compra: R$ "))
            cv =cv + compra
        elif c == "P" : 
            compra  = float(input("Digite o valor da compra R$ "))
            cp = cp + compra 
    c = ""

    os.system("cls")

    print(f"o valor total á vista: R$ {cv:.2f}")
    print(f"o valor total á prazo: R$ {cp:.2f}")
    print(f"o valor total das compras: R$ {cp + cv:.2f}")
    print(
        f"o valor da primeira prestação das compras  a prazo juntas: R$ {cp/3:.2f}")
    