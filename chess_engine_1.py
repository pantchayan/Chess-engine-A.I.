import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\ishaa\Desktop\chess_engine\stockfish-11-win\Windows\stockfish_20011801_x64.exe')

white = 1
moves = 0
while((not board.is_game_over()) and moves<10):
    if(white):
        move = input("White to move : ")
        board.push_san(move)
        white ^= 1
    else:
        result = engine.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)
        white ^= 1
    moves+=1
    print(board)
engine.quit()
