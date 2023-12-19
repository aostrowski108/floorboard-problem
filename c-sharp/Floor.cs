using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;


namespace FloorProblem
{
    class Floor
    {
        static void Main(string[] args)
        {
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();
            var rows = GenerateRows(32); 

            var prefixSumsList = new List<HashSet<long>>();
            foreach (var row in rows)
            {
                var prefixSums = GeneratePrefixSum(row);
                prefixSumsList.Add(prefixSums);
            }

            var conflictList = GenerateConflictList(prefixSumsList);

            long totalWays = CalculateTotalWays(conflictList, 10);
            stopwatch.Stop();
            long elapsedMilliseconds = stopwatch.ElapsedMilliseconds;
            Console.WriteLine($"Total ways to build the floor: {totalWays}");
            Console.WriteLine($"Elapsed Time: {elapsedMilliseconds} milliseconds");
        }
        static List<List<long>> GenerateRows(long width)
        {
            if (width == 0)
            {
                return new List<List<long>> { new List<long>() };
            }
            if (width == 1)
            {
                return new List<List<long>>();
            }

            List<List<long>> rows = new List<List<long>>();

            if (width - 2 >= 0)
            {
                foreach (var row in GenerateRows(width - 2))
                {
                    var newRow = new List<long>(row);
                    newRow.Add(2);
                    rows.Add(newRow);
                }
            }

            if (width - 3 >= 0)
            {
                foreach (var row in GenerateRows(width - 3))
                {
                    var newRow = new List<long>(row);
                    newRow.Add(3);
                    rows.Add(newRow);
                }
            }

            return rows;
        }
        static HashSet<long> GeneratePrefixSum(List<long> row)
        {
            HashSet<long> prefixSum = new HashSet<long>();
            long prefix = 0;

            for (int i = 0; i < row.Count - 1; i++)
            {
                prefix += row[i];
                prefixSum.Add(prefix);
            }

            return prefixSum;
        }
        static List<List<long>> GenerateConflictList(List<HashSet<long>> prefixSumsList)
        {
            var conflictList = new List<List<long>>();

            for (int i = 0; i < prefixSumsList.Count; i++)
            {
                var conflicts = new List<long>();
                for (int j = 0; j < prefixSumsList.Count; j++)
                {
                    if (i != j && !prefixSumsList[i].Overlaps(prefixSumsList[j]))
                    {
                        conflicts.Add(j);
                    }
                }
                conflictList.Add(conflicts);
            }

            return conflictList;
        }
        static long CalculateTotalWays(List<List<long>> conflictList, long height)
        {
            int numRows = conflictList.Count;
            long[] possibleWays = new long[numRows];
            Array.Fill(possibleWays, 1L);  // Base case: 1 way to build the floor with 1 row

            for (int h = 1; h < height; h++)  // Loop index can stay as int if height will not exceed int.MaxValue
            {
                long[] newPossibleWays = new long[numRows];
                for (int i = 0; i < numRows; i++)  // Loop index can stay as int since numRows is based on conflictList.Count
                {
                    foreach (long j in conflictList[i])
                    {
                        newPossibleWays[j] += possibleWays[i];
                    }
                }
                possibleWays = newPossibleWays;
            }

            long totalWays = 0;
            foreach (long way in possibleWays)
            {
                totalWays += way;
            }
            return totalWays;
        }

    }
}
