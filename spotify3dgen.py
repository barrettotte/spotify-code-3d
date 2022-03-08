# Generate 3D-printable keychain thing for Spotify codes.

import os
import re
import requests
import sys
import xml.etree.ElementTree as ET

# web page constants - https://www.spotifycodes.com/#create
CODE_URL = 'https://www.spotifycodes.com/downloadCode.php'
CODE_WIDTH = 320
PX_TO_MM = 0.2645833333

# fetch spotify code SVG
def get_code_svg(spotify_uri):
    bg = 'FFFFFF'
    bar = 'black'

    target = requests.utils.quote(spotify_uri)
    req = f'{CODE_URL}?uri=svg%2F{bg}%2F{bar}%2F{CODE_WIDTH}%2F{target}'
    resp = requests.get(req)

    if resp.status_code != 200 or len(resp.content) == 0:
        raise Exception('Spotify codes request failed: ({}) - {}'.format(resp.status_code, req))

    # delete background from svg
    svg_raw = re.sub(' xmlns="[^"]+"', '', resp.content.decode()) # fix namespace
    svg = ET.fromstring(svg_raw)
    svg.remove(svg.find('rect'))
    return ET.tostring(svg)

def main():
    # TODO: command line args
    spotify_uri = 'spotify:album:5l5m1hnH4punS1GQXgEi3T'
    
    try:
        svg_data = get_code_svg(spotify_uri)
    except Exception as e:
        print(f'failed to fetch Spotify code SVG {e}')
        sys.exit(1)

    svg_out = spotify_uri.replace(':', '_') + '.svg'
    
    svg_out = 'test.svg' # TODO:
    print(f'{CODE_WIDTH * PX_TO_MM} pixels') # TODO:
    
    try:
        with open(svg_out, 'wb') as f:
            f.write(svg_data)
    except Exception as e:
        print(f'unexpected error {e}')
        sys.exit(2)
    finally:
        # if os.path.exists(svg_out):
        #     os.remove(svg_out)
        pass

    # TODO: check for openscad existence
    # TODO: launch separate process for openscad build, passing svg
    # TODO: output stl and where it was generated

if __name__ == "__main__": main()
