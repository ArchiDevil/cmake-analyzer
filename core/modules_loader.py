import os
import importlib
import sys
import inspect
import fnmatch

import core.module_base


class ModulesLoader(object):
    def __init__(self, modules_path, filters=['*']):
        self.modules_path = modules_path
        self.modules = []
        self.checkers = []
        self.filters = filters
        self.__load_modules()

    def __load_checkers(self, module):
        classes = inspect.getmembers(module, inspect.isclass)
        for _, class_type in classes:
            if class_type.__bases__[0] == core.module_base.SingleFileChecker:
                class_object = class_type()
                self.checkers.append(class_object)
                
    def __match_filters(self, filename):
        for filter_ in self.filters:
            match_result = fnmatch.fnmatch(filename, filter_)
            if not match_result:
                return False
        return True

    def __load_modules(self):
        sys.path.append(self.modules_path)
        for filename in os.listdir(self.modules_path):
            if not self.__match_filters(filename):
                continue

            if not filename.endswith('.py'):
                continue

            module = importlib.import_module(os.path.splitext(filename)[0])
            self.modules.append(module)
            self.__load_checkers(module)

    @property
    def loaded_modules(self):
        return self.modules

    @property
    def loaded_checkers(self):
        return self.checkers
