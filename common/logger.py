'''
Copyright (C) 2014 Plasmasolutions
software@plasmasolutions.de

Created by Thomas Beck
Donated to CGCookie and the world

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import bpy

from .blender import show_blender_popup, show_blender_text


class Logger:
    _log_filename = 'Logger'
    _divider = '=' * 80

    @staticmethod
    def set_log_filename(path):
        Logger._log_filename = path

    @staticmethod
    def get_log_filename():
        return Logger._log_filename

    @staticmethod
    def get_log(create=True):
        if Logger._log_filename not in bpy.data.texts:
            if not create:
                return None
            # create a log file for recording
            bpy.ops.text.new()
            bpy.data.texts[-1].name = Logger._log_filename
        return bpy.data.texts[Logger._log_filename]

    @staticmethod
    def add(line):
        log = Logger.get_log()
        log.write('\n\n%s\n%s' % (Logger._divider, str(line)))

    @staticmethod
    def open_log():
        if Logger.get_log(create=False):
            show_blender_text(Logger._log_filename)
        else:
            show_blender_popup('Log file (%s) not found' % Logger._log_filename)



