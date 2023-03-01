package classes.pieces;
import classes.Board;

public class Bishop extends Piece {

    public Bishop(Board Board, boolean isWhite, int r, int f) {
        super(Board, isWhite, r, f);
    }

    public boolean move(int r, int f) {
        return true;
    }

    @Override
    public char getSymbol() {
        return 'B';
    }


}