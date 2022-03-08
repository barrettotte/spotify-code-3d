// base Spotify code tag

$fn = 60;

module spotify_code(x, y, z) {
    margin_left = 6;
    keychain_r = 4;

    difference() {
        // base
        difference() {
            minkowski() {
                cube(size=[x + margin_left, y, z], center=true);
                cylinder(r=4, h=z, center=true);
            }
            translate([(-x/2 - keychain_r/2 + margin_left*0.75), 0, -5]) cylinder(h=z*2, r=keychain_r);
        }
        // bars
        translate([margin_left, 0, 0])
        linear_extrude(height=z) {
            import(file = "test.svg", center = true, dpi = 96);
            // TODO: file arg
        }
    }
}

w = 84.666666656; // TODO: arg
h = 21.166666667; // TODO: arg
spotify_code(w,20,5);

// openscad -o test.stl base.scad
// openscad -o output.stl -D "model=\"input.stl\"" test.scad
