from distutils.core import setup
setup(
  name = 'chorus_detection',
  packages = ['chorus_detection'], # this must be the same as the name above
  version = '0.1',
  description = 'Library to find the choruses and interesting segments of songs',
  author = 'Eronen A.',
 
  keywords = ['Chorus', 'Audio Signal Processing', 'Music'], # arbitrary keywords
  install_requires=[
    'Essentia',
    'numpy',
    'matplotlib',
    'scipy',
    'soundfile',
  ],
  classifiers = [],
)
