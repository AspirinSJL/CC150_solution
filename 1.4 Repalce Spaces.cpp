#include <stdio.h>

void move_tail(char *first, int length)
{
    if (length > 0)
    {
        for (int i = length - 1; i >= 0; --i)
        {
            first[i + 2] = first[i];
        }
    }
}

void replace_spaces_forward(char *string, int length)
{
    for (int i = 0; i < length; ++i)
    {
        if (string[i] == ' ')
        {
            move_tail(string + i + 1, length - i - 1);
            string[i] = '%';
            string[i + 1] = '2';
            string[i + 2] = '0';
            i += 2;
            length += 2;
        }
    }
    // TODO: no effect?
//    string[length] = '\0';
}

void replace_spaces_backward(char *string, int length)
{
    int count_space = 0;
    for (int i = 0; i < length; ++i)
    {
        if (string[i] == ' ')
        {
            ++count_space;
        }
    }
    int new_length = length + count_space * 2;
    int dest = new_length;
    // TODO: no effect?
//    string[dest] = '\0';
    --dest;
    
    for (int i = length - 1; i >= 0; --i)
    {
        if (string[i] == ' ')
        {
            string[dest--] = '0';
            string[dest--] = '2';
            string[dest--] = '%';
        }
        else
        {
            string[dest--] = string[i];
        }
    }
}

int main(int argc, char const *argv[])
{
    char string1[100] = "a test  case ";
    replace_spaces_forward(string1, 13);
    printf("%s\n", string1);
 
    char string2[100] = "a test  case ";
    replace_spaces_backward(string2, 13);
    printf("%s\n", string2);
    
    return 0;
}
