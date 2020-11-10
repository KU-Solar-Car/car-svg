SCALE = .27

def draw_tile(x, y):
	# Generate string to draw tile at specified x, y.

	return f"""<polygon points="{(9+x)*SCALE},{(0+y)*SCALE} {(100+x)*SCALE},{(0+y)*SCALE} {(109+x)*SCALE},{(9+y)*SCALE} {(109+x)*SCALE},{(100+y)*SCALE} {(100+x)*SCALE},{(109+y)*SCALE} {(9+x)*SCALE},{(109+y)*SCALE} {(0+x)*SCALE},{(100+y)*SCALE} {(0+x)*SCALE},{(9+y)*SCALE}" fill="#3b3c3e" />"""


def draw_group(x, y, rows, cols):
	# Generate string to draw tightly placed group at specified x, y.
	str = ""

	for i in range(rows):
		for j in range(cols):
			str = str + draw_tile(x+(j*109), y+(i*109)) + '\n'  # No scale on distance.

	return str


def draw_thick_row(x, y):
	str = ""
	# First column is only 2x2, an d we need special 2x3 case for the spacing, too.
	str = draw_group(x, y, 2, 2)
	str = str + draw_group(x+230, y, 2, 3)

	# All others are 3x2.
	for i in range(0, 8):
		str = str + draw_group(x+(339*i)+(569), y, 2, 3)

	return str


def draw_thin_row(x, y):
	str = ""
	str = draw_group(x, y, 1, 2)
	str = str + draw_group(x+230, y, 1, 3)
	for i in range(0, 8):
		str = str + draw_group(x+(339*i)+(569), y, 1, 3)

	return str


def draw_additional_groups(x, y):
	str = ""

	# First column.
	str = draw_group(x, y, 2, 2)
	str = str + draw_group(x+0, y+230, 3, 2)
	str = str + draw_group(x+0, y+569, 2, 2)

	# Second column.
	str = str + draw_group(x+230, y+192, 1, 1)
	str = str + draw_group(x+230, y+313, 3, 2)
	str = str + draw_group(x+230, y+652, 1, 1)

	return str


def draw():
	# Generate string to draw tile layout.
	top_padding = 30
	side_padding = 43

	# Main rows.
	str = draw_thick_row(side_padding, top_padding)
	str = str + draw_thick_row(side_padding, 230+top_padding)
	str = str + draw_thin_row(side_padding, 460+top_padding)
	str = str + draw_thick_row(side_padding, 581+top_padding)
	str = str + draw_thick_row(side_padding, 811+top_padding)

	# Additional rows up front.
	str = str + draw_additional_groups(3281+side_padding, 83+top_padding)

	return str


if __name__ == '__main__':
	start = """<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
 "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1045 298">\n<g style="height: 100%; width: 100%">"""

	image = """\n<image href="car.png" height="100%" width="100%"/>\n"""

	end = """</g></svg>"""

	with open('car.svg', 'w') as f:
		f.write(start)
		f.write(image)
		f.write(draw())
		f.write(end)
