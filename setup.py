import setuptools
import os, platform

if platform.system() == 'Darwin':
    setuptools.setup(
        name="eats_worm",
        version="0.0.3",
        author="Steven Ban",
        author_email="ban.steven1337@gmail.com",
        description="Method for extracting GCaMP signal from volumetric imaging recordings",
        long_description_content_type=open('README.md').read(),
        url="",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            'numpy>=1.22.4',
            'scipy>=1.0.0',
            'tifffile>=2022.5.4',
            'opencv-python-headless>=4.1.0.25',
            'matplotlib>=2.1.0',
            'improc @ git+https://github.com/focolab/image-processing',
            'npex @ git+https://git@github.com/focolab/npex', 
            'imreg_dft',
            'fastcluster',
            'pyqt6', 
            'napari[pyqt6_experimental]',
            'pyqtgraph==0.13',
            'magicgui',
            'pandas>=1.4.2',
            'scikit-image',
            'xmltodict',
            'pynwb',
            'nwbinspector',
            'dandi'
        ], 
        dependency_links=['https://github.com/matejak/imreg_dft/tarball/master#egg=imreg_dft'],
        python_requires='<3.11'
    )

else:
    setuptools.setup(
        name="eats_worm",
        version="0.0.3",
        author="Steven Ban",
        author_email="ban.steven1337@gmail.com",
        description="Method for extracting GCaMP signal from volumetric imaging recordings",
        long_description_content_type=open('README.md').read(),
        url="",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            'numpy>=1.22.4',
            'scipy>=1.0.0',
            'tifffile>=2022.5.4',
            'opencv-python-headless>=4.1.0.25',
            'matplotlib>=2.1.0',
            'improc @ git+https://github.com/focolab/image-processing',
            'npex @ git+https://git@github.com/focolab/npex', 
            'imreg_dft',
            'fastcluster',
            'napari[all]',
            'pyqtgraph==0.13',
            'magicgui',
            'pandas>=1.4.2',
            'scikit-image',
            'xmltodict',
            'pynwb',
            'nwbinspector',
            'dandi'
        ], 
        dependency_links=['https://github.com/matejak/imreg_dft/tarball/master#egg=imreg_dft'],
        python_requires='<3.11'
    )
