import random

nomes = ["Gustavo Medeiros", "Brenda Búzios", "Isac Silva", "Pedro Freitas", "Helena Moreira", "Ana Vitória Moraes", "Bruna Silveira", "Vitória Campos", "Letícia Cardoso", "MAariana Nunes"]
email = ["@hotmail.com", "@gmail.com", "@yahoo.com"]
figurinhas =    [["Harry Potter", "Grifinória", "Aluno", "Lendário"],
                ["Hermione Granger", "Grifinória", "Aluno", "Raro"],
                ["Ron Weasley", "Grifinória", "Aluno", "Raro"],
                ["Minerva Mcgonagall", "Grifinória", "Professor", "Lendário"],
                ["Alvo Dumbledore", "Grifinória", "Diretor", "Lendário"],
                ["Rubeo Hagrid", "Grifinória", "Guarda", "Comum"],
                ["Neville Longbottom", "Grifinória", "Aluno", "Comum"],
                ["Sirius Black", "Grifinória", "Bruxo", "Comum"],
                ["Olívio Wood", "Grifinória", "Aluno", "Comum"],
                ["Pomona Sprout", "Lufa Lufa", "Professor", "Comum"],
                ["Cedrico Diggory", "Lufa Lufa", "Aluno", "Comum"],
                ["Newton Scamander", "Lufa Lufa", "Bruxo", "Raro"],
                ["Silvano Ketleburn", "Lufa Lufa", "Professor", "Comum"],
                ["Zacarias Smith", "Lufa Lufa", "Aluno", "Comum"],
                ["Ana Abbott", "Lufa Lufa", "Aluno", "Comum"],
                ["Luna Lovegood", "Corvinal", "Aluno", "Raro"],
                ["Fílio Flitwick", "Corvinal", "Professor", "Comum"],
                ["Quirino Quirrel", "Corvinal", "Professor", "Comum"],
                ["Padma Patil", "Corvinal", "Aluno", "Comum"],
                ["Miguel Corner", "Corvinal", "Aluno", "Comum"],
                ["Garrick Olivaras", "Corvinal", "Bruxo", "Comum"],
                ["Sibila Trelawney", "Corvinal", "Professor", "Comum"],
                ["Alvo Potter", "Sonserina", "Aluno", "Comum"],
                ["Tiago Potter", "Sonserina", "Aluno", "Comum"],
                ["Lilian Potter", "Sonserina", "Aluno", "Comum"],
                ["Dolores Umbridge", "Sonserina", "Professor", "Comum"],
                ["Severo Snape", "Sonserina", "Professor", "Raro"],
                ["Draco Malfoy", "Sonserina", "Aluno", "Raro"],
                ["Merlin", "Sonserina", "Bruxo", "Lendário"],
                ["Lord Voldemort", "Sonserina", "Bruxo", "Lendário"]]



# 1. Esse tópico é responsável por criar, aleatoriamente, informações para popularmos a tabela de USUÁRIOS.

print("insert into USUÁRIO (id_usuario, nome_usuario, email_usuario) values")
for id_usuario in range(10):
    nome_usuario = nomes[id_usuario]
    email_usuario = nome_usuario.lower().replace(" ", "") + random.choice(email)
    
    print(f"({id_usuario + 1}, '{nome_usuario}', '{email_usuario}'),")



# 2. Esse tópico é responsável por criar, aleatoriamente, informações para popularmos a tabela de POSSES.

print("insert into POSSES (id_usuario, figurinha_01, figurinha_02, figurinha_03, figurinha_04, figurinha_05, figurinha_06, figurinha_07, figurinha_08, figurinha_09, figurinha_10, figurinha_11, figurinha_12, figurinha_13, figurinha_14, figurinha_15, figurinha_16, figurinha_17, figurinha_18, figurinha_19, figurinha_20, figurinha_21, figurinha_22, figurinha_23, figurinha_24, figurinha_25, figurinha_26, figurinha_27, figurinha_28, figurinha_29, figurinha_30) values")

for id_figurinha in range(10):
    print(f"({id_figurinha + 1}", end = "")
    for colunas in range(30):
        quantidade = random.randint(1, 10)
        print(f", {quantidade}", end = "")
    
    print("), ")



# 3. Esse tópico é responsável por criar, aleatoriamente, informações para popularmos a tabela de FIGURINHAS.

print("insert into FIGURINHAS (id_figurinha, titulo_figurinha, casa_figurinha, classe_figurinha, raridade_figurinha) values")
id_figurinha = 1

for figurinha in figurinhas:
    titulo_figurinha = figurinha[0]
    casa_figurinha = figurinha[1]
    classe_figurinha = figurinha[2]
    raridade_figurinha = figurinha[3]

    print(f"({id_figurinha}, '{titulo_figurinha}', '{casa_figurinha}', '{classe_figurinha}', '{raridade_figurinha}'),")
    id += 1