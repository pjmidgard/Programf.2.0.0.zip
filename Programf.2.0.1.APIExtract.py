import numpy as np
from mtscomp import Writer, Reader


# Define a reader to decompress a compressed array.
r = Reader()
# Open the compressed dataset.
r.open('data.cbin', 'data.ch')
# The reader can be sliced as a NumPy array: decompression happens on the fly. Only chunks
# that need to be loaded are loaded and decompressed.
# Here, we load everything in memory.
array = r[:]
# Or we can decompress into a new raw binary file on disk.
r.tofile('data_dec.bin')
r.close()
