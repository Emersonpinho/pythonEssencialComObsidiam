você provavelmente encontrará muitas strings com prefixo ```u```, por exemplo:

```u"Minha string"``` 

isso é a sintaxe surgiu na versão 2 para dizer que uma string está escrita em uma unicode. já na versão 3,3, a sintaxe ```u"minha string``` passou novamente a ser aceita para facilitar a portabilidade de programas escritos na versão 2, nos quais os literais unicode devem ter obrigatoriamente o prefixo, como em ```u'string'```. anteriormente, nas versões 3.0 até 3.2, as strings com prefixo ```u``` eram erro de sintaxe.
