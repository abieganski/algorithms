// Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

class MissingIntInArray
{

    public void Run()
    {
        int[] a = { 1, 4, 2, -1, 0, 9, -4, 2, 2, 5 };

        for (int i = 0; i < a.Length; i++)
        {

            a[i]++;
        }

        Console.Write(a[0]);
    }
}