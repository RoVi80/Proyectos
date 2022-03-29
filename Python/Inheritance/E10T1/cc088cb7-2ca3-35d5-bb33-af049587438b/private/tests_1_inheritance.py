#!/usr/bin/env python3

from unittest import TestCase
from abc import ABC
import ast

# catch potential exception from import
try:
    from public.geometric_object import GeometricObject
    from public.cone import Cone
    from public.cube import Cube
    from public.cylinder import Cylinder
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass

ANNO = "abstractmethod"


class TestInheritance(TestCase):

    def test_geometric_obejct(self):
        try:
            sut = TestGeometricObject()
        except:
            m = "@@Anonymous subclass of GeometricObject cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(
            sut, ABC, "@@GeometricObject does not extend ABC.@@")

    def test_cone(self):
        try:
            sut = Cone(2, 5, 3, "red", True)
        except:
            m = "@@Cone cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(sut, GeometricObject,
                              "@@Cone does not extend GeometricObject.@@")

    def test_cube(self):
        try:
            sut = Cube(6, "blue", False)
        except:
            m = "@@Cube cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(
            sut, GeometricObject, "@@Cube does not extend GeometricObject.@@")

    def test_cylinder(self):
        try:
            sut = Cylinder(3.9, 61, "black", True)
        except:
            m = "@@Cylinder cannot be instantiated.@@"
            self.fail(m)
        self.assertIsInstance(sut, GeometricObject,
                              "@@Cylinder does not extend GeometricObject.@@")

    def test_for_abstract_method_annotations(self):
        with open("public/geometric_object.py") as f:
            tree = ast.parse(f.read())

            # print(ast.dump(tree))

            v = ABCTestVisitor()
            v.visit(tree)

            for name in ["get_area", "get_volume"]:
                if name not in v.annotated_methods:
                    m = "@@The method '{}' lacks the required annotation '{}'.@@".format(
                        name, ANNO)
                    self.fail(m)


class ABCTestVisitor(ast.NodeVisitor):

    def __init__(self):
        self.annotated_methods = []

    def visit_FunctionDef(self, node):
        for d in node.decorator_list:
            if d.id == ANNO:
                self.annotated_methods.append(node.name)


class TestGeometricObject(GeometricObject):
    def __init__(self):
        self.set_color("red")
        self.set_filled(True)

    def get_area(self): pass
    def get_volume(self): pass