from tinyWinToast.tinyWinToast import *
import time
toast = Toast()
toast.setTitle("TITLE", maxLines=1)
toast.setMessage("MESSAGE", maxLines=1)
toast.setTag("mytag")
toast.setGroup("mygroup")
toast.setProgress(Progress(title="Title", value="0.2", valueStringOverride="15/20", status="Save..."))
toast.show()

time.sleep(6)

toast.setProgress(Progress(title="Title", value="0.9", valueStringOverride="19/20", status="Save..."))
d = {'progressValue': "0.9", 'progressValueString': "19/20"}
#toast.show() # if you wand update all toast
toast.update(200, d)