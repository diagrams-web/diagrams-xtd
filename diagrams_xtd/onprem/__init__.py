"""
OnPrem provides a set of general on-premise services.
"""

from diagrams_xtd import Node


class _OnPrem(Node):
    _provider = "onprem"
    _icon_dir = "resources/onprem"

    fontcolor = "#ffffff"
