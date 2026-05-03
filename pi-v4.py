# Aplicativo web para doação e reaproveitamento de materiais

if 'lista_alunos_geral' not in locals():
  lista_alunos_geral = []
if 'lista_matriculas' not in locals():
  lista_matriculas = []
if 'lista_alunos_ensino_fundamental' not in locals():
  lista_alunos_ensino_fundamental = []
if 'lista_alunos_ensino_medio' not in locals():
  lista_alunos_ensino_medio = []

if 'lista_materiais_geral' not in locals():
  lista_materiais_geral = []
if 'lista_doacoes_geral' not in locals():
  lista_doacoes_geral = []

if 'lista_materiais_fundamental' not in locals():
  lista_materiais_fundamental = []
if 'lista_materiais_fundamental_recebidos' not in locals():
  lista_materiais_fundamental_recebidos = []
if 'lista_materiais_fundamental_doados' not in locals():
  lista_materiais_fundamental_doados = []

if 'lista_materiais_ensino_medio' not in locals():
  lista_materiais_ensino_medio = []
if 'lista_materiais_ensino_medio_recebidos' not in locals():
  lista_materiais_ensino_medio_recebidos = []
if 'lista_materiais_ensino_medio_doados' not in locals():
  lista_materiais_ensino_medio_doados = []


class Aluno:
  def __init__(self, matricula, nome, idade, serie, turma, ensino_medio):
    self.nome = str(nome)
    self.matricula = str(matricula)
    if self.matricula in lista_matriculas:
      raise ValueError('Matrícula já está na lista') 
    lista_matriculas.append(self.matricula) 
    self.idade = int(idade)
    self.serie = int(serie)
    self.turma = str(turma).upper()
    self.ensino_medio = str(ensino_medio).lower()
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_alunos_ensino_medio.append(self)
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_alunos_ensino_fundamental.append(self)
    lista_alunos_geral.append(self)

  def realizou_doacao(self):
    print(f'O Aluno {self.nome} - {self.matricula} Realizou a doação do material\n')
  
  def recebeu_doacao(self,):
    print(f'O Aluno {self.nome} - {self.matricula} Reacebeu a doação do material\n')
  
  def exibir(self):
    print(f'N° Matrícula: {self.matricula} - Nome: {self.nome} - {self.idade} Anos - Série: {self.serie}ª - Turma: {self.turma} - Ensino Médio: {self.ensino_medio}\n')

  def novo_aluno(self, serie_antiga, repetiu, aluno_novato, transferido):
    self.serie_antiga = str(serie_antiga)
    self.aluno_novato = str(aluno_novato)
    if self.aluno_novo == 'sim':
      print(f'{self.nome} Aluno novo')
    self.repetiu = str(repetiu)
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      print(f'O aluno {self.nome} deve fazer o ano letivo, novamente')
    self.transferido = str(transferido)


class Material:
  def __init__(self, nome_do_aluno_dono, codigo_material, ensino_medio, serie, disciplina, obs):
    self.nome_do_aluno_dono = str(nome_do_aluno_dono)
    if not any(aluno.nome == self.nome_do_aluno_dono for aluno in lista_alunos_geral):
      raise ValueError('Nome do aluno não encontrado')
    self.codigo_material = str(codigo_material)
    self.serie = str(serie)
    self.disciplina = str(disciplina)
    self.ensino_medio = str(ensino_medio).lower()
    self.obs = str(obs)
    lista_materiais_geral.append(self)
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio.append(self)
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental.append(self)

  def exibir(self):
    print(f'Código do Material: {self.codigo_material} - Série: {self.serie} - Disciplina: {self.disciplina} - Ensino  Médio: {self.ensino_medio} - Dono: {self.nome_do_aluno_dono}\n')


class Doacao:
  def __init__(self, ensino_medio, serie, disciplina, codigo_do_material):
    self.ensino_medio = str(ensino_medio).lower()
    self.serie = int(serie)
    if (self.serie > 3 and self.ensino_medio == 'sim') or (self.serie > 3 and self.ensino_medio == 's'):
      raise ValueError('Ensino Médio não possui + de 3 séries')
    self.disciplina = str(disciplina)
    self.codigo_do_material = str(codigo_do_material)
    if not any(material.codigo_material == self.codigo_do_material for material in lista_materiais_geral):
      raise ValueError("Material não encontrado na lista geral.")

  def realizou(self, nome_do_aluno_doador, codigo_do_material, disciplina, obs):
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    if not any(aluno.nome == self.nome_do_aluno_doador for aluno in lista_alunos_geral):
      raise ValueError('Nome do aluno não encontrado na lista geral')
    self.codigo_do_material = str(codigo_do_material)
    self.disciplina = str(disciplina)
    # Correção: Verifica se o atributo codigo_do_material de algum objeto Material corresponde
    if not any(material.codigo_material == self.codigo_do_material for material in lista_materiais_geral):
      raise ValueError('Código do material não encontrado')
    if (self.serie > 3 and self.ensino_medio == 'sim') or (self.serie > 3 and self.ensino_medio == 's'):
      raise ValueError('Ensino Médio não possui + de 3 séries')
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio_doados.append(self)
      print(f'\nO Aluno {nome_do_aluno_doador} do Ensino Médio, Realizou doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental_doados.append(self)
      print(f'\nO Aluno {nome_do_aluno_doador} do Ensino Fundamental, Realizou doação\n')
    self.obs = str(obs)
    lista_doacoes_geral.append(self)

  def exibir_realizou(self):
    print(f'O Aluno {self.nome_do_aluno_doador} Realizou doação do {self.codigo_do_material} - {self.obs} - da disciplina de {self.disciplina}\n')

  def recebeu(self, nome_do_aluno_recebedor, serie_aluno_recebedor, ensino_medio, codigo_do_material, obs):
    self.nome_do_aluno_recebedor = str(nome_do_aluno_recebedor)
    if not any(aluno.nome == self.nome_do_aluno_recebedor for aluno in lista_alunos_geral):
      raise ValueError('nome_do_aluno_recebedor não encontrado')
    self.serie_aluno_recebedor = str(serie_aluno_recebedor)
    self.ensino_medio = str(ensino_medio).lower()
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
        print(f'O Aluno {nome_do_aluno_recebedor} do Ensino Médio, Recebeu doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
        print(f'O Aluno {nome_do_aluno_recebedor} do Ensino Fundamental, Recebeu doação\n')
    self.codigo_do_material = str(codigo_do_material)
    if not any(material.codigo_material == self.codigo_do_material for material in lista_materiais_geral):
      raise ValueError('codigo_do_material não encontrado')
    self.obs = str(obs)
    lista_doacoes_geral.append(self)
    print(f'O Aluno {nome_do_aluno_recebedor} recebeu o material doado\n')


  def exibir_recebeu(self):
        print(f'O Aluno {self.nome_do_aluno_doador} Recebeu doação de {self.codigo_do_material} - {self.obs} - da disciplina de {self.disciplina}\n')


# testes

print('\nLista de alunos Geral')
for i in lista_alunos_geral:
  print(f' Aluno {i.nome} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_alunos_geral) == 0:
  print('Lista Vazia\n')

a1 = Aluno('123456789', 'Luiz', 16, 2, 'a', 'sim')
a1.exibir()
a1.realizou_doacao()

a2 = Aluno('987654321', 'Felipe', 15, 2, 'a', 'Sim')
a2.exibir()
a2.realizou_doacao()
a2.recebeu_doacao()

a3 = Aluno('147258369', 'Abner', 11, 7, 'a', 'não')
a3.exibir()

a4 = Aluno('159753456', 'Marcus', 10, 7, 'b', 'Não')
a4.exibir()

a5 = Aluno('789456123', 'Luiz', 17, 3, 'b', 'SIM')
a5.exibir()

a6 = Aluno('748596123', 'Luan', 7, 3, 'b', 'NÃO')
a6.exibir()

a7 = Aluno('015436987', 'Marcos', 16, 3, 'b', 'SIM')
a7.exibir()


print('\nLista de alunos Geral')
for i in lista_alunos_geral:
  print(f' Aluno {i.nome} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_alunos_geral) == 0:
  print('Lista Vazia\n')

print('\nLista de alunos Ensino Fundamental')
for i in lista_alunos_ensino_fundamental:
  print(f' Aluno {i.nome} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_alunos_ensino_fundamental) == 0:
  print('Lista Vazia\n')

print('\nLista de alunos do Ensino Médio')
for i in lista_alunos_ensino_medio:
  print(f' Aluno {i.nome} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_alunos_ensino_medio) == 0:
  print('Lista Vazia\n')
  
print('\nLista de Materiais Geral')
for i in lista_materiais_geral:
  print(f'{i.codigo_material} - {i.disciplina} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_materiais_geral) == 0:
  print('Lista Vazia\n')

m1 = Material('Luiz', '1548625397', 'sim', 2, 'História', ' ')
m1.exibir()

m2 = Material('Felipe', '987654321', 'sim', 2, 'Português', ' ')
m2.exibir()

m3 = Material('Abner', '147258369','Não', 7, 'Matemática', 'Livro de questões')
m3.exibir()

m4 = Material('Marcus', '159753456', 'não', 7, 'Matemática', ' ')
m4.exibir()

m5 = Material('Luiz', '1548693207', 'NÃO', 8, 'Português', 'Caderno de respostas auxiliares')
m5.exibir()

m6 = Material('Luan', '7485962310', 'SIM', 9, 'Geografia',  ' ')
m6.exibir()


print('\nLista de Materiais Geral')
for i in lista_materiais_geral:
  print(f'{i.codigo_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais Fundamental')
for i in lista_materiais_fundamental:
  print(f'{i.codigo_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais do Ensino Médio')
for i in lista_materiais_ensino_medio:
  print(f'{i.codigo_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')


d1 = Doacao('sim', 2, 'História', '1548625397')
d1.realizou('Luiz', '1548625397', 'História', ' ')
d1.exibir_realizou()

d2 = Doacao('Felipe', 2, 'Português', '987654321')
d2.realizou('Felipe', '987654321', 'Português', ' ')
d2.exibir_realizou()

print('\nLista de Doações')
for i in lista_doacoes_geral:
  print(f'{i.nome_do_aluno_doador} realizou doação de {i.codigo_do_material} {i.disciplina}')