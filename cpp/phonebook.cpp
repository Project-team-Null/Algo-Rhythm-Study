#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string line;
    vector<string> arr;

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> line;
    arr.push_back(line);

    int idx;

    while (fin >> line)
    {
        for (auto &i : arr)
        {
            idx = (i.length() > line.length()) ? i.find(line) : line.find(i);
            if (idx == 0)
            {
                fout << 0;
                fin.close();
                fout.close();
                return 0;
            }
        }
        arr.push_back(line);
    }

    fout << 1;
    fin.close();
    fout.close();
    return 0;
}