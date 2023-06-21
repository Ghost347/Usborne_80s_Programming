#include <iostream>
#include <random>
#include <chrono>

void successful_takeoff()
{
  std::cout << "GOOD TAKEOFF!" << std::endl;
  std::exit(0);
}

int main()
{
  // Initialize random number generator
  std::mt19937 gen(std::chrono::system_clock::now().time_since_epoch().count());
  std::uniform_int_distribution<int> gravityDist(1, 20);
  std::uniform_int_distribution<int> weightDist(1, 40);

  std::cout << "STARSHIP TAKEOFF" << std::endl;

  int gravity = gravityDist(gen);
  int weight = weightDist(gen);
  int requiredForce = gravity * weight;

  std::cout << "GRAVITY: " << gravity << std::endl;
  std::cout << "ENTER FORCE: ";

  for (int i = 0; i < 10; ++i)
  {
    int force = 0;
    std::cin >> force;

    if (!std::cin)
    {
      std::cout << "INVALID INPUT" << std::endl;
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      i--;
      continue;
    }

    if (force > requiredForce)
    {
      std::cout << "TOO HIGH" << std::endl;
    }
    else if (force < requiredForce)
    {
      std::cout << "TOO LOW" << std::endl;
    }
    else
    {
      successful_takeoff();
    }

    if (i != 9)
    {
      std::cout << ", TRY AGAIN" << std::endl;
      std::cout << "ENTER FORCE: ";
    }
  }

  std::cout << "YOU FAILED" << std::endl;
  std::cout << "THE ALIENS GOT YOU" << std::endl;

  std::exit(0);
}
