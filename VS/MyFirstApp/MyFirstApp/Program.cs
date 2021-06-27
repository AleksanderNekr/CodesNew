using System;
using System.Linq;

namespace MyFirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            int[] values = { 1, 2, 3, 4, 5 };
            var sumVal = values.Aggregate(0, (sum, value) => sum + value);
            Console.WriteLine(sumVal);
            Array.ForEach(values, x => Console.Write($"{x} "));
            var valLst = values.ToList();
            Console.WriteLine();
            valLst.ForEach(x => Console.Write($"{x} "));
        }
    }
}
