# SPDX-FileCopyrightText: 2021 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

import warnings
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("openstf_dbc")
except PackageNotFoundError:
    # package is not installed
    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("Singleton call")
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        if len(args) or len(kwargs):
            warnings.warn("Singleton class already initialized, arguments are ignored")
        return cls._instances[cls]

    @classmethod
    def get_instance(cls, instance_cls):
        return cls._instances[instance_cls]
