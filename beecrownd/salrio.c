#include <stdio.h>
#include <stdlib.h>
 
using namespace std;
 
int main() {
 
   double salario, venda, comissao, total;
    char nome;

    printf("");
    scanf("%s", &nome);

    printf("");
    scanf("%lf", &salario);

    printf("");
    scanf("%lf", &venda);

    comissao=venda*0.15;

    total=salario+comissao;

    printf("TOTAL = R$ %.2f\n", total);
 
    return 0;
}

