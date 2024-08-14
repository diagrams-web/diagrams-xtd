---
id: cluster
title: Clusters
---

Cluster allows you group (or clustering) the nodes in an isolated group.

## Basic

Cluster represents a local cluster context.

You can create a cluster context with Cluster class. And you can also connect the nodes in a cluster to other nodes outside a cluster.

```python
from diagrams_xtd import Cluster, Diagram
from diagrams_xtd.aws.compute import ECS
from diagrams_xtd.aws.database import RDS
from diagrams_xtd.aws.network import Route53

with Diagram("Simple Web Service with DB Cluster", show=False):
    dns = Route53("dns")
    web = ECS("service")

    with Cluster("DB Cluster"):
        db_main = RDS("main")
        db_main - [RDS("replica1"),
                     RDS("replica2")]

    dns >> web >> db_main
```

![simple web service with db cluster diagram](/img/simple_web_service_with_db_cluster_diagram.png)

## Nested Clusters

Nested clustering is also possible.

```python
from diagrams_xtd import Cluster, Diagram
from diagrams_xtd.aws.compute import ECS, EKS, Lambda
from diagrams_xtd.aws.database import Redshift
from diagrams_xtd.aws.integration import SQS
from diagrams_xtd.aws.storage import S3

with Diagram("Event Processing", show=False):
    source = EKS("k8s source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers = [ECS("worker1"),
                       ECS("worker2"),
                       ECS("worker3")]

        queue = SQS("event queue")

        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]

    store = S3("events store")
    dw = Redshift("analytics")

    source >> workers >> queue >> handlers
    handlers >> store
    handlers >> dw
```

![event processing diagram](/img/event_processing_diagram.png)

> There is no depth limit of nesting. Feel free to create nested clusters as deep as you want.

## Clusters with icons in the label

You can add a Node icon before the cluster label (and specify its size as well).  You need to import the used Node class first.

It's also possible to use the node in the `with` context adding `cluster=True` to
make it behave like a cluster.

```python
from diagrams_xtd import Cluster, Diagram
from diagrams_xtd.aws.compute import ECS
from diagrams_xtd.aws.database import RDS, Aurora
from diagrams_xtd.aws.network import Route53, VPC

with Diagram("Simple Web Service with DB Cluster Icon", show=False):
    dns = Route53("dns")
    web = ECS("service")

    with Cluster(label='VPC',icon=VPC):
        with Cluster("DB Cluster A", icon=Aurora, icon_size=30):
            db_main = RDS("main")
            db_main - [RDS("replica1"),
                         RDS("replica2")]
        with Aurora("DB Cluster B", cluster=True):
            db_main = RDS("main")
            db_main - [RDS("replica1"),
                         RDS("replica2")]

        dns >> web >> db_main
```

![Simple Web Service with DB Cluster Icon](/img/simple_web_service_with_db_cluster_icon.png)

Another example with already defined Cluster with Node icon for AWS

```python
from diagrams_xtd import Diagram, Edge
from diagrams_xtd.aws.cluster import *
from diagrams_xtd.aws.compute import EC2
from diagrams_xtd.onprem.container import Docker
from diagrams_xtd.onprem.cluster import *
from diagrams_xtd.aws.network import ELB

with Diagram(name="AWS cluster with icon", direction="TB", show=False):
    with Cluster("AWS"):
        with Region("eu-west-1"):
            with AvailabilityZone("eu-west-1a"):
                with VirtualPrivateCloud(""):
                    with PrivateSubnet("Private"):
                        with SecurityGroup("web sg"):
                            with AutoScalling(""):
                                with EC2Contents("A"):
                                    d1 = Docker("Container")
                                with ServerContents("A1"):
                                    d2 = Docker("Container")

                    with PublicSubnet("Public"):
                        with SecurityGroup("elb sg"):
                            lb = ELB()

    lb >> Edge(forward=True, reverse=True) >> d1
    lb >> Edge(forward=True, reverse=True) >> d2
```

![AWS cluster with icon](/img/aws_cluster_with_icon.png)

And for Azure

```python
from diagrams_xtd import Diagram, Edge
from diagrams_xtd.azure.cluster import *
from diagrams_xtd.azure.compute import VM
from diagrams_xtd.onprem.container import Docker
from diagrams_xtd.onprem.cluster import *
from diagrams_xtd.azure.network import LoadBalancers

with Diagram(name="Azure cluster with icon", direction="TB", show=False):
    with Cluster("Azure"):
        with Region("East US2"):
            with AvailabilityZone("Zone 2"):
                with VirtualNetwork(""):
                    with SubnetWithNSG("Private"):
                        # with VMScaleSet(""): # Depends on PR-404
                        with VMContents("A"):
                            d1 = Docker("Container")
                        with ServerContents("A1"):
                            d2 = Docker("Container")

                    with Subnet("Public"):
                        lb = LoadBalancers()

    lb >> Edge(forward=True, reverse=True) >> d1
    lb >> Edge(forward=True, reverse=True) >> d2
```

![Azure cluster with icon](/img/azure_cluster_with_icon.png)
