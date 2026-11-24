from PIL import Image
import os
src=Image.open("app-icon.png").convert("RGBA")
res="android/app/src/main/res"
dens={"mdpi":1,"hdpi":1.5,"xhdpi":2,"xxhdpi":3,"xxxhdpi":4}
def fit(size,scale):
    c=Image.new("RGBA",(size,size),(0,0,0,0));s=int(size*scale)
    t=src.resize((s,s),Image.LANCZOS);c.paste(t,((size-s)//2,(size-s)//2),t);return c
for d,m in dens.items():
    p=f"{res}/mipmap-{d}"
    if not os.path.isdir(p):continue
    fit(int(48*m),.94).save(f"{p}/ic_launcher.png")
    fit(int(48*m),.94).save(f"{p}/ic_launcher_round.png")
    fit(int(108*m),.58).save(f"{p}/ic_launcher_foreground.png")
print("icons done")
