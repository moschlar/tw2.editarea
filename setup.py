from setuptools import setup, find_packages

setup(
    name='tw2.editarea',
    version='0.1',
    description='ToscaWidgets2 widget for EditArea, a JavaScript-based source code editor',
    long_description=open('README.rst').read(),
    author='Moritz Schlarb',
    author_email='mail@moritz-schlarb.de',
    url='https://github.com/moschlar/tw2.editarea',
    license='WTFPL-2',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.editarea
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
