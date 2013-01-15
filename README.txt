sparkl
======

about
-----

Provides sparklines. On the command line.

This sparklines project is inspired by, and being ported from, a similar project (<http://github.com/holman/spark>) by [@holman](http://github.com/holman).

installation
------------

`pip install sparkl`. Done.

usage
-----

Simply run `sparkl`, giving it a sequence of numbers (delimited by spaces, commas, or whatever you'd like).

    > sparkl 0 30 55 80 33 150
    ▁▂▃▅▂▇

Options and more at `sparkl -h`.

examples
--------

Magnitude of earthquakes over 1.0 in the last 24 hours:

    > curl http://earthquake.usgs.gov/earthquakes/catalogs/eqs1day-M1.txt --silent |
        sed '1d' |
        cut -d, -f9 |
        sparkl
    ▂▆▂▁▂▂▂▁▂▁▂▂▃▂▂▁▂▂▁▂▁▂▁▃▂▂▂▂▁▂▂▆▂▂▂▂▇▁▁▂▂▂▆▁▆▁▁▁▂▃▂▂▃▂▁▁▂▂▆▂▃▁▁▆▆▁▂▂▁▂▅▂▁▆▂▁▃▃▁▂▁▅▁▃▃▃▂▃▁▅▂▅▆▃▁▆▁▆▁

Number of characters in your last 50 commands:

    > history |
        awk '{ print length($0) }' |
        grep -Ev 0 |
        tail -n50 |
        sparkl
    ▂▄▁▁▆▅▇▂▅▇▄▂▄▇▄▇▇▁▁▂█▁▁▁▁▁▁▁▃▁▁▄▅▆▁▁▁▁▁▃▃▃▄▁▅▆▆▆▆▇

cool usage ideas
----------------

There's a [list of great command line sparkline usage](https://github.com/holman/spark/wiki/Wicked-Cool-Usage). And, you could always put it in your prompt...

    sparkl (master√ history: ▂▅▇▂) >

future?
-------

- have switch for allowing/forcing 0-based lines
- make logger use sparkl as module parameter
- allow sparkline to be turned 90 degrees clockwise into horizontal bar
  chart?
