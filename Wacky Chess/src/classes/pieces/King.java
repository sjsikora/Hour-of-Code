package classes.pieces;
import classes.Board;

public class King extends Piece {

    private boolean hasMoved = false;
    private boolean checked = false;

    public King(Board Board, boolean isWhite, int r, int f) {
        super(Board, isWhite, r, f);
    }

    public boolean move(int r, int f) {
        this.hasMoved = true;

        return true;
    }


    @Override
    public char getSymbol() {
        return 'K';
    }
}
