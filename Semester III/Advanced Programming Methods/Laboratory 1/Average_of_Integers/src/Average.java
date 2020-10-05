//  Laboratory 1:
//  Please write a Java program that computes the average of all integer numbers given
//  as command-line parameters
import java.util.Scanner;
import java.util.Arrays;
public class Average {
    public static double get_average(int[] array_of_numbers)
        /*
    Function which computes the average of the elements from array_of_numbers
    Input: array_of_numbers- an array which contains all inputs which was given
           as command-line parameters
    Output: average- average of all integer numbers
        */
    {
        int sum_of_numbers=0;
        double average;
        for (int index : array_of_numbers) {
            sum_of_numbers += index;
        }
        average=(double)sum_of_numbers/array_of_numbers.length;
        return average;
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Give the numbers: ");
        String[] data = input.nextLine().split(" ");
        int[] array_of_numbers = new int[data.length];
        for (int index = 0; index < data.length; index++) {
            array_of_numbers[index] = Integer.parseInt(data[index]);
        }
        double average_result=get_average(array_of_numbers);
        System.out.println("Numbers: " + Arrays.toString(array_of_numbers));
        System.out.println("Average of the numbers: " + average_result);
    }
}
