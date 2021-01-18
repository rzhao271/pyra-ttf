# Pyra TTF

[![Travis (.com) branch](https://img.shields.io/travis/com/rzhao271/pyra-ttf/main)](https://travis-ci.com/github/rzhao271/pyra-ttf)

## About

Pyra TTF, or Pyraminx Tip-to-Face, is an application that takes pyraminx algorithms in WCA notation, and converts them to face-turning algorithms.

The original purpose of the application was to generate algorithms that can be applied to the cell-turning 4D pyraminx in MC4D, but it turns out that there is a way to solve it without resorting to RKT: [https://www.rayzz.me/articles/hypercubing/4-simplex-solution.html](https://www.rayzz.me/articles/hypercubing/4-simplex-solution.html).

## Requirements

- Python 3.8 or newer

## Example

Running

`python main.py "R U R' U R U R'"`

in a shell (assuming you're in the right directory) gives the output

`Lw Rw Dw' Fw Lw Dw Fw'`

Also included is a shell script so one can call `./pyrattf.sh "[algorithm]"` instead.

## Program Limitations

The algorithm must only contain moves that are either

- Part of valid [WCA Pyraminx notation](https://www.worldcubeassociation.org/regulations/#12e), though X2, X'2, and X2' moves are allowed, OR
- Face turns, such as Lw, Rw, Fw, and Dw

separated by spaces. Note that rotations are not allowed in the input.
