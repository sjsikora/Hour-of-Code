package classes.pieces;
import classes.Board;

public class Knight extends Piece {

    public Knight(Board Board, boolean isWhite, int r, int f) {
        super(Board, isWhite, r, f);
    }

    public boolean move(int r, int f) {
        return true;
    }


    @Override
    public char getSymbol() {
        return 'k';
    }

    @Override
    public int[][] legalMoves() {

        int upOrDown = this.isWhite() ? 1 : -1;

        int[] aboveRight = {getR() + 1, getF() + 2}
        







    }
}
