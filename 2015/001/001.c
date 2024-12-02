#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int ac, char **av)
{
    char *input = NULL;
    int floor = 0;
    int i = 0;
    int position = 0;

    if (ac != 2)
    {
        printf ("Pleace enter the directions\n");
        return (0);
    }
    size_t length = strlen(av[1]);
    input = (char *)malloc((length + 1) * sizeof(char));
    if (input == NULL)
    {
        printf("Memory allocation failed!\n");
        return (1);
    }
    strcpy(input, av[1]);
    // printf ("Input: %s\n\n", input);

    while (i != length)
    {
        if (input[i] == '(')
            floor++;
        else if (input[i] == ')')
            floor--;
        if (floor < 0 && position == 0)
            position = i;
        i++;
    }
    printf("Current floor number is: %i\n", floor);
    printf ("Position: %i\n", position + 1);
    free (input);
    return (0);
}