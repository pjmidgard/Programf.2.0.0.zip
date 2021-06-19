import numpy as np
from mtscomp import Writer, Reader

# Define a writer to compress a flat raw binary file.
w = Writer(chunk_duration=1.)
# Open the file to compress.
w.open('data.bin', sample_rate=30000., n_channels=385, dtype=np.int16)
# Compress it into a compressed binary file, and a JSON header file.
w.write('data.cbin', 'data.ch')
w.close()

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
