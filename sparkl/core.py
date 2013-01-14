#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

sparkl. http://github.com/philadams/sparkl
"""

import logging

ticks = u'▁▂▃▅▆▇'


def sparkl():
    import argparse

    # populate and parse command line options
    description = 'sparkl: sparklines on the command line.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.add_argument('--delimiter', '-d', default=' ')
    #parser.add_argument('--zero-min', '-z', default='' action='store_false')
    parser.add_argument('data', nargs=argparse.REMAINDER)
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

    # not yet implemented
    if args.delimiter is not ' ':
        raise NotImplementedError, '--delimiter/-d flag coming soon...'

    # TODO: zero-min or data-min?

    # bin data into ticks
    data = [int(i) for i in args.data]
    range_min = min(data)
    range_span = max(data) - range_min
    step = (range_span / float(len(ticks) - 1)) or 1
    sparkline = u''.join(ticks[int(round((i - range_min) / step))] for i in data)

    # print sparkline
    print(sparkline.encode('utf-8'))


if '__main__' == __name__:
    sparkl()
