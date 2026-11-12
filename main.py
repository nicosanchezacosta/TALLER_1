import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

mayor_gasto = 0
cliente_vip = ""

mas_productos = 0
mejor_cliente = ""

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total += compra["precio"]

    print(f"{usuario}: {total:.2f} €")

    cantidad = len(compras)
    print(f"Productos comprados: {cantidad}")

    if total > mayor_gasto:
        mayor_gasto = total
        cliente_vip = usuario

    if cantidad > mas_productos:
        mas_productos = cantidad
        mejor_cliente = usuario

print(f"\nCliente VIP: {cliente_vip} - {mayor_gasto:.2f} €")

print(f"Más productos: {mejor_cliente} - {mas_productos}")
