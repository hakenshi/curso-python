pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "sexo": "masculino",
    "cidade": "São Paulo",
    "profissão": "Engenheiro",
    "email": "joao.silva@example.com",
    "telefone": "(11) 98765-4321"
}
print('\n')
for keys, values in pessoa.items():
    print(f'{keys.capitalize()}: {values}')
print('\n ')