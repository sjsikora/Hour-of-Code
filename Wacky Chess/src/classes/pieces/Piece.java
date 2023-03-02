package classes.pieces;
import classes.Board;

public abstract class Piece {

    private Board myBoard;
    private boolean isWhite;
    private boolean alive;
    private int r;
    private int f;

    public Piece(Board myBoard, boolean isWhite, int r, int f) {
        this.myBoard = myBoard;
        this.isWhite = isWhite;
        this.r = r;
        this.f = f;
        alive = true;
    }

    public Board getMyBoard() {
        return this.myBoard;
    }

    public void setMyBoard(Board myBoard) {
        this.myBoard = myBoard;
    }

    public boolean isWhite() {
        return this.isWhite;
    }

    public boolean isAlive() {
        return this.alive;
    }

    public boolean getAlive() {
        return this.alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }

    public int getR() {
        return this.r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getF() {
        return this.f;
    }

    public void setF(int f) {
        this.f = f;
    }
    
    
    public abstract boolean move(int x, int y);
    public abstract char getSymbol();
    public abstract int[][] legalMoves();

}
