QUESTÃO 1045 - Tipos de Triângulo 

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, 
de modo que o lado A representa o maior dos 3 lados. 
A seguir, determine o tipo de triângulo que estes três lados formam, 
com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

- se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
- se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO;
- se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO;
- se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO;
- se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
- se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;

>>>>    Entrada ->
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

>>>>    Saída ->
Imprima todas as classificações do triângulo especificado na entrada.

Exemplo de Entrada
> 7.0 5.0 7.0

Exemplo de Saída
> TRIANGULO ACUTANGULO
> TRIANGULO ISOSCELES

Exemplo de Entrada
> 6.0 6.0 10.0

Exemplo de Saída
> TRIANGULO OBTUSANGULO
> TRIANGULO ISOSCELES

Exemplo de Entrada
> 6.0 6.0 6.0

Exemplo de Saída
> TRIANGULO ACUTANGULO
> TRIANGULO EQUILATERO

Exemplo de Entrada
> 5.0 7.0 2.0

Exemplo de Saída
> NAO FORMA TRIANGULO

Exemplo de Entrada
> 6.0 8.0 10.0

Exemplo de Saída
> TRIANGULO RETANGULO