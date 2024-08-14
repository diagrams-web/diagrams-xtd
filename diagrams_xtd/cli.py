import argparse
import sys


def build(paths) -> int:
    """Build the diagram for the provided file(s)."""
    for path in paths:
        print('Generate diagram for the file: ', path)
        with open(path) as f:
            exec(f.read())

    return 0


def metas(providers) -> list:
    """Return the metas for the given provider(s)."""
    import os

    resources_path = 'resources'
    providers_metas: list[dict] = []
    # list the providers from resources dir
    provider_list = os.listdir(resources_path)
    provider_list.sort()
    for one_provider in provider_list:
        provider_path = '%s/%s' % (resources_path, one_provider)
        if one_provider in providers or providers == ['all']:
            providers_metas.append({one_provider: _read_provider_meta_file(provider_path)})
            # we asked only this provider so leave the loop
            if one_provider in providers and len(providers) == 1:
                break

    return providers_metas


def _read_provider_meta_file(provider_path) -> str:
    """"""
    import os
    import json

    meta_file_name = 'meta.json'
    meta_file_content = ''

    for one_file in os.listdir(provider_path):
        if one_file == meta_file_name:
            with open(provider_path + '/' + meta_file_name, "r") as meta_file:
                meta_file_content = json.load(meta_file)
    return meta_file_content


def main():
    parser = argparse.ArgumentParser(prog='diagrams')
    subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name')

    # cfor the default build command
    parser_a = subparsers.add_parser('build', help='Run diagrams code files in a diagrams environment.')
    parser_a.add_argument(
        "paths",
        metavar="path",
        type=str,
        nargs="+",
        help="a Python file containing diagrams code",
    )

    # create the parser for the --metas command
    parser_b = subparsers.add_parser('metas', help='Return metas for given provider(s)')
    parser_b.add_argument(
        "pvd",
        type=str,
        nargs="+",
        help="Name of a provider, set to 'all' get all the providers."
    )

    args = parser.parse_args()

    if args.subparser_name == 'build':
        sys.exit(build(args.paths))
    elif args.subparser_name == 'metas':
        print(metas(args.pvd))
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
