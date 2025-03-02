'''

Objects:
    1) PieceType -> Enum = {O, X}, it can be extended
    2) Board -> has size and PLayingPiece
    3) Player -> has name, PieceType
    4) Game -> has PLayer, Board

Clearification:
    PieceType should be extendable, so in future if new pece is added and any new functionality is added then it is possible.
    Board -> size should be dynamic.
    Player -> N number of player can be possible. 

    
Game:
    Has -> Board, PLayers
    First intialize the game:
            -> create players
            -> create board
    Start Game:
        -> take first player for players list.
                -> get free cell -> if no free cell then it is tie so no winner.
                -> ask player for the position, row, col
                -> addPiece -> row, col, player.piece
                    -> piecenot added then addplayer again in queue in starting so he can enter correct possition.
                -> if added then move current playeri n last.
                -> check if the current is winner.
                if winner then return player name.
                

'''