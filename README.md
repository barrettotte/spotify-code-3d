# spotify-code-3d

Generate 3D-printable keychain thing for Spotify codes in one command.

I came across [this Thingiverse post](https://www.thingiverse.com/thing:4758473) and thought it'd be cool to
automate it. Additionally, I wanted a really small OpenSCAD project to work on.

TODO: add picture

## Requirements

- Python 3+
- OpenSCAD 2019.05+

## Usage

In Spotify, right click > Share > Copy Spotify URI

Example: Tool Lateralus - `spotify:album:5l5m1hnH4punS1GQXgEi3T`

`python3 spotify3dgen.py spotify:album:5l5m1hnH4punS1GQXgEi3T`

Then feed the `.stl` into a slicing program and print.

See [example/](example/) for example of generated files.

## Summary

- Get Spotify URI via stdin
- Request SVG from Spotify's site - [Spotify Codes](https://www.spotifycodes.com/#create)
- Clean up SVG and make background transparent
- Pass SVG path and additional parameters to OpenSCAD CLI
- Extrude SVG down into base OpenSCAD model

## References

- https://www.spotifycodes.com/#create
- Inspiration - https://www.thingiverse.com/thing:4758473
