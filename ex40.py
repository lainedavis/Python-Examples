
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

	def suck_my_dick(self):
		for element in self.lyrics:
			print(element+' - suck my dick')

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

twinkle = Song(["twinkle twinkle little star",
				"how i wonder what you are"])

happy_bday.sing_me_a_song()
happy_bday.suck_my_dick()
bulls_on_parade.sing_me_a_song()
twinkle.suck_my_dick()