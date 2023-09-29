# Projected Area Calculator

This repository includes a Python script for computing the projected area of a 3D mesh along the translational axes of surge, sway, and heave.

The area is computed by projecting the mesh triangles onto a 2D plane, computing the union of all of the 2D triangles, and then taking the area of the resulting polygon.


## Usage Example

    $ python3 -m pip install -r requirements.txt
    $ python3 projected_area.py models/cylinder.stl
    volume = 6.242890110933359
    approximate area = 3.3904483048691634
    surge X projected area = 4.0
    sway  Y projected area = 4.0
    heave Z projected area = 3.1214450554666797
