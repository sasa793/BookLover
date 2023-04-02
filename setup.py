from setuptools import setup

setup(name= 'booklover_package',
      version= '1.0.0',
      url= 'https://github.com/sasa793/BookLover',
      author= 'Sarah Elmasry',
      author_email= 'sme5qyx@virginia.edu',
      description= 'M09 HW assignment containing a Booklover class that contains methods and information about a specific  persons book experience. Whether it is their favorite, the number read, the name, or rating, etc.',
      packages = ['booklover_package'],
      install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'pandas'],)

