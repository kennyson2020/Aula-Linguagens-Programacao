#include <iostream>

using namespace std;

int main() {

    string nome;
    string sobrenome;
    cin >> nome;
    cin >> sobrenome;

    int ultima_posicao = nome.size() -1;


    cout << sobrenome << "," << nome [0] << nome[ultima_posicao] << endl;

    return 0;
}

