import random

import click


@click.command()
@click.option('--count', default=1, help='Number of random sets')
def parsel(count):
    """CLI program to print random number from 1 to 10"""
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in range(count):
        random.shuffle(items)
        click.echo(items)


if __name__ == '__main__':
    parsel()
