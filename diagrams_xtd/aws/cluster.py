from diagrams_xtd import Cluster
from diagrams_xtd.aws.compute import EC2, ApplicationAutoScaling
from diagrams_xtd.aws.network import VPC, PrivateSubnet, PublicSubnet


class Region(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "dotted",
        "labeljust": "l",
        "pencolor": "#AEB6BE",
        "fontname": "Sans-Serif",
        "fontsize": "12",
    }
    # fmt: on


class AvailabilityZone(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "dashed",
        "labeljust": "l",
        "pencolor": "#27a0ff",
        "fontname": "sans-serif",
        "fontsize": "12",
    }
    # fmt: on


class VirtualPrivateCloud(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "",
        "labeljust": "l",
        "pencolor": "#00D110",
        "fontname": "sans-serif",
        "fontsize": "12",
    }
    # fmt: on
    _icon = VPC


class PrivateSubnet(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "",
        "labeljust": "l",
        "pencolor": "#329CFF",
        "fontname": "sans-serif",
        "fontsize": "12",
    }
    # fmt: on
    _icon = PrivateSubnet


class PublicSubnet(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "",
        "labeljust": "l",
        "pencolor": "#00D110",
        "fontname": "sans-serif",
        "fontsize": "12",
    }
    # fmt: on
    _icon = PublicSubnet


class SecurityGroup(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "dashed",
        "labeljust": "l",
        "pencolor": "#FF361E",
        "fontname": "Sans-Serif",
        "fontsize": "12",
    }
    # fmt: on


class AutoScalling(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "dashed",
        "labeljust": "l",
        "pencolor": "#FF7D1E",
        "fontname": "Sans-Serif",
        "fontsize": "12",
    }
    # fmt: on
    _icon = ApplicationAutoScaling


class EC2Contents(Cluster):
    # fmt: off
    _default_graph_attrs = {
        "shape": "box",
        "style": "",
        "labeljust": "l",
        "pencolor": "#FFB432",
        "fontname": "Sans-Serif",
        "fontsize": "12",
    }
    # fmt: on
    _icon = EC2
