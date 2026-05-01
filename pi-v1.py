# Aplicativo web para doação e reaproveitamento de materiais 

lista_alunos = []
lista_materiais_doados = []
lista_doacoes_realizadas = []


class Aluno:
  def __init__(self, matricula, nome, *serie, turma, ensino_medio):
    self.matricula = str(matricula)
    self.nome = str(nome)
    self.serie = serie
    self.turma = str(turma).upper()
    self.ensino_medio = str(ensino_medio).lower()
    lista_alunos.append(self)
    print(f'Aluno {nome} cadastrado com sucesso')
    
  def exibir_aluno(self, matricula, nome, *serie):
    self.matricula = str(matricula)
    self.nome = str(nome)
    self.serie = int(serie)
    print(f'N° Matrícula: {matricula}. \nNome: {nome} \nSérie: {serie}ª Turma: {self.turma} \nEnsino Médio: {self.ensino_medio}')
      
  def realizou_doacao(self, nome_do_aluno_doador, *serie, codigo_do_material):
    self.nome_do_aluno = str(nome_do_aluno_doador)
    self.serie = int(serie)
    self.material = str(codigo_do_material)
    lista_materiais_doados.append(self)
    print('Doação Realizada')


class Material:
  def __init__(self, codigo_do_material, serie, disciplina):
    self.codigo_do_material = str(codigo_do_material)
    self.serie = str(serie)
    self.disciplina = str(disciplina)


class Doacao:
  def __ini__(self, nome_do_aluno_doador, *serie, codigo_do_material):
    self.nome_do_aluno_doador = str(nome_do_aluno_doador)
    self.serie = int(serie)
    self.codigo_do_material = str(codigo_do_material)
    lista_doacoes_realizadas.append(self)
    print(f'O Aluno {nome_do_aluno_doador} Realizou doação')
  
  def recebeu(self, nome_do_aluno_recebedor, *serie, codigo_do_material):
    self.nome_do_aluno_recebedor = str(nome_do_aluno_recebedor)
    self.serie = int(serie)
    self.codigo_do_material = str(codigo_do_material)
    print(f'O Aluno {nome_do_aluno_recebedor} recebeu o material')
