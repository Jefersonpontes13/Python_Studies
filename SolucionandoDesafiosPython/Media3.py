"""coding: utf-8"""


def main():
    n1, n2, n3, n4 = input().split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)

    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / (2 + 3 + 4 + 1)
    print(f"Media: {media:.1f}")

    if media >= 7:
        print('Aluno aprovado.')
    elif media < 5:
        print('Aluno reprovado.')
    elif 5 <= media <= 6.9:
        print('Aluno em exame.')

        n5 = float(input())
        final = (n5 + media) / 2

        print(f"Nota do exame: {n5:.1f}")

        if final >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado')
        print(f"Media final: {final:.1f}")


if __name__ == '__main__':
    main()
