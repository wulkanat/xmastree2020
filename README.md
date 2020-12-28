# SDF Christmas Tree

This is in principle a renderer that outputs to a volumetric display.

## Video by Stand-up Maths
[![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOVF.vsBC0xwnkS1%252flZVMb22DIA%26pid%3DApi&f=1)](https://www.youtube.com/watch?v=TvlpIojusBE)

## Instructions

To render this on your local machine
* [Open3D](http://www.open3d.org/docs/release/getting_started.html) `conda install -c open3d-admin open3d`
* `numpy`
* Stuff I forgot

Run `test_render.py`

*Note: this program blocks the window close button, and I am too lazy to fix it. Know how to force close it*

Admire the preview.

To change the rendered scene, go to the top of the file and change this line
```python
from scenes.[SCENE_NAME] import render_point, tick, set_palette_mode
```

## Demo of scenes

### Growing Sphere

![](https://cdn.discordapp.com/attachments/516304581517377587/793222931328663562/anim.gif)

