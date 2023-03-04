Tutorial: Brain View
===========================
![example](https://user-images.githubusercontent.com/90367338/222876164-ec73f654-1239-4870-a95b-eb46fa30933f.png)
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
![Screenshot 2023-03-03 at 10 39 24 PM](https://user-images.githubusercontent.com/90367338/222876172-55e4f318-3795-49a9-90dd-31af9230c395.png)

   (2) Then in BrainNet Viewer, click File > Load File. In "Surface file", browse and choose "./data/surface.nv"; in "Node file", browse and choose the node file you just generated (example: "./output/example.node"); leave the rest two fields blank. Click "OK".
![Screenshot 2023-03-03 at 11 08 14 PM](https://user-images.githubusercontent.com/90367338/222876199-b6aba102-c8a7-4bdd-b01c-169e64af3830.png)

   (3) You may modify the settings under the left-side tabs. (Typically, you can modify the color and size features under the "Node" tab. Here, for example, we set Node > Color > Colormap to "Jet"). Then click "OK".
![Screenshot 2023-03-03 at 11 22 15 PM](https://user-images.githubusercontent.com/90367338/222876218-c797fe79-4fa3-4e95-a142-4add4753e3e9.png)
![Screenshot 2023-03-03 at 11 22 35 PM](https://user-images.githubusercontent.com/90367338/222876222-7ebdaccc-dca6-4815-b8f3-c8c139dc603c.png)

   (4) Click "Save Figure" to save the generated brain view plot. (In the example case, since the size array are set the same, we have balls in the figure with the same size)
![Screenshot 2023-03-03 at 11 22 51 PM](https://user-images.githubusercontent.com/90367338/222876228-18a600bf-c03b-4ca7-87f1-d5a2a4c431a3.png)
 

3. Install MATLAB (Optional)
   
   Wake Forest students have free access to download and use MATLAB. To learn more, please visit https://software.wfu.edu/download/matlab/.


# 2 Contacts


Please email chenm@wfu.edu




