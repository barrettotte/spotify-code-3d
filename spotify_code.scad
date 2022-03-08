// base Spotify code tag
//
// command line args
//   svg_path   ; downloaded Spotify SVG
//   svg_width  ; width in pixels
//   svg_height ; height in pixels

$fn = 60;

// convert pixels to mm
function px_to_mm(px) = px * 0.2645833333;

// main module
module spotify_code(x, y, z, svg) {
    padding = 6;
    hole_r = 3;

    difference() {
        // base
        difference() {
            minkowski() {
                cube(size=[x + (padding * 2.5), y, z], center=true);
                cylinder(r=4, h=z, center=true);
            }
            // keychain hole
            translate([(x - hole_r + padding) / 2, 0, -5])
                cylinder(h=z * 2, r=hole_r);
        }
        // bars
        translate([-padding, 0, 0])
        linear_extrude(height=z) {
            import(file=svg_path, center=true, dpi=96);
        }
    }
}

spotify_code(px_to_mm(svg_width), px_to_mm(svg_height), 5, svg_path);
