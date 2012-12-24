import os

if os.environ.get('USE_SETUPTOOLS'):
    from setuptools import setup
    setup_kwargs = dict(zip_safe=0)

else:
    from distutils.core import setup
    setup_kwargs = dict()

import twisted
from twisted.python.versions import Version


if Version('twisted', 10, 1, 0) < twisted.version:
    raise Exception('Your version of twisted already has this library')

NAME = 'python-twisted-endpoints'
VERSION = '11.1.0'
DOCSTR = "%s-%s" % (NAME,VERSION)
#write our setup.cfg
open('setup.cfg','w').write("""[install]
install-lib = %s
install-data = /usr/share/doc/%s 
""" % (os.path.sep.join(twisted.__file__.split(os.path.sep)[:-2]), DOCSTR))

__doc__ = """
Implementations of L{IStreamServerEndpoint} and L{IStreamClientEndpoint} that
wrap the L{IReactorTCP}, L{IReactorSSL}, and L{IReactorUNIX} interfaces.
    
This also implements an extensible mini-language for describing endpoints,
parsed by the L{clientFromString} and L{serverFromString} functions.
    
@since: 10.1

This library has been modified to work with older versions of twisted and is
not supported by the twisted upstream development team. Use at your own risk.
"""

setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/JustinVenus/twisted-endpoints',
    author='Justin Venus',
    author_email='justin.gmail.com',
    license='MIT',
    description='Twisted Endpoints Compatibility',
    long_description=__doc__,
    packages=[
        'twisted.internet',
        'twisted.internet.test',
    ],
    package_dir={'': 'lib'},
    data_files=['LICENSE','README.md'],
    scripts=[],
    **setup_kwargs
)
