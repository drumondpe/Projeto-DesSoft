'''
Módulo de configurações do jogo
'''

class Settings():
	''' Classe de configurações '''

	def __init__(self):
		''' Construtor da classe Settings '''

		# configurações de tile
		self.tile_size = 25
		
		# configurações da janela
		self.screen_width = 24 * self.tile_size
		self.screen_height = 28 * self.tile_size
		self.caption = 'Joguinho do Come-Come'

		# configuações do clock
		self.fps = 60

		# sub-configurações
		self.texts = Settings.Texts()
		self.colors = Settings.Colors()


	class Texts():
		''' Configurações do menu do jogo '''

		def __init__(self):
			self.font = 'Futura ZBlk BT'
			self.large_fontsize = 50
			self.small_fontsize = 30
			self.title = 'Joguinho do Come-Come'


	class Colors():
		''' Configurações de cores '''

		def __init__(self):
			self.menu_button = (255, 40, 255)
			self.title = (200, 205, 70)
			self.names = (200, 90, 210)
			self.black = (0, 0, 0)
			self.bg = self.black



