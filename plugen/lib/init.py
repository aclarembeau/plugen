from pathlib import Path


def init_func(args):
    with open(Path(__file__).parent.parent.parent.joinpath('plugen.config.yml'), 'r') as source_file:
        with open('plugen.config.yml', 'w+') as dest_file:
            dest_file.write(source_file.read())