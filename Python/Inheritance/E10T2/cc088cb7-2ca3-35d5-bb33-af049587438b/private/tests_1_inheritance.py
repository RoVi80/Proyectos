#!/usr/bin/env python3

from unittest import TestCase
from abc import ABC
import ast

# catch potential exception from import
try:
    from public.shop import Shop
    from public.bakery import Bakery
    from public.clothing_store import ClothingStore
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass

ANNO = "abstractmethod"

class TestInheritance(TestCase):

    def test_shop(self):
        try:
            sut = TestShop(1000)
        except:
            m = "@@Anonymous subclass of Shop cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(sut, ABC, "@@Shop does not extend ABC.@@")

    def test_bakery(self):
        try:
            sut = Bakery(1000)
        except:
            m = "@@Bakery cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(sut, Shop, "@@Bakery does not extend Shop.@@")

    def test_clothing_store(self):
        try:
            sut = ClothingStore(2000)
        except:
            m = "@@ClothingStore cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(sut, Shop, "@@ClothingStore does not extend Shop.@@")

    def test_for_abstract_method_annotations(self):
        with open("public/shop.py") as f:
            tree = ast.parse(f.read())

            #print(ast.dump(tree))

            v = ABCTestVisitor()
            v.visit(tree)

            for name in ["add_procured_units", "get_produced_units", "set_produced_units"]:
                if name not in v.annotated_methods:
                    m = "@@The method '{}' lacks the required annotation '{}'.@@".format(name, ANNO)
                    self.fail(m)


class ABCTestVisitor(ast.NodeVisitor):

    def __init__(self):
        self.annotated_methods = []

    def visit_FunctionDef(self, node):
        for d in node.decorator_list:
            if d.id == ANNO:
                self.annotated_methods.append(node.name)


class TestShop(Shop):
    def add_procured_units(self, units):
        pass

    def get_produced_units(self):
        pass

    def set_produced_units(self, units):
        pass