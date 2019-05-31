import click
import pkg_resources


@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--version')
def version():
    project_version = pkg_resources.require("Am-I-Better")[0].version
    print(project_version)


@cli.command()
@click.option('--task', prompt='enter type of task to be added')
def add(task):
    click.echo(task)


if __name__ == "__main__":
    cli()
