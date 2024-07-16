package 문방구패턴맞추기게임;

import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class UserSolution {

    private static final int UP = 0;
    private static final int RIGHT = 1;
    private static final int DOWN = 2;
    private static final int LEFT = 3;

    // Main API:
    // Solution.swap(int dir)

    private static int[][] directions = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    private boolean[][] puzzled;
    private Point emptyPoint;

    class Point {
        int row;
        int col;

        Point(int row, int col) {
            this.row = row;
            this.col = col;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Point point = (Point) obj;
            return row == point.row && col == point.col;
        }

        @Override
        public int hashCode() {
            return 31 * row + col;
        }
    }

    public UserSolution() {
        puzzled = new boolean[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                puzzled[i][j] = false;
            }
        }
    }

    public void solve(int[][] board, int[][] pattern, int callCntLimit) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == 0) {
                    emptyPoint = new Point(i, j);
                }
            }
        }

        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                puzzleOnePart(board, pattern[i - 1][j - 1], i, j);
                puzzled[i][j] = true;
            }
        }
    }

    public void puzzleOnePart(int[][] board, int targetColor, int targetRow, int targetCol) {
        List<Point> pointSequence = getPointSequence(board, targetColor, targetRow, targetCol);

        for (Point point : pointSequence) {
            move(point, targetRow, targetCol);
            targetRow = point.row;
            targetCol = point.col;
        }

        // 마지막에 target 위치로 한번 더 스왑
        move(new Point(targetRow, targetCol), targetRow, targetCol);
    }

    public List<Point> getPointSequence(int[][] board, int targetColor, int targetRow, int targetCol) {
        List<Point> result = new ArrayList<>();

        Deque<Point> deq = new LinkedList<>();
        Map<Point, Point> parentMap = new HashMap<>();
        boolean[][] visited = new boolean[5][5];

        visited[emptyPoint.row][emptyPoint.col] = true;
        deq.add(emptyPoint);

        Point targetPoint = null;

        while (!deq.isEmpty()) {
            Point current = deq.poll();
            if (board[current.row][current.col] == targetColor && !puzzled[current.row][current.col]) {
                targetPoint = current;
                break;
            }

            for (int[] direction : directions) {
                int newRow = current.row + direction[0];
                int newCol = current.col + direction[1];

                if (0 <= newRow && newRow < 5 && 0 <= newCol && newCol < 5 && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    Point nextPoint = new Point(newRow, newCol);
                    deq.add(nextPoint);
                    parentMap.put(nextPoint, current);
                }
            }
        }

        if (targetPoint != null) {
            Point current = targetPoint;
            while (current != null) {
                result.add(0, current);
                current = parentMap.get(current);
            }
        }

        return result;
    }

    private void move(Point point, int targetRow, int targetCol) {
        List<Point> path = getPointSequence(new int[5][5], 0, point.row, point.col);

        for (Point p : path) {
            int direction = getDirection(emptyPoint, p);
            Solution.swap(direction);
            emptyPoint = p;
        }

        Point currPoint = new Point(targetRow, targetCol);
        int finalDirection = getDirection(emptyPoint, currPoint);
        Solution.swap(finalDirection);
        emptyPoint = currPoint;
    }

    private int getDirection(Point from, Point to) {
        if (from.row == to.row) {
            return from.col < to.col ? RIGHT : LEFT;
        } else {
            return from.row < to.row ? DOWN : UP;
        }
    }
}
