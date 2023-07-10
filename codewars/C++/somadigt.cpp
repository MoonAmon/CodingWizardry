#include <iostream>
#include <vector>
#include <string>

int main() {
    int n = 16;
    int soma = 0;
    std::string str_numero = std::to_string(n); // Converte o número em uma string

    int tamanho = str_numero.length();
    std::vector<int> vetor(tamanho);

    for (int i = 0; i < tamanho; i++) {
        vetor[i] = str_numero[i] - '0'; // Converte cada caractere em um dígito inteiro
    }

    // Exibe o vetor resultante
    for (int i = 0; i < tamanho; i++) {
        std::cout << vetor[i] << " ";
    }
    for (int i = 0; i < tamanho; i++)
    {
        soma += vetor[i];
    }
  
    return soma;

}
