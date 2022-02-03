#include "adm.h"
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <stdexcept>
#include <stdio.h>

using namespace std;

void parse_line(string s){
    string delimiter = "\t";
    id.push_back(stoi(s.substr(0, s.find(delimiter))));
    s.erase(0, s.find(delimiter) + delimiter.length());
    midterm.push_back(stoi(s.substr(0, s.find(delimiter))));
    s.erase(0, s.find(delimiter) + delimiter.length());
    final.push_back(stoi(s));
}

/*
 * find mode in sorted vector
 */

int find_mode(vector<int> v){
    int number = v[0];
    int mode = number;
    int count = 1;
    int countMode = 1;
    for (int i=1; i < v.size(); i++){
        if (v[i] == number) {
            ++count;
        }else{
            if (count > countMode){
                countMode = count;
                mode = number;
            }
            count = 1;
            number = v[i];
        }
    }
    if (count > countMode){
        countMode = count;
        mode = number;
    }
    return mode;
}

/*
 * calculate standard deviation
 */

float calculate_standard_deviation(vector<int> v, float mean) {
    float standardDeviation = 0.0;
    for(int i = 0; i < 10; ++i) {
        standardDeviation += pow(v[i] - mean, 2);
    }
    return sqrt(standardDeviation / 10);
}

/*
 * calculation of:
 *   1. Max, min, median, Q1, Q3;
 *   2. Mean, mode, Standard deviation.
 */
void calculate_stat_for_vector(string name, vector<int> v){
    if (v.size() == 0){
        printf("empty file\n");
        return;
    }
    int v_min = v[0];
    int v_max = v[0];
    int v_sum = v[0];
    int size = v.size();
    vector<int> sorted_v;
    sorted_v.push_back(v[0]);
    for (int i = 1; i < v.size(); i++){
        //cout << v[i] << ", " ;
        sorted_v.push_back(v[i]);
        v_sum += v[i];
        if (v[i] < v_min)
            v_min = v[i];
        if (v[i] > v_max)
            v_max = v[i];
    }

    sort(sorted_v.begin(), sorted_v.end());
    float v_median, v_Q1, v_Q3;
    //printf("size: %d \n", size);
    int half_size = 0;
    if (size % 2 == 0){
        half_size = size / 2 ;
        v_median = 1.0 * (sorted_v[size / 2] +  sorted_v[size / 2 - 1]) / 2;
    }else{
        half_size = size / 2 + 1;
        v_median = sorted_v[size / 2 ];
    }
    if (half_size % 2 == 0){
        v_Q1 = 1.0 * (sorted_v[half_size / 2] +  sorted_v[half_size / 2 - 1]) / 2;
    }else{
        v_Q1 = 1.0 * sorted_v[half_size / 2];
    }
    int second_size = size - half_size;
    if (second_size % 2 == 0){
        v_Q3 = 1.0 * (sorted_v[half_size + half_size / 2 ] +  sorted_v[half_size + half_size / 2 - 1]) / 2;
    }else{
        v_Q3 = 1.0 * sorted_v[half_size + half_size / 2 - 1 ];
    }


    printf("%s: Max - %d, min - %d, median - %.3lf, Q1 - %.3lf, Q3 - %.3lf \n",
           name.c_str(), v_max, v_min, v_median, v_Q1, v_Q3);
    float mean = 1.0 * v_sum / size;
    int mode = find_mode(sorted_v);
    float standard_deviation = calculate_standard_deviation(sorted_v, mean);
    printf("%s: Mean - %.3lf, mode - %d, Standard deviation - %.3lf\n",
           name.c_str(), mean, mode, standard_deviation);
}
/*
 * parse score and add to struct
 */

void read_score(){
    for (string line; getline(cin, line);) {
        parse_line(line);
    }
}


void allocate_memory_hierarchy_stucture(){
}

void main_pipeline(){
    calculate_stat_for_vector("Midterm", midterm);
    calculate_stat_for_vector("Final", final);
//    vector<int> tmp {13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70} ;
//    calculate_stat_for_vector("test", tmp);
}

int main()
{
    //allocate all structures
    allocate_memory_hierarchy_stucture();
    //read input then call main_piplene
    read_score();
    //calculate values
    main_pipeline();
    return 0;
}


