#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File name: setup.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg and avconv.
#   Copyright 2015-2016 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module defines the installation script for VideoMorph."""

from setuptools import setup, find_packages

from videomorph.videomorph import VERSION
from videomorph.videomorph import PACKAGE_NAME


LONG_DESC = """Small Video Converter based on ffmpeg, Python 3 and Qt5.
Unlike other video converters, VideoMorph focuses on a single task,
convert video, making it simple, easy to use and allowing the user
choose from a list of popular video formats.

VideoMorph UI is simple and clean focused on usability, eliminating
annoying options rarely used.
Videomorph is a video converter, just that. If you want a video
editor, VideoMorph isn't for you.
"""


if __name__ == '__main__':
    setup(name=PACKAGE_NAME,
          version=VERSION,
          description='Small Video Converter based on ffmpeg, '
                      'Python 3 and Qt5, focused on usability.',
          long_description=LONG_DESC,

          author='Ozkar L. Garcell',
          author_email='codeshard@openmailbox.org',
          maintainer='Leodanis Pozo Ramos',
          maintainer_email='lpozo@openmailbox.org',
          url='https://github.com/codeshard/videomorph',
          license='Apache License, Version 2.0',
          packages=find_packages(exclude=['tests', 'docs']),

          data_files=[
              # Desktop entry
              ('/usr/share/applications',
               ['share/applications/videomorph.desktop']),
              # App icon
              ('/usr/share/icons',
               ['share/icons/videomorph.png']),
              # App translation file
              ('/usr/share/videomorph/translations',
               ['share/videomorph/translations/videomorph_es.qm']),
              # Default conversion profiles
              ('/usr/share/videomorph/stdprofiles',
               ['share/videomorph/stdprofiles/profiles.xml']),
              # Documentation files
              ('/usr/share/doc/videomorph',
               ['README.md', 'LICENSE', 'AUTHORS',
                'copyright', 'changelog.gz', 'TODO'])
          ],

          scripts=['bin/videomorph']
         )
