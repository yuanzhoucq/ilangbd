# -*- coding: utf-8 -*-
import click
from func import speak


@click.command()
@click.option('-f', type=click.File('rb'))
@click.argument('text', required=False)
def read(f, text):
    if f:
        speak(unicode(f.read(), 'utf-8'))
    elif text:
        speak(text)
    else:
        print('Text is required.')

if __name__ == '__main__':
    read()
