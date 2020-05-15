"""
Grapphin Mind models.
"""

from django.db import models

from grapphin.constants import NodeContent
from grapphin.models import GModel, HistoricMixin, OwnedMixin


class GTree(GModel, HistoricMixin, OwnedMixin):
    """
    GTree model. Represents a tree
    of GNodes that is owned by a user.
    """

    __prefix__ = "trees"

    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name="Name",
    )

    description = models.TextField(
        default="",
        null=False,
        blank=True,
        verbose_name="Description",
    )


class GNode(GModel, HistoricMixin, OwnedMixin):
    """
    GNode model. Represents a single node
    of content owened by a user.
    """

    __prefix__ = "nodes"

    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name="Name",
    )

    description = models.TextField(
        default="",
        null=False,
        blank=True,
        verbose_name="Description",
    )

    relations = models.ManyToManyField(
        "mind.GNode",
        through="GBranch",
        symmetrical=False,
    )

    def __str__(self):
        return f"{self.name} (owned by: {self.owner})"

    @property
    def inbound_nodes(self):
        """
        Returns the inbound nodes IDs.
        """

        return self.inbound_branches.values("inbound", "tree")

    @property
    def outbound_nodes(self):
        """
        Returns the outbound nodes IDs.
        """

        return self.outbound_branches.values("outbound", "tree")



class GContent(GModel, HistoricMixin):
    """
    GContent model. Actual content
    stored against a GNode.
    """

    __prefix__ = "contents"

    node = models.ForeignKey(
        "mind.GNode",
        related_name="contents",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    kind = models.CharField(max_length=32, choices=NodeContent.choices)

    value = models.TextField()

    def __str__(self):
        return f"{self.kind} for {self.node}"


class GBranch(GModel):
    """
    GBranch model. Connection between
    GNodes, forming a GTree.
    """

    __prefix__ = "branches"

    name = models.CharField(
        max_length=128,
        default="",
        null=False,
        blank=True,
        verbose_name="Name",
    )

    description = models.TextField(
        default="",
        null=False,
        blank=True,
        verbose_name="Description",
    )

    inbound = models.ForeignKey(
        "mind.GNode",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="outbound_branches",
    )

    outbound = models.ForeignKey(
        "mind.GNode",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="inbound_branches",
    )

    weight = models.IntegerField(
        default=0,
        verbose_name="Weight",
        help_text="Weight of the relation",
    )

    tree = models.ForeignKey(
        "mind.GTree",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="branches",
    )

    def __str__(self):
        return f"Branch from {self.inbound} to {self.outbound}"
