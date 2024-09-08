#include <stdio.h>

unsigned long long factorial(int num){
    if (num == 0 || num == 1){
        return num;
    }
    else{
        return num * factorial(num-1);
    }
}