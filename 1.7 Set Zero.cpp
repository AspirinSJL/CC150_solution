#include <iostream>
#include <iomanip>
#include <vector>
#include <bitset>

using namespace std;

typedef vector<int> Row;
typedef vector<Row> Matrix;

size_t const MAX_ROW = 20;
size_t const MAX_COL = 20;

void set_zero(Matrix &matrix, size_t row, size_t col)
{
    bitset<MAX_ROW> row_checker;
    bitset<MAX_COL> col_checker;
    
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            if (matrix[i][j] == 0)
            {
                row_checker.set(i);
                col_checker.set(j);
            }
        }
    }
    
//    for (int i = 0; i < row; ++i)
//    {
//        if (row_checker[i])
//        {
//            for (int k = 0; k < col; ++k)
//            {
//                matrix[i][k] = 0;
//            }
//        }
//    }
//    for (int j = 0; j < col; ++j)
//    {
//        if (col_checker[j])
//        {
//            for (int k = 0; k < row; ++k)
//            {
//                matrix[k][j] = 0;
//            }
//        }
//    }
    
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
        {
            if (row_checker[i] || col_checker[j])
            {
                matrix[i][j] = 0;
            }
        }
    }
}

void print_matrix(Matrix const &matrix, size_t row, size_t col)
{
    for (auto &i : matrix)
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
    size_t row = 5, col = 4;
    Matrix matrix(row, Row(col));
    int value = 0;
    for (auto &i : matrix)
    {
        for (auto &j : i)
        {
            j = value++;
        }
    }
    matrix[2][1] = 0;
    matrix[4][2] = 0;
    
    print_matrix(matrix, row, col);
    set_zero(matrix, row, col);
    print_matrix(matrix, row, col);

    return 0;
}