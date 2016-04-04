# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 maria alas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_md5sum communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

import re

# Add your library functions here.


def md5sum_command(enode, _file, t=False, b=False, c=False, status=False,
                   w=False, quiet=False, strict=False, shell='bash'):
    """
    This function will execute md5sum command to get a string
    for compare files

    -file, this is the file, or directory file to be md5sum
    -b, --binary         read in binary mode
    -c, --check          read MD5 sums from the FILEs and check them
    -t, --text           read in text mode (default)

The following three options are useful only when verifying checksums:
      --quiet          don't print OK for each successfully verified file
      --status         don't output anything, status code shows success
      -w, --warn           warn about improperly formatted checksum lines

      --strict         with --check, exit non-zero for any invalid input

    """
    pass

    # Usually, the library functions use the parameters to build a command that
    # is to be sent to the enode, for example:
    #
    # command = 'md5sum file.txt'
    #
    # It will return an string
    #
    # enode('md5sum file.txt', shell=shell)

    arguments = locals()

    required_arg = ['file']

    optional_arg = {'t': '-t', 'b': '-b', 'c': '-c', 'status': '--status',
                    'w': '-w', 'quiet': '--quiet', 'strict': '--strict'}

    options = ''

    for key, value in list(arguments.items()):
        if value is True:
            options = '{0}{1} '.format(options, optional_arg.get(key))

    md5sum_cmd = 'md5sum {0}{1}'.format(options, _file)
    md5sum_response = enode(md5sum_cmd, shell=shell)
    md5sum_re = (
      r'(?P<data>\w*)\s+'
    )
    return_code = ''
    re_result = re.match(md5sum_re, md5sum_response)
    assert re_result
    result = re_result.groupdict()
    return result


__all__ = [
    'md5sum_command'
]
