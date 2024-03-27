# python3.8 deepliif_getScores.py $im_DIR $seg_DIR $marker_DIR $seg_thresh $size_thresh $size_thresh_upper $marker_thresh $resolution $output_dir
# python3 deepliif_getScores.py im/ seg/ None 150 auto None auto None .

# from deepliif.postprocessing import compute_results
from compute_functions import compute_results
import tifffile as tiff
import imageio as iio
import pandas as pd

import sys
from glob import glob
import pathlib

im_dir = sys.argv[1]
seg_dir = sys.argv[2]
marker_dir = sys.argv[3]
seg_thresh = sys.argv[4]
size_thresh = sys.argv[5]
size_thresh_upper = sys.argv[6]
marker_thresh = sys.argv[7]
resolution = sys.argv[8]
out_dir = sys.argv[9]

image_path = glob(f'{im_dir}/*')[0]
seg_path = glob(f'{seg_dir}/*')[0]
try:
    marker_path = glob(f'{marker_dir}/*')[0]
    marker = tiff.imread(marker_path)
except:
    marker_path = None
    marker = None
    marker_thresh = None

print(f''' ******* Using the following settings ********
        Original image: {image_path}
        Segmentation image: {seg_path}
        Marker image: {marker_path}
        Segmentation threshold: {seg_thresh}
        Size threshold: {size_thresh}
        Size threshold (upper): {size_thresh_upper}
        Marker threshold: {marker_thresh}
        Resolution: {resolution}
        ''')

orig =  tiff.imread(image_path)
file_extension = pathlib.Path(seg_path).suffix
if file_extension == '.png':
    seg = iio.imread(seg_path)
else:
    seg = tiff.imread(seg_path) # omg.tiff for WSI

if size_thresh != 'auto':
    size_thresh = int(size_thresh)
if marker_thresh != None:
    marker_thresh = int(marker_thresh)
if size_thresh_upper != 'None':
    size_thresh_upper = int(size_thresh_upper)
else:
    size_thresh_upper = None
if resolution == 'None':
    resolution = None

# size_thresh: Lower size threshold in pixels. Only include cells larger than this count.
# size_thresh_upper: Upper size threshold in pixels, or None. Only include cells smaller than this count.

overlay, refined, scoring = compute_results(orig, seg, marker, \
                                            resolution=resolution, \
                                            seg_thresh=int(seg_thresh), size_thresh=size_thresh, \
                                            marker_thresh=marker_thresh, size_thresh_upper=size_thresh_upper)
score_df = pd.DataFrame.from_dict(scoring, orient='index').T

score_df.to_csv(f'{out_dir}/results.csv', index=False)
