# From the package swampy, take the module World and import the class World
from swampy.World import World


class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, color, corner
    """


class Circle(object):
    """Represents a circle.

    attributes: point, radius
    """


class Polygon(object):
    """Represents a polygon.

    attributes: a list of point objects
    """


def create_canvas(world, w, h, my_background):
    my_canvas = world.ca(width=w, height=h, background=my_background)
    return my_canvas


def create_rectangle(height, width, color):
    my_rect = Rectangle()
    my_rect.width = width
    my_rect.height = height
    my_rect.corner = Point()
    my_rect.corner.x = 0.0
    my_rect.corner.y = 0.0
    my_rect.color = color
    return my_rect


def bbox(rectangle):
    """Return a list of lists, with individual lists containing coordinates."""
    p1 = [rectangle.corner.x, rectangle.corner.y]

    p2 = [rectangle.corner.x + rectangle.width,
          rectangle.corner.y + rectangle.height]

    return [p1, p2]


def draw_rectangle(canvas, rectangle, my_bbox=None):
    if not bbox:
        my_bbox = bbox(rectangle)

    canvas.rectangle(my_bbox, outline='black', width=2, fill=rectangle.color)


def draw_point(canvas, point):

    draw_point_rect = create_rectangle(3, 3, 'black')

    draw_point_rect.corner.x = point.x
    draw_point_rect.corner.y = point.y

    draw_bbox = [[point.x + 1, point.y + 1], [point.x - 1, point.y - 1]]
    draw_rectangle(canvas, draw_point_rect, draw_bbox)


def create_circle(point, radius, fill):

    my_circle = Circle()
    my_circle.fill = fill
    my_circle.radius = radius
    my_circle.point = point
    return my_circle


def draw_circle(canvas, circle):

    circle_tuple = (circle.point.x, circle.point.y)

    canvas.circle(circle_tuple, circle.radius, circle.fill)


def gen_point_list(polygon):
    # Create a list of lists based on points in a Polygon object.
    master_point_list = []
    # vars(polygon) is a dictionary with keys being point names
    # and the values being point objects
    # points_list = polygon.points
    # print "Our points list is ", points_list
    for point_object in polygon.points:
        # Create a list based on specific points_dict item
        # print point_object
        master_point_list.append([point_object.x, point_object.y])
    # print "Our master point_list is ", master_point_list
    return master_point_list


def draw_polygon(canvas, polygon):
    """Draw a specified polygon object on the canvas."""

    # The polygon object has points, we need to make those points a list.
    points_list = gen_point_list(polygon)

    # Now that we have the points_list, we can draw the polygon
    canvas.polygon(points_list, fill=polygon.fill)


def main():
    # Create World object
    # print  sys.version_info
    world = World()
    # Create our canvas
    canvas = create_canvas(world, 500, 500, 'grey')
    # canvas = world.ca(width=500, height=500, background='white')
    # Create our rectangle
    my_rect = create_rectangle(100, 200, 'blue')
    # Create a new Point object
    new_point = Point()
    # Put new point at 0,0
    new_point.x = -30
    new_point.y = -30

    draw_point(canvas, new_point)

    my_circle = create_circle(new_point, 5, 'green')
    # draw_circle(canvas, my_circle)

    my_circle = create_circle(new_point, 30, 'red')
    # draw_circle(canvas, my_circle)


    # Polygon are made of points, so we should create a list of points
    point_a = Point(-100, -100)
    point_b = Point(50, 0)
    point_c = Point(-100, 100)

    my_points = (point_a, point_b, point_c)

    my_polygon = Polygon()
    # Create an attribute that is a list
    my_polygon.points = []
    # Append our point objects to the Polygon object's list
    my_polygon.points.append(point_a)
    my_polygon.points.append(point_b)
    my_polygon.points.append(point_c)

    # Add fill color attribute
    my_polygon.fill = 'blue'

    # After the polygon has all the points in question, we need a "draw_polygon"
    # function.
    draw_polygon(canvas, my_polygon)

    # Polygon are made of points, so we should create a list of points
    point_a = Point(-100, -100)
    point_b = Point(50, 0)
    point_c = Point(200, 0)
    point_d = Point(200,-100)
    my_points = (point_a, point_b, point_c, point_d)
    
    my_polygon = Polygon()
    # Create an attribute that is a list
    my_polygon.points = []
    # Append our point objects to the Polygon object's list
    my_polygon.points.append(point_a)
    my_polygon.points.append(point_b)
    my_polygon.points.append(point_c)
    my_polygon.points.append(point_d)
    
    # Add fill color attribute
    my_polygon.fill = 'red'
    # After the polygon has all the points in question, we need a "draw_polygon"
    # function.
    draw_polygon(canvas, my_polygon)


    # Polygon are made of points, so we should create a list of points
    point_a = Point(-100, 100)
    point_b = Point(50, 0)
    point_c = Point(200, 0)
    point_d = Point(200, 100)
    my_points = (point_a, point_b, point_c, point_d)
    
    my_polygon = Polygon()
    # Create an attribute that is a list
    my_polygon.points = []
    # Append our point objects to the Polygon object's list
    my_polygon.points.append(point_a)
    my_polygon.points.append(point_b)
    my_polygon.points.append(point_c)
    my_polygon.points.append(point_d)
    
    # Add fill color attribute
    my_polygon.fill = 'white'
    # After the polygon has all the points in question, we need a "draw_polygon"
    # function.
    draw_polygon(canvas, my_polygon)


    world.mainloop()


if __name__ == '__main__':
    main()
