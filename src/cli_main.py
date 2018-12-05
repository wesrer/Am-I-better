import click

@click.command()
def firstRunText():

    click.secho('Welcome to the Am-I-better? setup.', fg='yellow')
    click.echo('Please answer a few questions to continue')


if __name__ == '__main__':
    firstRunText()
