package classes.pieces;
import classes.Board;

public class Pawn extends Piece {

    private boolean hasMoved = false;

    public Pawn(Board Board, boolean isWhite, int r, int f) {
        super(Board, isWhite, r, f);
    }

    @Override
    public int[][] legalMoves() {

        int upOrDown = this.isWhite() ? 1 : -1;
        int numLegalMoves = 0;
        boolean[] legalMovesBoolean = new boolean[4];

        Piece above = getMyBoard().getPiece(getR(), getF() + upOrDown);
        Piece above2 = getMyBoard().getPiece(getR(), getF() + (2 * upOrDown));
        Piece aboveLeft = getMyBoard().getPiece(getR() - upOrDown, getF() + upOrDown);
        Piece aboveRight = getMyBoard().getPiece(getR() + upOrDown, getF() + upOrDown);

        if (above == null) {
            numLegalMoves++;
            legalMovesBoolean[0] = true;
        }
        if (above2 == null && !hasMoved) {
            numLegalMoves++;
            legalMovesBoolean[1] = true;
        }
        if (aboveLeft != null && (aboveLeft.isWhite() != isWhite())) {
            numLegalMoves++;
            legalMovesBoolean[2] = true;
        }
        if (aboveRight != null && aboveRight.isWhite() != isWhite()) {
            numLegalMoves++;
            legalMovesBoolean[3] = true;
        }

        int[][] legalMoves = new int[numLegalMoves][2];

        int rowNum = 0;

        if (legalMovesBoolean[0]) {
            legalMoves[rowNum][0] = getR();
            legalMoves[rowNum][1] = getF() + upOrDown;
            rowNum++;
        }
        if (legalMovesBoolean[1]) {
            legalMoves[rowNum][0] = getR();
            legalMoves[rowNum][1] = getF() + (2 * upOrDown);
            rowNum++;
        }
        if (legalMovesBoolean[2]) {
            legalMoves[rowNum][0] = getR() - upOrDown;
            legalMoves[rowNum][1] = getF() + upOrDown;
            rowNum++;
        }
        if (legalMovesBoolean[3]) {
            legalMoves[rowNum][0] = getR() + upOrDown;
            legalMoves[rowNum][1] = getF() + upOrDown;
            rowNum++;
        }

        return legalMoves;

    }

    public boolean move(int r, int f) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public char getSymbol() {
        return 'p';
    }
}
