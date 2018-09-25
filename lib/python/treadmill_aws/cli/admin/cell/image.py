"""Admin module to manage cell AMIs.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import click

from treadmill import admin
from treadmill import context


_LOGGER = logging.getLogger(__name__)


def init():
    """Admin Cell CLI module"""

    @click.command(name='image')
    @click.option('--image', help='AMI image.')
    def image_cmd(image):
        """Configure cell AMI image."""
        admin_cell = admin.Cell(context.GLOBAL.ldap.conn)
        cell = admin_cell.get(context.GLOBAL.cell)
        data = cell.get('data', {})
        if image:
            data['image'] = image

        admin_cell.update(context.GLOBAL.cell, {'data': data})
        print(data.get('image', ''))

    return image_cmd
