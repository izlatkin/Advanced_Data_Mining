#include "adm.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <stdexcept>
#include <sstream>

using namespace std;


void main_pipeline(){

}
/*
 * parse score and add to struct
 */

void read_score(){
    for (string line; getline(cin, line);) {
        cout << line << endl;
    }
}


void allocate_memory_hierarchy_stucture(){
}

/*
 * print statistics
 */

void print_stat(){

}

int main()
{
    //allocate all structures
    allocate_memory_hierarchy_stucture();
    //read input then call main_piplene
    read_score();
    //print statictics
    print_stat();
    return 0;
}


