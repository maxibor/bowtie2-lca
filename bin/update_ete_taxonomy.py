#!/usr/bin/env python
import click
from ete3 import NCBITaxa

@click.command()
@click.option('-u',
              '--update',
              is_flag=True,
              help='Update local copy of ete3 NCBI taxonomy database')
def cli(**kwargs):
    """\b
    Update ete3 local copy of NCBI taxonomy database
    """
    update_db(**kwargs)


def update_db(update):
    ncbi = NCBITaxa()
    message = "ete3 taxonomy database loaded\n"
    if update:
        ncbi.update_taxonomy_database()
        message = "ete3 taxonomy database updated\n"
    with open("db_update_status.txt", 'w') as f:
        f.write(message)

if __name__ == '__main__':
    cli()