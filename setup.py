import io
import os
import re
from setuptools import setup, find_packages

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
with open("src/automateboringstuff3/__init__.py", "r") as fileObj:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fileObj.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name='automateboringstuff3',
    version=version,
    url='https://github.com/asweigart/automateboringstuff3',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('This package installs the modules used in "Automate the Boring Stuff with Python", 3rd Edition.'),
    long_description=long_description,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license='BSD',
    install_requires=[
        'send2trash==1.8.3',
        'requests==2.32.3',
        'beautifulsoup4==4.12.3',
        'selenium==4.23.1',
        'openpyxl==3.1.5',#'openpyxl==3.1.0',
        'PyPDF==4.3.1',#'PyPDF2==3.0.1',
        'pdfminer.six==20240706',
        'python-docx==1.1.2',#'python-docx==0.8.11', # not updated since May 2021
        #'imapclient==2.3.1', # not updated since Jul 2022
        #'pyzmail36==1.0.4',
        #'twilio',
        'pillow==10.4.0', # 9.0.0 dropped support for 3.6
        'playwright==1.45.1',
        'playsound==1.3.0',
        'xmltodict==0.13.0',
        'PyYAML==6.0.2',
        'tomli_w==1.0.0',
        'matplotlib==3.9.0',
        'pytesseract==0.3.10',
        'pyttsx3==2.90',

        # These modules always have the latest version installed.
        'ezgmail',
        'ezsheets',
        'pyautogui',
        'pyperclip',
        'humre',
        'bext',
        'pymsgbox',
        'pyperclipimg',

    ],
    keywords="automate boring stuff python",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',

    ],
)

