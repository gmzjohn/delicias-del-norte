from typing import Callable, Generic, Optional, TypeVar
from ..domains.enums.traverse_type import TraverseType

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self,
        value: T,
        next: Optional["Node[T]"] = None,
        prev: Optional["Node[T]"] = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional["Node[T]"] = None
        self.tail: Optional["Node[T]"] = None
        self.length = 0

    def get_length(self) -> int:
        return self.length

    def add(self, value: T) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            prev_node = self.tail
            if prev_node is not None:
                new_node.prev = prev_node
                prev_node.next = new_node

            self.tail = new_node

        self.length += 1

    def pop(self) -> None:
        if self.tail is not None:
            self.tail = self.tail.prev

        self.length -= 1

    def _traverse(
        self,
        direction: TraverseType,
        node: Optional["Node[T]"],
        fn: Callable[["T"]],
    ) -> None:
        if node is None:
            return
        fn(node.value)

        next_node = node.next if direction == TraverseType.FORWARD else node.prev

        self._traverse(direction, next_node, fn)

    def traverse(
        self,
        direction: TraverseType,
        fn: Callable[["T"]],
    ) -> None:


        node = self.head if direction == TraverseType.FORWARD else self.tail

        self._traverse(direction, node, fn)

