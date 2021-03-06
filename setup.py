from setuptools import setup, find_packages

__version__ = 0.25
__doc__ = """Declarative GUIs"""

setup(
    name="gui_builder",
    version=__version__,
    description=__doc__,
    packages=find_packages(),
    install_requires=["six"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ],
)
