'''Exercícios Teóricos | Capítulo 4


1) Qual o significado de estado? E de computação?

Num dado instante, os objetos têm um determinado conjunto de características (em particular, têm um dado valor) e o
programa encontra-se a executar uma dada instrução. Afirmamos que o programa se encontra num dado ESTAD0.A sequência
de estados por que vai passando o programa ao longo do tempo constitui uma COMPUTAÇÃO.


2) Que palavras reservadas existem em Python? Qual é a sua função e importância?

and, as, assert, break, class, continue, def, del, elif, else, except, false, finally, for, from, global,
if, import, in, is, lambda, none, nonlocal, not, or, pass, raise, return, true, width, while, yield.

Definem regras de sintaxe e estrutura da linguagem e elas não podem ser usadas como nomes de variáveis.


3) O que significa dizer que Python é uma linguagem não tipada e que o tipo associado a um objeto é determinado
dinamicamente?

O tipo não tem de ser declarado, sendo uma característica do objeto e não do nome que, num dado instante,
lhe está associado. Exemplo: o nome x deixou de estar associado a um objeto do tipo float e ficou associado a um objeto
do tipo int.

Fortemente tipada, ou seja, deve fazer operações com a necessidade da realização de cast; e dinamicamente tipada,
ou seja, em que o tipo de uma variável pode ser alterado durante a execução do código.

_ Na tipagem estática, o tipo é inferido pela variável e a checagem (type checking) é feita durante a compilação;

_ Na tipagem dinâmica, o tipo é inferido pelo valor do dado e a checagem (type checking) é feita
em tempo de execução (runtime);


4) Que consequências práticas existem de a tipagem ser dinãmica?

Perdem em relação à performance de execução melhor da tipagem estática, pois durante a execução o código
já foi “traduzido” para linguagem máquina e a checagem/tipagem das variáveis já foi feita. Entretanto, ganha por ser
mais ágil durante o desenvolvimento e também são mais flexíveis.


5) Como define o conceito de atribuição?

A Atribuição de Valores é a passagem de informação a determinada variável. Toda variável, por sua definição,
pode receber valores ou então, pode ter seu valor alterad.


6) Que formas de atribuição conhece?

a) atribuição implícita
b) atribuição aumentada
c) atribuição em cadeia
d) atribuição múltipla


7) De que maneiras se pode introduzir dados num programa? E de que maneiras se pode retirar resultados?

Podemos introduzir dados através dos parâmetros formais ou da instrução input, e podemos comunicar resultados
recorrendo à instrução return ou à instrução print.

No caso da instrução input, existe um argumento opcional que, quando presente, é uma cadeia de caracteres
que funciona como uma mensagem. Podemos usar o construtor dos diferentes tipos de dados para forçar um objeto a ser
convertido, quando tal é possível, para outro tipo de objeto. Ex: int(input('...'))

Para generalizar, usar eval(input('...'))
Para retirar resultados, podemos usar a função PRINT, que é feita tendo por argumento zero ou mais expressões.

Uma aplicação pode receber dados através das mais distintas formas, como por exemplo, pela leitura de um arquivo,
através dos protocolos TCP/IP, pelo uso de janelas gráficas, como por exemplo, a biblioteca TkInter, que é a
forma nativa para a construção de Janelas Gráficas no Python e etc.


8) Como funciona a instrução input? Funciona com qualquer tipo de objeto?

Faz uma pausa no programa e espera uma entrada do usuário pelo terminal. Para ler a entrada do usuário a
função input() espera que após digitada a entrada o usuário aperte a tecla enter, após isso input() lê
essa entrada como uma string, portanto, se a entrada esperada for um número ela deve ser convertida usando-se
as funções de conversão int() ou float().


9) O que é o método format?

Muitas vezes se deseja mais controle sobre a formatação da saída do que simplesmente exibir valores separados
por espaço. Existem várias maneiras de formatar a saída.

Se aplica a um modelo de cadeia de caracteres que é instanciado por recurso a argumentos por posição ou por nome.
Usamos a notação por ponto (método) com uso de chavetas para referenciar os objetos. O método format devolve
uma cadeia de caracteres, que, sendo um objeto imutável, ou é enviado para o exterior, ou é associado a um nome.
Caso contrário, perde-se.



'''