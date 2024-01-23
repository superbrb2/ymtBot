from unittest import TestCase
from itertools import chain
import re

class ChessPositionToFEN:
	def __init__(self, position, white_to_move, enpassant_pos, castling):
		self.position = position
		self.white_to_move = white_to_move
		self.enpassant_pos = enpassant_pos
		self.castling = castling

	def board_to_fen(self):
		fen = ''
		empty_count = 0

		for row in self.position:
			for square in row:
				if square.isdigit():
					empty_count += int(square)
				else:
					if empty_count:
						fen += str(empty_count)
						empty_count = 0
					fen += square

			if empty_count:
				fen += str(empty_count)
				empty_count = 0

			fen += '/'

		fen = fen[:-1]  
		
		# Player turn 
		if self.white_to_move == True:
			fen += ' w'
		else:
			fen += ' b'
		
		# castling turn
		fen += ' ' + self.castling
		
		# Enpassant location
		fen += ' ' + self.enpassant_pos
		
		return fen



class FenToChessPosition():
	def __init__(self, fen_str):
		self.fen_str = fen_str

	def parse(self):
		ranks = self.fen_str.split(" ")[0].split("/")
		ending = self.get_end()
		print(f'this is{ending}')
		pieces_on_all_ranks = [self.parse_rank(rank) for rank in ranks]
		return pieces_on_all_ranks
		# white_to_move, enpassant_pos, castling

	def get_end(self):
		fen_str = self.fen_str
		ending = ''
		for i in range(len(fen_str)):
			pass
		ending = ending[::-1]
		return ending

	def parse_rank(self, rank):
		rank_re = re.compile("(\d|[kqbnrpKQBNRP])")
		piece_tokens = rank_re.findall(rank)
		pieces = self.flatten(map(self.expand_or_noop, piece_tokens))
		return pieces

	def flatten(self, lst):
		return list(chain(*lst))

	def expand_or_noop(self, piece_str):
		piece_re = re.compile("([kqbnrpKQBNRP])")
		retval = ""
		if piece_re.match(piece_str):
			retval = piece_str
		else:
			retval = self.expand(piece_str)
		return retval

	def expand(self, num_str):
		return int(num_str)*" "

