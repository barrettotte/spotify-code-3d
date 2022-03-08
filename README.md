# spotify-code-3d

Generate 3D-printable keychain thing for Spotify codes in one command.

I came across [this Thingiverse post](https://www.thingiverse.com/thing:4758473) and thought it'd be cool to
automate it. Additionally, I wanted a really small OpenSCAD project to work on.

## Requirements

- Python 3+
- OpenSCAD 

## Usage

In Spotify, right click > Share > Copy Spotify URI

Example: Tool Lateralus - `spotify:album:5l5m1hnH4punS1GQXgEi3T`

`python3 spotify3dgen.py spotify:album:5l5m1hnH4punS1GQXgEi3T`

See [example/](example/) for example of generated files.

## References

- https://www.spotifycodes.com/#create
