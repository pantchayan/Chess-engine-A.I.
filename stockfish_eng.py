from stockfish import Stockfish
import chess

board = chess.Board()

stockfish = Stockfish(r'C:\Users\ishaa\Desktop\chess_engine\stockfish-11-win\Windows\stockfish_20011801_x64.exe')
stockfish.set_position(['e2e4', 'e7e6'])

print(stockfish.get_best_move())
print(stockfish.is_move_correct('a2a3'))
