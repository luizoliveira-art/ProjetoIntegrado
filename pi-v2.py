# Aplicativo web para doação e reaproveitamento de materiais

if 'lista_alunos_geral' not in locals():
  lista_alunos_geral = []
if 'lista_alunos_ensino_fundamental' not in locals():
  lista_alunos_ensino_fundamental = []
if 'lista_alunos_ensino_medio' not in locals():
  lista_alunos_ensino_medio = []  

if 'lista_materiais' not in locals():
  lista_materiais = []
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
  def __init__(self, matricula, nome, serie, turma, ensino_medio):
    self.matricula = str(matricula)
    self.nome = str(nome)
    self.serie = serie
    self.turma = str(turma).upper()
    self.ensino_medio = str(ensino_medio).lower()
    if not any(aluno.matricula == self.matricula for aluno in lista_alunos_geral):
      lista_alunos_geral.append(self)
      print(f'Aluno {nome} cadastrado com sucesso\n')
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      if 'lista_alunos_ensino_medio' not in locals():
        lista_alunos_ensino_medio = []
      lista_alunos_ensino_medio.append(self)
      print(f'\nAluno {nome} do Ensino Médio cadastrado com sucesso\n')
    else:
      print(f'\nAluno {nome} do Ensino Fundamental cadastrado com sucesso\n')

  def exibir(self):
    print(f'\nN° Matrícula: {self.matricula} - Nome: {self.nome} - Série: {self.serie}ª - Turma: {self.turma} - Ensino Médio: {self.ensino_medio}\n')


class Material:
  def __init__(self, codigo_do_material, serie, disciplina, ensino_medio, obs):
    self.codigo_do_material = str(codigo_do_material)
    self.serie = str(serie)
    self.disciplina = str(disciplina)
    self.ensino_medio = str(ensino_medio).lower()
    self.obs = str(obs)
    lista_materiais.append(self)
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio.append(self)
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental.append(self)

  def exibir(self):
    print(f'Código do Material: {self.codigo_do_material} - Série: {self.serie} - Disciplina: {self.disciplina} - Ensino  Médio: {self.ensino_medio}\n')


class Doacao:
  def __init__(self, nome_do_aluno_doador, serie, codigo_do_material, ensino_medio, obs):
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    self.serie = int(serie)
    self.codigo_do_material = str(codigo_do_material)
    self.ensino_medio = str(ensino_medio).lower()
    self.obs = str(obs)

  def realizou_doacao(self, nome_do_aluno_doador, serie, codigo_do_material, ensino_medio, obs):
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    if self.nome_do_aluno_doador not in lista_alunos_geral:
      print('Aluno não cadastrado')
    self.codigo_do_material = str(codigo_do_material)
    self.serie = str(serie)
    lista_doacoes_geral.append(self)
    self.ensino_medio = str(ensino_medio).lower()
    self.obs = str(obs)
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio_doados.append(self)
      print(f'O Aluno {nome_do_aluno_doador}do Ensino Médio, Realizou doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental_doados.append(self)
      print(f'O Aluno {nome_do_aluno_doador}do Ensino Fundamental, Realizou doação\n')
    

  def exibir(self):
    print(f'O Aluno {self.nome_do_aluno_doador} Realizou doação\n')

  def recebeu_doacao(self, nome_do_aluno_recebedor, serie, codigo_do_material, ensino_medio, obs):
    self.nome_do_aluno_recebedor = str(nome_do_aluno_recebedor)
    if self.nome_do_aluno_recebedor not in lista_alunos_geral:
      print('Aluno não cadastrado')
    self.serie = str(serie)
    self.codigo_do_material = str(codigo_do_material)
    lista_doacoes_geral.append(self)
    print(f'O Aluno {nome_do_aluno_recebedor} recebeu o material doado\n')
    self.obs = str(obs)
    self.ensino_medio = str(ensino_medio).lower()
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio_recebidos.append(self)
      print(f'O Aluno {nome_do_aluno_recebedor}do Ensino Médio, Recebeu doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental_doados.append(self)
      print(f'O Aluno {nome_do_aluno_recebedor}do Ensino Fundamental, Recebeu doação\n')

# testes

a1 = Aluno('123456789', 'Luiz', 2, 'a', 's')
a1.exibir()

a2 = Aluno('987654321', 'Felipe', 2, 'a', 'S')
a2.exibir()

a3 = Aluno('147258369', 'Abner', 7, 'a', 'n')
a3.exibir()

a4 = Aluno('159753456', 'Marcus', 7, 'b', 'N')
a4.exibir()

print('\nLista de alunos Geral')
for i in lista_alunos_geral:
  print(f' Aluno {i.nome} {i.serie}°')


print('\nLista de Materiais')
for i in lista_materiais:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}° - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais Fundamental')
for i in lista_materiais_fundamental:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}° - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais do Ensino Médio\n')
for i in lista_materiais_ensino_medio:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}° - Ensino Médio? {i.ensino_medio}')


m1 = Material('123456789', 2, 'Matemática', 'S', ' ')
m1.exibir()

m2 = Material('987654321', 2, 'Português', 's', ' ')
m2.exibir()

m3 = Material('147258369', 7, 'Matemática', 'N', ' ')
m3.exibir()

m4 = Material('159753456', 7, 'Português', 'n', ' ')
m4.exibir()

print('\nLista de Materiais')
for i in lista_materiais:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais Fundamental')
for i in lista_materiais_fundamental:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais do Ensino Médio')
for i in lista_materiais_ensino_medio:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')
