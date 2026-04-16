import svgwrite

def export_svg(contours, filename):
    svg_image = svgwrite.Drawing()
    coord_list = []
    for contour in contours:
        x = contour[:,1]
        y = contour[:,0]    
        coord_list = zip(x,y)
        line = svg_image.polyline(coord_list)
        svg_image.add(line)
        
    
    svg_image.saveas(f"{filename}")



