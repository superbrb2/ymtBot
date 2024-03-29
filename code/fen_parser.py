from itertools import chain
import re

class ChessPositionToFEN:
	def __init__(self, position):
		self.position = position

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
		
		return fen



class FenToChessPosition():
	def __init__(self, fen_str):
		self.fen_str = fen_str

	def parse(self):
		ranks = self.fen_str.split(" ")[0].split("/")
		pieces_on_all_ranks = [self.parse_rank(rank) for rank in ranks]
		return pieces_on_all_ranks

	def parse_rank(self, rank):
		rank_re = re.compile("(\d	|[kqbnrpKQBNRP])")
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

