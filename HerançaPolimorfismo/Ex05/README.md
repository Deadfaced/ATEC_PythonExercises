# Exercício 5 — Herança e composição

## a) Relações e justificações

| Par | Relação | Justificação |
| --- | --- | --- |
| Cão e Animal | É um — herança | Um cão é um animal e pode herdar as suas características e comportamentos. |
| Carro e Roda | Tem um — composição | Um carro tem rodas como componentes. |
| Gestor e Funcionário | É um — herança | Um gestor é um funcionário com responsabilidades específicas. |
| Computador e Teclado | Tem um — composição | Um computador tem um teclado que utiliza para escrever texto. |
| Quadrado e Forma geométrica | É um — herança | Um quadrado é uma forma geométrica com quatro lados iguais e quatro ângulos retos. |
| Biblioteca e Livro | Tem um — composição | Uma biblioteca tem livros na sua coleção. |

## b) e c) Implementação

`Computer` cria um `Keyboard` e guarda-o no atributo privado `__keyboard`.
O método `write()` delega a formatação do texto no método `type_text()` do teclado.

Executar `python main.py` nesta pasta.

Output esperado:

```text
Lenovo: [PT] Olá mundo
```
