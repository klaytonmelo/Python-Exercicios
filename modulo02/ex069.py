from rich import print

maior = homens = menor_20 = 0

while True:
    print("-" * 30)
    print("[blue]     CADASTRE UMA PESSOA   [/]")
    print("-" * 30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))

    while sexo.strip().upper()[0] not in "MF":
        print("[red]ERRO![/] [green]tente novamente...[/]")
        sexo = str(input('Sexo: '))

    if idade >= 18:
        maior += 1

    if sexo.strip().upper()[0] == "M":
        homens += 1

    if sexo.strip().upper()[0] == "F" and idade < 20:
        menor_20 +=1

    op = str(input('Quer continuar ? [s/n]'))

    while op.strip().upper()[0] not in "SN":
            print("[red]ERRO![/] [green]tente novamente...[/]")
            op = str(input('Quer continuar ? [s/n] '))

    if op.strip().upper()[0] == "N":
        break

print("[green]-[/]" * 30)
print(f"[green]total de pessoas[/] [blue]com mais de [yellow]18 anos[/]: [green]{maior}[/][/]")
print(f"[blue]Ao todo temos [yellow]{homens}[/] homens cadastrados[/]")
print(f"[blue]E temos [yellow]{menor_20}[/] mulheres com menos de [yellow]20 anos[/][/]")
print("[green]-[/]" * 30)