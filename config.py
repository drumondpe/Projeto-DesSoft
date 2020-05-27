'''
Módulo de configurações do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

class Config():

	def __init__(self):

		self.titulo = 'Joguinho do Come-Come'
		self.largura_tela = 560
		self.altura_tela = 620
		self.FPS = 60

		self.velocidade = 5	# pixels/ciclo

		self.cores = Cores()
		self.textos = Textos()


class Cores():

	def __init__(self):

		self.titulo = (200, 205, 70)
		self.fundo = (0, 0, 0)
		self.nomes = (200, 90, 210)

		self.preto = (0, 0, 0)


class Textos():

	def __init__(self):

		self.fonte = 'Futura ZBlk BT'
		self.tamanho_grande = 50
		self.tamanho_pequeno = 30



CONFIG = {
	'titulo': 'Joguinho do Come-Come'.upper(),
	'largura': 560,
	'altura': 620,
	'fps': 60,
	'cores': {
		'titulo': (200, 205, 70),
		'nomes': (200, 90, 210),
		'fundo': (0, 0, 0),
		'preto': (0, 0, 0),
		'branco': (255, 255, 255),
		'rosa': (255, 0, 255),
		'vermelho': (255, 0, 0),
		'verde': (0, 255, 0),
		'azul': (0, 0, 255),
		'amarelo': (255, 255, 0)
	},
	'fonte grande': 50,
	'fonte pequena': 30
}