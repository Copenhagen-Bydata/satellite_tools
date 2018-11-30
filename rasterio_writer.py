# data must be a valid NumPy array

def rasterio_writer(outputLocation, data, metadata):
  with rasterio.open(outputLocation, 'w', **metadata) as dest:
		dest.write(data, 1)
