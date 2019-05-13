import click

@click.group
def install_cli():
    # Group for the tools that lets you install the application
    pass

@install_cli.command()
def firstRunText():
    click.secho('Welcome to the Am-I-better? setup.', fg='yellow')
    click.echo('Please answer a few questions to continue')

def install_am_i_better():
    firstRunText()

if __name__ == '__main__':
    install_am_i_better()

