notas = []

for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

soma_notas = sum(notas)
media = soma_notas / 10

if media <= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Média: ", media)
print("Status: ", situacao)

