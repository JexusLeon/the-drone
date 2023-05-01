import setuptools

import versioneer

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [line.strip() for line in fh]

# Setting up
setuptools.setup(
    name='the_drone',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Jesus Leandro Leon',
    author_email='<jexusleandro@gmail.com>',
    description='Focuses on creating useful functions for drones.',
    python_requires='>=3.10',
    keywords=['python'],
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
