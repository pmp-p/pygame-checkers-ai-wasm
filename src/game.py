from operator import xor
from .board import Board
from .move import Move, generate_moves


class Game:
    def __init__(
        self,
        red=None,
        blue=None,
    ):
        self.board = Board()
        self.moves: list[Move] = []
        self.reset_correct_moves()

        self.red = red
        self.blue = blue

    def play_move(self, index: int):
        """Play a move on the Board

        Args:
            index (int): the index of the move
        """
        move = self.moves[index]
        move.play(self.board)
        self.reset_correct_moves()

    def find_move_index(self, start: int, end: int) -> int:
        """Find the index for the  move based on the start and end
        this is possible only because all the moves are unique

        Args:
            start (int): the start index
            end (int): the end index

        Raises:
            Exception: this is when the position is not there

        Returns:
            int: the index of the move in the moves list
        """
        for i, move in enumerate(self.moves):
            if move.start == start and move.end == end:
                return i

        raise Exception(f"Move not Present with start and end: {(start, end)}")

    def reset_correct_moves(self):
        """Resets the game instances correct move
        based on the position
        """
        self.moves = generate_moves(self.board)