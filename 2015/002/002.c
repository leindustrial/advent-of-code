#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main (void)
{
    int file;
    char buffer[100];
    ssize_t bytes_read;
    int i = 0;

    file = open("example.txt", O_RDONLY);
    if (file == -1)
        return 1;
    

    return (0);
}