import os
import sys
from typing import Iterable

from jinja2 import Environment, FileSystemLoader, Template, exceptions

import config as cfg
from . import app_root_dir, doc_root_dir, resource_dir, template_dir, base_dir

_usage = "Usage: generate.py <provider>"


def load_tmpl(tmpl: str) -> Template:
    env = Environment(loader=FileSystemLoader(template_dir()))
    env.filters["up_or_title"] = up_or_title
    return env.get_template(tmpl)


def up_or_title(pvd: str, s: str) -> str:
    if s in cfg.UPPER_WORDS.get(pvd, ()):
        return s.upper()
    if s in cfg.TITLE_WORDS.get(pvd, {}):
        return cfg.TITLE_WORDS[pvd][s]
    return s.title()


def gen_class_metas(pvd: str, typ: str, paths: Iterable[str]) -> list:
    """Generate the class metas."""
    metas = []
    for path in paths:
        base = os.path.splitext(path)[0]
        name = "".join([up_or_title(pvd, s) for s in base.split("-")])
        alias = cfg.ALIASES[pvd].get(typ, {}).get(name, '')
        metas.append({"name": name, "icon": path, "alias": alias})
    return metas


def gen_classes(pvd: str, typ: str, metas: Iterable[str]) -> str:
    """Generate all service node classes based on resources paths with class templates."""
    tmpl = load_tmpl(cfg.TMPL_MODULE)
    aliases = {meta['name']: meta['alias'] for meta in metas if meta['alias']}
    return tmpl.render(pvd=pvd, typ=typ, metas=metas, aliases=aliases)


def gen_apidoc(pvd: str, typ_paths: dict) -> str:
    try:
      default_tmp = cfg.TMPL_APIDOC.split('.')
      tmpl_file = f"{default_tmp[0]}_{pvd}.{default_tmp[1]}"
      tmpl = load_tmpl(tmpl_file)
    except exceptions.TemplateNotFound:
      tmpl = load_tmpl(cfg.TMPL_APIDOC)

    # TODO: remove
    def _gen_class_name(path: str) -> str:
        base = os.path.splitext(path)[0]
        name = "".join([up_or_title(pvd, s) for s in base.split("-")])
        return name

    typ_classes = {}
    for typ, (paths, resource_root) in sorted(typ_paths.items()):
        typ_classes[typ] = []
        for path in paths:
            name = _gen_class_name(path)
            resource_path = os.path.join(resource_root, path)
            alias = cfg.ALIASES[pvd].get(typ, {}).get(name)
            typ_classes[typ].append({"name": name, "alias": alias, "resource_path": resource_path})
    return tmpl.render(pvd=pvd, typ_classes=typ_classes)


def make_module(pvd: str, typ: str, classes: str) -> None:
    """Create a module file"""
    mod_path = os.path.join(app_root_dir(pvd), f"{typ}.py")
    with open(mod_path, "w+") as f:
        f.write(classes)


def make_apidoc(pvd: str, content: str) -> None:
    """Create an api documentation file"""
    mod_path = os.path.join(doc_root_dir(), f"{pvd}.md")
    with open(mod_path, "w+") as f:
        f.write(content)


def make_metas(pvd: str, content: str) -> None:
    """Create metas for other services"""
    import json

    meta_path = os.path.join(resource_dir(pvd), "meta.json")
    with open(meta_path, "w+") as f:
        f.write(json.dumps(content, sort_keys=True))


def generate(pvd: str) -> None:
    """Generates a service node classes."""
    typ_paths = {}
    typ_meta = {}
    base = base_dir()
    for root, _, files in os.walk(resource_dir(pvd)):
        # Extract the names and paths from resources.
        files.sort()
        pngs = list(filter(lambda f: f.endswith(".png"), files))
        paths = list(filter(lambda f: "rounded" not in f, pngs))

        # Skip the top-root directory.
        typ = os.path.basename(root)
        if typ == pvd:
            continue

        resource_root = os.path.relpath(root, base)
        metas = gen_class_metas(pvd, typ, paths)
        classes = gen_classes(pvd, typ, metas)
        make_module(pvd, typ, classes)

        typ_paths[typ] = (paths, resource_root)
        typ_meta[typ] = metas

    # Build API documentation
    apidoc = gen_apidoc(pvd, typ_paths)
    make_apidoc(pvd, apidoc)
    make_metas(pvd, typ_meta)


if __name__ == "__main__":
    pvd = sys.argv[1]
    if pvd not in cfg.PROVIDERS:
        sys.exit()
    generate(pvd)
