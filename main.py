import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total += compra["precio"]

    print(f"{usuario}: {total:.2f} €")
    mayor_gasto = 0
cliente_vip = ""
    if total > mayor_gasto:
        mayor_gasto = total
        cliente_vip = usuario
        cliente_vip = max(data, key=lambda usuario: sum(c["precio"] for c in data[usuario]))
print(cliente_vip)

