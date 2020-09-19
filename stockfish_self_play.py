import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\ishaa\Desktop\chess_engine\stockfish-11-win\Windows\stockfish_20011801_x64.exe')

board = chess.Board()
moves = 0
while ((not board.is_game_over()) and moves<10):
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(result.move)
    print()
    print(board)
    print()
    moves+=1

engine.quit()
