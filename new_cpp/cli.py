import click


@click.command()
@click.argument('name', type=str)
def main(name):
    print('new-cpp', name)
