# -*- coding: utf-8 -*-
import click
from func import speak


@click.command()
@click.argument('text')
def read(text):
    speak(text)
