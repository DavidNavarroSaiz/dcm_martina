from rectangle_dimensions import RectangleDimensions


image_path = './compareimages/2junio_10x10.tiff'
mm_px = 0.2506
width = RectangleDimensions(image_path)
width.evaluate_image(mm_px)