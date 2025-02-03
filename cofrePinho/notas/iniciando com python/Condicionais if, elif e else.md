
Se considerarmos que grande parte das pessoas no Brasil paga a mesma quantidade de impostos, **podemos dizer que existe um valor padrão usá-lo se o usuário não souber informar quanto paga.**  Para isso podemos aplicar um ```if``` para saber se ele deixou o input vazio. Caso não seja vazio, vamos usá-lo como o valor da taxa de impostos digitada pelo usuário. 

## Comando if

Na teoria, um ```if``` é um comando que avalia uma **expressão** e escolhe um bloco a ser executado, de acordo com o resultado dessa avaliação. A expressão nesse casso é ```imposto == ""``` **tendo uma variável sendo comparada com o operador de igualdade** == com um valor literal da string vazia. Semanticamente, uma string vazia em um bloco ```if``` equivale a ```False``` 

## Expressão if

Também existem as expressões condicionais ```if```, chamados de operadores ternários (No caso do operador ternário, a expressão condicional é usada para determinar o valor que será atribuído a uma variável, mas não é que as condições estejam "dentro" da variável. Em vez disso, a variável recebe um valor baseado na avaliação da condição. ) este nome "Operador ternário" surgiu porque geralmente ele lida com três tipos de situações retorna o valor internamente e atribui a variável