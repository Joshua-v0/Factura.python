cost = 0
pag = 0
cant = 0
impuesto = 0.07
contador = 0

nom = input("Ingrese su nombre: ")
cant = int(input(f"ingrese cantidad de productos que desea llevar {nom}: "))
for x in range(cant):
    contador = contador +1
    prod = input("\nIngrese el nombre del producto: ")
    cost = float(input("Ingrese el precio del producto: "))
print(f"{nom}, el total a pagar es:", (cost*cant)+1.07) 
pag = float(input(f"ingrese el monto que pago {nom}: "))


costo_total = cant*cost  
itbms= round((cant * cost) * 0.07,2)  
total= round((cant*cost)+itbms,2) 

print("\n ------------------ ")    
print("\nnombre:", nom) 
print("cantidad:", cant)
print("costo del producto:", cost) 
print("ITBMS:", impuesto) 
print("total a pagar:", total)   

if total == pag: 
    vuelto=0
    print("\nMuchas gracias por su compra.") 
    print("\n\n----------------Factura----------------")
    print("Cliente: ",nom)
    print("Cantidad: x",cant)
    print("-------------------------------------------")
    print("precio unitario: ",cost)
    print("precio total: ",costo_total)
    print("ITBMS: ",itbms)
    print("Total a pagar:",total)
    print("--------------------------------------------") 
    print("total pagado: ",pag)
    print("--------------------------------------------")
    print("vuelto: ",vuelto)

elif pag > total:  
    vuelto=round(pag-total,2)
    print(f"\nmuchas gracias por su compra, su vuelto seria {vuelto}.") 
    print("\n\n---- Factura ----")
    print("Cliente: ",nom) 
    print("Cantidad: x",cant)
    print("--------------------------------")
    print("precio unitario: ",cost)
    print("precio total: ",costo_total)
    print("ITBMS:",itbms)
    print("Total a pagar:",total)
    print("--------------------------------")
    print("total pagado: ",pag)
    print("--------------------------------")
    print("vuelto: ",vuelto)
elif pag < total:
    print("\ntarjeta declinada")  
    



    




     

    