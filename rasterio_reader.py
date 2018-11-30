import rasterio

def rasterio_reader(inputTIF):
	with rasterio.open(inputTIF) as src:
		image = src.read(1)
		image_meta = src.meta.copy()
	return image, image_meta
