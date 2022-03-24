#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void swap_(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

bool sort_changed(vector<int> &num_arr, bool is_odd)
{
    auto iter = num_arr.begin();
    auto next = iter + 1;
    auto end = num_arr.end();
    bool changed = false;

    if (!is_odd)
    {
        iter++;
        next++;
    }

    while (iter != end && next != end)
    {
        if (*iter > *next)
        {
            swap_(*iter, *next);
            changed = true;
        }
        iter += 2;
        next += 2;
    }

    return changed;
}

int main()
{
    string line;
    vector<int> num_arr;
    int n;
    int num;

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> n;
    while (fin >> num)
    {
        num_arr.push_back(num);
    }

    int cnt = 0;
    bool is_odd = true;
    bool last = true;
    bool cur = sort_changed(num_arr, is_odd);

    while (cur || last)
    {
        is_odd = !is_odd;
        last = cur;
        cur = sort_changed(num_arr, is_odd);
        cnt++;
    }

    fout << cnt - 1;

    fin.close();
    fout.close();

    return 0;
}