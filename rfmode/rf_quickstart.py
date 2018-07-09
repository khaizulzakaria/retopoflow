'''
Copyright (C) 2018 CG Cookie
http://cgcookie.com
hello@cgcookie.com

Created by Jonathan Denning, Jonathan Williamson

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

import re
import bgl
import bpy
import random
from ..common.blender import show_blender_text
from ..options import options
from ..help import help_quickstart

class OpenQuickStart(bpy.types.Operator):
    """Open Quick Start Guide new window"""
    bl_idname = "wm.open_quickstart"
    bl_label = "Quick Start Guide"

    @classmethod
    def poll(cls, context): return True

    def execute(self, context):
        self.openTextFile()
        return {'FINISHED'}

    def openTextFile(self):
        # simple processing of help_quickstart
        t = help_quickstart
        t = re.sub(r'^\n*', r'', t)         # remove leading newlines
        t = re.sub(r'\n*$', r'', t)         # remove trailing newlines
        t = re.sub(r'\n\n+', r'\n\n', t)    # make uniform paragraph separations
        ps = t.split('\n\n')
        l = []
        for p in ps:
            if p.startswith('- '):
                l += [p]
                continue
            lines = p.split('\n')
            if len(lines) == 2 and (lines[1].startswith('---') or lines[1].startswith('===')):
                l += [p]
                continue
            l += ['  '.join(lines)]
        t = '\n\n'.join(l)

        # play it safe!
        if options['quickstart_filename'] not in bpy.data.texts:
            # create a log file for error writing
            bpy.data.texts.new(options['quickstart_filename'])
        # restore data, just in case
        txt = bpy.data.texts[options['quickstart_filename']]
        txt.from_string(t)
        txt.current_line_index = 0

        show_blender_text(options['quickstart_filename'])
