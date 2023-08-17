/*
Este código utiliza programación dinámica para calcular la cantidad de formas en que la rana puede cruzar el río.
*/
using System;

class Program
{
    static int CountFrogWays(int rocks)
    {
        if (rocks <= 0)
            return 0;
        else if (rocks == 1)
            return 1;
        else if (rocks == 2)
            return 2;
        else if (rocks == 3)
            return 4;

        int[] ways = new int[rocks + 1];
        ways[1] = 1;
        ways[2] = 2;
        ways[3] = 4;

        for (int i = 4; i <= rocks; i++)
            ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3];

        return ways[rocks];
    }

    static void Main(string[] args)
    {
        int numRocks = 3;
        int totalWays = CountFrogWays(numRocks);
        Console.WriteLine($"La rana puede cruzar el río de {numRocks} rocas de {totalWays} formas distintas.");
    }
}