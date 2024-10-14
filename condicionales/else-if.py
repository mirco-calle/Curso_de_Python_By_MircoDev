ingreso_mensual = 12000
gasto_mensual = 6000

#if aninado y elif
if ingreso_mensual > 10000:
    if ingreso_mensual-gasto_mensual > 0:
        print("ahora si estas bien")
    else:
        print("estas gastando mucho hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien economicamente en latinoamerica")
    
else:
    print("sos pobre")