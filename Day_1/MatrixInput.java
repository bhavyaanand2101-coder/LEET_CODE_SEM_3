package Day_1;

import java.util.Scanner;

public class MatrixInput {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Taking number of rows and columns
        System.out.print("Enter rows: ");
        int r = sc.nextInt();

        System.out.print("Enter columns: ");
        int c = sc.nextInt();

        // Creating 2D array
        int[][] arr = new int[r][c];

        // Taking matrix input
        System.out.println("Enter matrix elements:");

        for (int i = 0; i < r; i++) {

            for (int j = 0; j < c; j++) {

                int temp = sc.nextInt();
                arr[i][j] = temp;
            }
        }

        // Printing the matrix
        System.out.println("Matrix is:");

        for (int i = 0; i < r; i++) {

            for (int j = 0; j < c; j++) {

                System.out.print(arr[i][j] + " ");
            }

            System.out.println();
        }

        sc.close();
    }
}
