using System;

namespace StarshipTakeOff
{
    class StarshipTakeOffProgram
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            int gravity = random.Next(1, 21);
            int weight = random.Next(1, 41);
            int requiredForce = gravity * weight;

            Console.Clear();
            Console.WriteLine("STARSHIP TAKE-OFF");
            Console.WriteLine("Gravity = {0:D}", gravity);
            Console.WriteLine("TYPE IN FORCE");

            for (int counter = 1; counter <= 10; counter++)
            {
                if (counter != 1)
                {
                    Console.WriteLine(", TRY AGAIN");
                }

                int force = Convert.ToInt32(Console.ReadLine());

                if (force > requiredForce)
                {
                    Console.Write("TOO HIGH");
                }
                else if (force < requiredForce)
                {
                    Console.Write("TOO LOW");
                }
                else
                {
                    SuccessfulTakeoff();
                    return;
                }
            }

            FailedTakeoff();
        }

        static void FailedTakeoff()
        {
            Console.WriteLine();
            Console.WriteLine("YOU FAILED =");
            Console.WriteLine("THE ALIENS GOT YOU");
            Console.WriteLine();
            Console.WriteLine("Press enter to exit.");
            Console.ReadLine();
            Environment.Exit(0);
        }

        static void SuccessfulTakeoff()
        {
            Console.WriteLine("GOOD TAKE OFF");
            Console.WriteLine();
            Console.WriteLine("Press enter to exit.");
            Console.ReadLine();
            Environment.Exit(0);
        }
    }
}
