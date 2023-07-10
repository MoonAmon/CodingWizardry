#include <stdbool.h>

bool better_than_average(const int class_points[], int class_size, int your_points) {
    int sum = 0;
    float media = 0;

    for (int i = 0; i < class_size; i++)
    {
        sum += class_points[i];
    }
    media = sum / class_size;

    if (media < your_points)
    {
        return true;
    } 
    
  return false;
}