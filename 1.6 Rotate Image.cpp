#include <stdint.h>
#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

// >> is treated as bit-wise right shifting
// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2005/n1757.html
typedef vector<uint32_t> Row;
typedef vector<Row> Image;

// if using 2D array, it will decay to a pointer to array,
//   and the array size should be explicitly stated like uint32_t image[][5],
//   so flexibility is degraded
// even more, the actual parameter should be declared a size by constant to match formal one
//   like uint32_t image[5][5] or replace 5 with const int 5
// so, use vector insted
void rotate_image(Image &image, int length)
{
    for (int layer = 0; layer < length / 2; ++layer)
    {
        int start = layer;
        int end = length - 1 - start;
        for (int i = start; i < end; ++i)
        {
            int offset = i - start;
            uint32_t temp = image[start][i];
            image[start][i] = image[end - offset][start];
            image[end - offset][start] = image[end][end - offset];
            image[end][end - offset] = image[i][end];
            image[i][end] = temp;
        }
    }
}

void print_image(Image &image, int length)
{
    for (auto &i : image)
    {
        for (auto &j : i)
        {
            cout << setw(3) << j;
        }
        cout << endl;
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    int length = 5;
    Image image(length, Row(length));
    int value = 0;
    for (auto &i : image)
    {
        for (auto &j : i)
        {
            j = value++;
        }
    }

    print_image(image, length);
    rotate_image(image, length);
    print_image(image, length);

    return 0;
}