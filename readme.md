<h1 align = "center" > EditVideoTool </h1>


# 前置文档



# 依赖包
```shell
pip install moviepy==2.0.0.dev2
```
```shell
pip install opencv-python
```


# 功能
* **已实现**
  * `check_folder_path`方法：检查对应的文件是否存在，如不存在便自动创建
  * `check_video`，方法：检查视频尺寸比例、编码等格式是否符合规范，不符合规范的视频将会自动的放入`nonstandard`中
  * `video_ready`方法：枚举出符合规范的视频
  * `video_convert`方法：将原视频转换成符合规范的视频
    * 横板4k视频 - 横板4k视频
    * 横板4k视频 -> 竖版1080P视频（需要根据视觉人工判断裁剪范围）
    * 竖版1080P/2160P视频 ->  竖版1080P视频
  * `video_convert`方法：将原视频倒序并收尾拼接成一个新的前后可循环的视频
    * 需要人工判断哪些视频可循环，并将可循环视频手动的放进`loop`文件中
  * `video_to_icon`方法：根据视频输出对应的缩略图 
    * 横板视频 -> 缩略图 
    * 竖版视频 -> 缩略图 （需要根据视觉人工判断裁剪范围）
  <br> <br>


* **待实现**
  * p0：视频编码格式过滤
  * P1：分文件编写
  * P1：GUI
  * P2：打包发布
      

# 问题及解决方案
* 问题: 没有找到fx的相关函数，如编译报错: AttributeError: module 'moviepy.audio.fx.all' has no attribute 'audio_fadein'
* 解决方案:
  1. 在`C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\moviepy\video\fx\all`中找到并打开`__init__.py`文件
  2. 修改如下代码：
  ```python
  """
  Loads all the fx !
  Usage:
  import moviepy.video.fx.all as vfx
  clip = vfx.resize(some_clip, width=400)
  clip = vfx.mirror_x(some_clip)
  """
  
  # import pkgutil
  # 
  # import moviepy.video.fx as fx
  # 
  # __all__ = [name for _, name, _ in pkgutil.iter_modules(fx.__path__) if name != "all"]
  # 
  # for name in __all__:
  #     # exec("from ..%s import %s" % (name, name))
  #     print("from  moviepy.video.fx import %s" % (name))
  
  
  from moviepy.video.fx.accel_decel import accel_decel
  from moviepy.video.fx.blackwhite import blackwhite
  from moviepy.video.fx.blink import blink
  from moviepy.video.fx.colorx import colorx
  from moviepy.video.fx.crop import crop
  from moviepy.video.fx.even_size import even_size
  from moviepy.video.fx.fadein import fadein
  from moviepy.video.fx.fadeout import fadeout
  from moviepy.video.fx.freeze import freeze
  from moviepy.video.fx.freeze_region import freeze_region
  from moviepy.video.fx.gamma_corr import gamma_corr
  from moviepy.video.fx.headblur import headblur
  from moviepy.video.fx.invert_colors import invert_colors
  from moviepy.video.fx.loop import loop
  from moviepy.video.fx.lum_contrast import lum_contrast
  from moviepy.video.fx.make_loopable import make_loopable
  from moviepy.video.fx.margin import margin
  from moviepy.video.fx.mask_and import mask_and
  from moviepy.video.fx.mask_color import mask_color
  from moviepy.video.fx.mask_or import mask_or
  from moviepy.video.fx.mirror_x import mirror_x
  from moviepy.video.fx.mirror_y import mirror_y
  from moviepy.video.fx.painting import painting
  from moviepy.video.fx.resize import resize
  from moviepy.video.fx.rotate import rotate
  from moviepy.video.fx.scroll import scroll
  from moviepy.video.fx.speedx import speedx
  from moviepy.video.fx.supersample import supersample
  from moviepy.video.fx.time_mirror import time_mirror
  from moviepy.video.fx.time_symmetrize import time_symmetrize
  ```
  解决方案：
  1. 在`C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\moviepy\audio\fx\all`找到并打开`__init__.py`文件
  2. 修改如下代码：
     ```python
     """
     Loads all the fx!
     Usage:
     import moviepy.audio.fx.all as afx
     audio_clip = afx.volume_x(some_clip, .5)
     """
    
     # import pkgutil
     # 
     # import moviepy.audio.fx as fx
    
     # __all__ = [name for _, name, _ in pkgutil.iter_modules(fx.__path__) if name != "all"]
     # 
     # for name in __all__:
     #     # exec("from ..%s import %s" % (name, name))
     #     print("from  moviepy.audio.fx import %s" % (name))
         
     from moviepy.audio.fx import audio_fadein
     from moviepy.audio.fx import audio_fadeout
     from moviepy.audio.fx import audio_left_right
     from moviepy.audio.fx import audio_loop
     from moviepy.audio.fx import audio_normalize
     from moviepy.audio.fx import volumex
     ```
  <br><br>

* 问题: Moviepy - OSError: Error in file xxxxx.mp4, Accessing time t=1352.40-1352.45 seconds, with clip duration=1352.400000 seconds
* 解决方案：
  1. 在`C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\moviepy\video\fx`找到并打开`time_mirror.py`文件
  2. 修改如下代码：
  ```
  from moviepy.decorators import apply_to_audio, apply_to_mask, requires_duration
  
  
  @requires_duration
  @apply_to_mask
  @apply_to_audio
  def time_mirror(self):
      """
      Returns a clip that plays the current clip backwards.
      The clip must have its ``duration`` attribute set.
      The same effect is applied to the clip's audio and mask if any.
      """
      # return self.fl_time(lambda t: self.duration - t - 1, keep_duration=True)
      return self.fl_time(lambda t: self.duration - t, keep_duration=True)
  
  ```
  
  <br><br>

