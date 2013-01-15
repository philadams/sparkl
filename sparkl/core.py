#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

sparkl. http://github.com/philadams/sparkl
"""

import logging
import os
import fileinput

ticks = u'▁▂▃▅▆▇'


def sparkl():
    import argparse

    # populate and parse command line options
    description = 'sparkl: sparklines on the command line.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.add_argument('--delimiter', '-d', default=' ')
    #parser.add_argument('--zero-min', '-z', default=''
                         #action='store_false')
    parser.add_argument('data', nargs=argparse.REMAINDER,
                        default='-')
    args = parser.parse_args()

    # logging config
    log_level = logging.WARNING  # default
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    # main debuggery
    logging.debug('args: %s' % args.__repr__())

    data = []
    if os.isatty(0) and not args.data:
        parser.print_help()
        exit()
    if args.data:
        data = args.data
    else:
        data = [line.strip() for line in fileinput.input()]

    if len(data[0].split(args.delimiter)) > 1:
        data = [int(round(float(x.strip()))) for x in data[0].split(args.delimiter)]
    else:
        data = [int(round(float(x.strip()))) for x in data if x.strip() is not '']

    # TODO: zero-min or data-min?

    # bin data into ticks
    range_min = min(data)
    range_span = max(data) - range_min
    step = (range_span / float(len(ticks) - 1)) or 1
    sparkline = u''.join(ticks[int(round((i - range_min) / step))] for i in data)

    # print sparkline
    print(sparkline.encode('utf-8'))


if '__main__' == __name__:
    sparkl()
