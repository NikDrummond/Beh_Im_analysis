from setuptools import setup, find_packages
import re

VERSIONFILE = "Beh_Im_analysis/__init__.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RunTimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    requirements = [l for l in requirements if not l.startswith('#')]

setup(name = 'Beh_Im_analysis',
    version = verstr,
    description = 'Code for behavioural analysis from Zlatic lab',
    url = 'https://github.com/NikDrummond/Beh_Im_analysis',
    author = ['Nadine Randal', 'Nik Drummond'],
    author_email = 'nikolasdrummond@gmail.com',
    packages = find_packages(),
    zip_safe = False
)
