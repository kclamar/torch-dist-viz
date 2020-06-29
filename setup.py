from distutils.core import setup

setup(
    name='torchdistviz',
    version='0.0.1',
    packages=['torchdistviz'],
    url='https://github.com/kclamar/torch-dist-viz',
    license='MIT license',
    author='Ka Chung Lam',
    author_email='kclamar@connect.ust.hk',
    description='Interactive visualization of PyTorch distributions for Jupyter Notebook',
    requires=['ipywidgets', 'matplotlib', 'torch']
)
