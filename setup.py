from setuptools import setup, find_packages

version = '0.1'

setup(
    name='slc.quickchangenote',
    version=version,
    description="Provide an auto-complete Change Note field for CMFEditions",
    long_description=open("README.txt").read() + "\n" +
                    open("HISTORY.txt").read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='CMFEditions flexbox',
    author='Izak Burger, Syslab.com GmbH',
    author_email='isburger@gmail.com',
    url='https://github.com/syslabcom/slc.quickchangenote',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir = {'' : 'src'},
    namespace_packages=['slc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
    setup_requires=["PasteScript"],
    paster_plugins = ["ZopeSkel"],
    )
