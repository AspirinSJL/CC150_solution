// Reverse a string word-wise,
//   different from the original question

#include <stdio.h>

void reverse_letter(char* start, char* end)
{
    while (start < end)
    {
        char temp = *start;
        *start++ = *end;
        *end-- = temp;
    }
}

void reverse(char* str)
{
    if (!str)
        return;
    
    // loop invariant: [start, end) will be reversed as a word
    char* start = str;
    char* end = start;
    while (1)
    {
        if (*end != ' ' && *end != '\0')
        {
            end++;
        }
        else if (*end == ' ')
        {
            if (start < end)
            {
                reverse_letter(start, end - 1);
            }
            end++;
            start = end;
        }
        else if (*end == '\0')
        {
            if (start < end)
            {
                reverse_letter(start, end - 1);
            }
            reverse_letter(str, end - 1);
            break;
        }
    }
}

int main(int argc, char const *argv[])
{
    char str[20] = "   a     test case\0";
    printf("%s\n", str);
    reverse(str);
    printf("%s\n", str);
    return 0;
}