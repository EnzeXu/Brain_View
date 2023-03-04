Tutorial: Brain View
===========================

===========================

# Catalog


* [1 Getting started](#1-getting-started)

* [2 Contacts](#2-contacts)


****


# 1 Getting started

1. Data Prepare

   (1) Prepare a color (value) array and a size array in Python. They can be either `list` or `numpy.ndarray` instances.

   (2) Call the `build_txt()` function in `utils.py` to easily generate a .node file with `160` rows and `6` columns. Elements in one row are split by space. Each element can be an integer or float number.

   Example: file `output/example.node`.

2. Launch BrainNet Viewer in MATLAB

   (1) In MATLAB, open BrainNetViewer/BrainNet.m. Then run it.

   ```shell
   >> BrainNet
   Please cite:
   Xia M, Wang J, He Y (2013) BrainNet Viewer: A Network Visualization Tool for Human Brain Connectomics. PLoS ONE 8: e68910.
   An example:
   'The brain networks were visualized with the BrainNet Viewer (http://www.nitrc.org/projects/bnv/) (Xia et al., 2013)'.
   ```

   (2) Then in BrainNet Viewer, click File > Load File. In "Surface file", browse and choose "./data/surface.nv"; in "Node file", browse and choose the node file you just generated (example: "./output/example.node"); leave the rest two fields blank. Click "OK".

   (3) You may modify the settings under the left-side tabs. (typically, you can modify the color and size features under the "Node" tab). Then click "OK".

   (4) Click "Save Figure" to save the generated brain view plot. (In the example case, since the size array are set the same, we have balls in the figure with the same size)

3. Install MATLAB (Optional)
   
   Wake Forest students have free access to download and use MATLAB. To learn more, please visit https://software.wfu.edu/download/matlab/.


# 2 Contacts


Please email chenm@wfu.edu




