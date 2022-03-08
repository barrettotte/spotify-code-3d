# Generate 3D-printable keychain thing for Spotify codes.
import os, re, requests, subprocess, sys
import xml.etree.ElementTree as ET

# fetch spotify code SVG
def get_code_svg(spotify_uri, width):
    target = requests.utils.quote(spotify_uri)
    req = f'https://www.spotifycodes.com/downloadCode.php?uri=svg%2FFFFFFF%2Fblack%2F{width}%2F{target}'
    resp = requests.get(req)

    if resp.status_code != 200 or len(resp.content) == 0:
        raise Exception('Spotify codes request failed: ({}) - {}'.format(resp.status_code, req))
    
    # delete background from svg
    svg_raw = re.sub(' xmlns="[^"]+"', '', resp.content.decode()) # fix namespace
    svg = ET.fromstring(svg_raw)
    svg.remove(svg.find('rect'))
    return ET.tostring(svg)

def main():
    try:
        svg_out = None
        svg_size = [320, 80]

        if len(sys.argv) != 2:
            raise ValueError('Usage: py spotify3dgen.py SPOTIFY_URI')
        spotify_uri = sys.argv[1]

        if not spotify_uri.startswith('spotify'):
            raise ValueError("Invalid Spotify URI. Expected to start with 'spotify:'")

        spotify_file = spotify_uri.replace(':', '_')
        svg_out =  spotify_file + '.svg'
        with open(svg_out, 'wb') as f:
            f.write(get_code_svg(spotify_uri, svg_size[0])) # temp file

        print(f'Generating STL to {spotify_file}.stl using ${svg_out}')
        subprocess.run([
            'openscad', 
            '-o', f'{spotify_file}.stl', 
            '-D', f'svg_path="{svg_out}"',
            '-D', f'svg_width={svg_size[0]}',
            '-D', f'svg_height={svg_size[1]}',
            'spotify_code.scad'
        ])
    except Exception as e:
        print(f'Error generating 3D spotify code.\n{e}')
        sys.exit(1)
    finally:
        if svg_out and os.path.exists(svg_out):
            os.remove(svg_out)

if __name__ == "__main__": main()
