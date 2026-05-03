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
  def __init__(self, matricula, nome, serie, turma, ensino_medio):
    self.matricula = str(matricula)
    if self.matricula not in lista_matriculas:
      raise ValueError('Matrícula não encontrada')
    self.nome = str(nome)
    self.serie = int(serie)
    self.turma = str(turma).upper()
    self.ensino_medio = str(ensino_medio).lower()
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_alunos_ensino_medio.append(self)
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_alunos_ensino_fundamental.append(self)

  def exibir(self):
    print(f'N° Matrícula: {self.matricula} - Nome: {self.nome} - Série: {self.serie}ª - Turma: {self.turma} - Ensino Médio: {self.ensino_medio}\n')

  def cadastrar(self, serie_antiga, repetente):
    self.serie_antiga = str(serie_antiga)
    self.repetente = str(repetente)
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      print(f'O aluno {self.nome} deve fazer o ano letivo, novamente')


class Material:
  def __init__(self, nome_do_aluno_dono, codigo_do_material, ensino_medio, serie, disciplina, obs):
    self.nome_do_aluno_dono = str(nome_do_aluno_dono)
    if self.nome_do_aluno_dono not in lista_alunos_geral:
      raise ValueError('Nome do aluno não encontrado')
    self.codigo_do_material = str(codigo_do_material)
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
    print(f'Código do Material: {self.codigo_do_material} - Série: {self.serie} - Disciplina: {self.disciplina} - Ensino  Médio: {self.ensino_medio}\n')


class Doacao:
  def __init__(self, ensino_medio, serie, disciplina, codigo_do_material):
    self.ensino_medio = str(ensino_medio).lower()
    self.serie = int(serie)
    if (self.serie > 3 and self.ensino_medio == 'sim') or (self.serie > 3 and self.ensino_medio == 's'):
      raise ValueError('Ensino Médio não possui + de 3 séries')
    self.disciplina = str(disciplina)
    self.codigo_do_material = str(codigo_do_material)
    if self.codigo_do_material not in lista_materiais_geral:
      raise ValueError("Material não encontrado na lista geral.")

  def realizou_doacao(self, nome_do_aluno_doador,  ensino_medio, serie, codigo_do_material, obs):
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    if self.nome_do_aluno_doador not in lista_alunos_geral:
      raise ValueError('Nome do aluno não encontrado na lista geral')
    self.codigo_do_material = str(codigo_do_material)
    if self.codigo_do_material not in lista_materiais_geral:
      raise ValueError('Código do material não encontrado')
    self.serie = str(serie)
    self.ensino_medio = str(ensino_medio).lower()
    if (self.serie > 3 and self.ensino_medio == 'sim') or (self.serie > 3 and self.ensino_medio == 's'):
      raise ValueError('Ensino Médio não possui + de 3 séries')
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
      lista_materiais_ensino_medio_doados.append(self)
      print(f'O Aluno {nome_do_aluno_doador} do Ensino Médio, Realizou doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
      lista_materiais_fundamental_doados.append(self)
      print(f'O Aluno {nome_do_aluno_doador} do Ensino Fundamental, Realizou doação\n')
    self.obs = str(obs)
    lista_doacoes_geral.append(self)

  def exibir_doador(self):
    print(f'O Aluno {self.nome_do_aluno_doador} Realizou doação do {self.codigo_do_material} {self.obs} de {self.disciplina}\n')
 
  def recebeu_doacao(self, nome_do_aluno_recebedor, serie_aluno_recebedor, ensino_medio, codigo_do_material, obs):
    self.nome_do_aluno_recebedor = str(nome_do_aluno_recebedor)
    if self.nome_do_aluno_recebedor not in lista_alunos_geral:
      raise ValueError('nome_do_aluno_recebedor não encontrado')
    self.serie_aluno_recebedor = str(serie_aluno_recebedor)
    self.ensino_medio = str(ensino_medio).lower()
    if self.ensino_medio == 's' or self.ensino_medio == 'sim':
        print(f'O Aluno {nome_do_aluno_recebedor} do Ensino Médio, Recebeu doação\n')
    elif self.ensino_medio == 'n' or self.ensino_medio == 'não':
        print(f'O Aluno {nome_do_aluno_recebedor} do Ensino Fundamental, Recebeu doação\n')
    self.codigo_do_material = str(codigo_do_material)
    if self.codigo_do_material not in lista_materiais_geral:
      raise ValueError('codigo_do_material não encontrado')
    self.obs = str(obs)
    lista_doacoes_geral.append(self)
    print(f'O Aluno {nome_do_aluno_recebedor} recebeu o material doado\n')
    
    
  def exibir_recebedor(self, matricula, nome_do_aluno_doador, nome_do_aluno_recebedor, serie_aluno_doador, codigo_do_material, ensino_medio, obs, serie_aluno_recebedor):
    self.matricula = str(matricula)
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    if self.nome_do_aluno_doador not in lista_alunos_geral:
      print('Aluno não cadastrado')
    self.nome_do_aluno_recebedor = str(nome_do_aluno_recebedor)
    if self.nome_do_aluno_recebedor not in lista_alunos_geral:
      raise ValueError('nome_do_aluno_recebedor não encontrado')
    self.serie_aluno_doador = str(serie_aluno_doador)
    self.codigo_do_material = str(codigo_do_material)
    self.serie_aluno_recebedor = str(serie_aluno_recebedor)
    self.ensino_medio = str(ensino_medio).lower()
    self.obs = str(obs)


# testes

print('\nLista de alunos Geral')
for i in lista_alunos_geral:
  print(f' Aluno {i.nome} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_alunos_geral) == 0:
  print('Lista Vazia\n')

a1 = Aluno('123456789', 'Luiz', 2, 'a', 'sim')
a1.exibir()

a2 = Aluno('987654321', 'Felipe', 2, 'a', 'Sim')
a2.exibir()

a3 = Aluno('147258369', 'Abner', 7, 'a', 'não')
a3.exibir()

a4 = Aluno('159753456', 'Marcus', 7, 'b', 'Não')
a4.exibir()

a5 = Aluno('789456123', 'Luiz', 3, 'b', 'SIM')
a5.exibir()

a6 = Aluno('748596123', 'Luan', 3, 'b', 'NÃO')
a6.exibir()

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
  

print('\nLista de Materiais')
for i in lista_materiais_geral:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}° - Ensino Médio? {i.ensino_medio}')
if len(lista_materiais_geral) == 0:
  print('Lista Vazia\n')


m1 = Material('1548625397', 2, 'Matemática', 'Sim', ' ')
m1.exibir()

m2 = Material('987654321', 2, 'Português', 'sim', ' ')
m2.exibir()

m3 = Material('147258369', 7, 'Matemática', 'Não', ' ')
m3.exibir()

m4 = Material('159753456', 7, 'Português', 'não', ' ')
m4.exibir()

m5 = Material('1548693207', 8, 'Português', 'NÃO', ' ')
m5.exibir()

m6 = Material('7485962310', 9, 'Geografia', 'SIM',  ' ')
m6.exibir()

m7 = Material('1548769320', 4, 'História', 'NÃO', 'Livro com perguntas')
m7.exibir()

print('\nLista de Materiais Geral')
for i in lista_materiais_geral:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais Fundamental')
for i in lista_materiais_fundamental:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')

print('\nLista de Materiais do Ensino Médio')
for i in lista_materiais_ensino_medio:
  print(f'{i.codigo_do_material} - {i.disciplina} - {i.serie}º - Ensino Médio? {i.ensino_medio}')
