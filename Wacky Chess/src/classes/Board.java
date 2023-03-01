package classes;
import classes.pieces.*;

public class Board {
    
    private Piece[][] pieceArray;
    private boolean isWhiteTurn = true;

    public Board() {
        pieceArray = new Piece[8][8];
    }

    public void addPiece(Piece p, int r, int f) {
        pieceArray[r][f] = p;
    }

    public void startGame() {

        System.out.println("Starting game...");
        // Add pieces to the board
        for (int j = 0; j < 2; j++) {

            int rankToAdd = 0;
            int pawnRank = 1;
            boolean isWhite = false;

            if (j == 0) {
                pawnRank = 6;
                rankToAdd = 7;
                isWhite = true;
            }

            addPiece(new Rook(this, isWhite, rankToAdd, 0), rankToAdd, 0);
            addPiece(new Knight(this, isWhite, rankToAdd, 1), rankToAdd, 1);
            addPiece(new Bishop(this, isWhite, rankToAdd, 2), rankToAdd, 1);
            addPiece(new Queen(this, isWhite, rankToAdd, 3), rankToAdd, 3);
            addPiece(new King(this, isWhite, rankToAdd, 4), rankToAdd, 4);
            addPiece(new Bishop(this, isWhite, rankToAdd, 5), rankToAdd, 5);
            addPiece(new Knight(this, isWhite, rankToAdd, 6), rankToAdd, 6);
            addPiece(new Rook(this, isWhite, rankToAdd, 7), rankToAdd, 7);
    
            for (int i = 0; i < 8; i++) {
                addPiece(new Pawn(this, isWhite, pawnRank, i), pawnRank, i);
            }

        }
        System.out.println("Game started!");

    }

    public Piece getPiece(int r, int f) {
        return pieceArray[r][f];
    }


    public String toString() {
        String boardString = "";
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (pieceArray[i][j] == null) {
                    boardString += "| |";
                } else {
                    boardString += "|" + pieceArray[i][j].getSymbol() + "|";
                }
            }
            boardString += "\n";
        }

        return boardString;
    }




}
