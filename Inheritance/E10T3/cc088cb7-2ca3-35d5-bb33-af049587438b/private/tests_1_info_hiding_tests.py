#!/usr/bin/env python3

from unittest import TestCase
import ast, types

# catch potential exception from import
try:
    from public.onsite_restaurant import OnsiteRestaurant
    from public.delivery_restaurant import DeliveryRestaurant
    from public.restaurant import Restaurant
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass

INSTANCES = [
    OnsiteRestaurant("osr", "all cuisine", 20),
    DeliveryRestaurant("dr", "all cuisine", 30),
    Restaurant("r", "all cuisine")
]
TYPES = {
    OnsiteRestaurant: "public/onsite_restaurant.py",
    DeliveryRestaurant: "public/delivery_restaurant.py",
    Restaurant: "public/restaurant.py",
}


# utility
def get_non_method_members(ts):
    if type(ts) == type:
        ts = [ts]
    class_members = []
    for t in ts:
        for attr_name in dir(t):
            attr = getattr(t, attr_name)
            if isinstance(attr, types.MethodType) or isinstance(attr, types.FunctionType):
                continue
            class_members.append(attr_name)
    return class_members


class PrivateInformationHidingTestSuite(TestCase):

    def test_instance_variables(self):
        for instance in INSTANCES:
            static = get_non_method_members(type(instance))
            for attr_name in dir(instance):
                if attr_name.startswith("_"):
                    continue
                if type(getattr(instance, attr_name)) == types.MethodType:
                    continue
                if attr_name in static:
                    continue
                m = "@@Classes should hide implementation details. The variable '{}' in type '{}' " \
                    "does not need to be public.@@"
                m = m.format(attr_name, type(instance).__name__)
                self.fail(m)

    def test_global_state(self):
        for t in TYPES:
            path = TYPES[t]
            with open(path) as f:
                tree = ast.parse(f.read())
                v = SolutionVisitor()
                v.visit(tree)

                m = "@@Class state should be self-contained, yet, at least " +\
                    "one variable in '{}' is defined in the global scope.@@"
                m = m.format(t.__name__)
                self.assertFalse(v.hasAssignInGlobalScope, m)

    def test_static_variables(self):
        predef = get_non_method_members([object, TestCase]) # built-int type + imported type
        for t in TYPES:
            for attr_name in get_non_method_members(t): # attributes of the _class_
                if attr_name in predef:
                    continue
                m = "@@Object instances should be independent, yet, the variable " \
                    "'{}' in '{}' is defined as a shared class variable.@@"
                m = m.format(attr_name, t.__name__)
                self.fail(m)


class SolutionVisitor(ast.NodeVisitor):

    def __init__(self):
        self.hasAssignInGlobalScope = False

    def visit_If(self, node):
        try:
            if node.test.left.id == "__name__":
                return
        except:
            self.generic_visit(node)

    def visit_Assign(self, node):
        self.hasAssignInGlobalScope = True

    def visit_FunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return
