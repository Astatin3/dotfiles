import subprocess
import datetime
import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

try:
    os.ulink("/tmp/wallpaper.png")
except:
    x = None # Do nothing

#file = open("/home/astatin3/.config/sway/icon.txt","r")
#lines = file.readlines()
#file.close()

output = (subprocess.run(['neofetch', '--stdout'], capture_output=True, text=True).stdout).split("\n")

screenX = 0
screenY = 0

for i in range(0, len(output)-2, 1):
    #lines[i] = lines[i][:-1] + output[i]

    #print(lines[i])

    if i == 0:
        output[0] += f"at ({datetime.datetime.now().strftime('%m-%d %H:%M:%S')})"

    if i == 8:
        res = output[i].split(" ")[1].split("x")
        screenX = int(res[0])
        screenY = int(res[1])

#neofetch = "\n".join(lines)

icon = Image.open("/home/astatin3/.config/sway/icon.png")
iconsizeX, iconsizeY = icon.size

neofetch = "\n".join(output)

textSize = 0.01

iconscale = 0.0005

textoffsetX = 0.0 #Percentages
textoffsetY = -0.16

iconoffsetX = -0.145
iconoffsetY = -0.16

img = Image.new('RGB', (screenX, screenY), (31, 26, 32))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/astatin3/.config/sway/UbuntuMonoNerdFontMono-Regular.ttf", textSize*screenX)
draw.text((textoffsetX*screenX+screenX/2, textoffsetY*screenY+screenY/2),neofetch,(199,0,57),font=font)
icon = icon.resize((round(iconscale*iconsizeX*screenY), round(iconscale*iconsizeY*screenY)), Image.Resampling.LANCZOS)
img.paste(icon, (round(iconoffsetX*screenX+screenX/2), round(iconoffsetY*screenY+screenY/2)))
img.save("/tmp/wallpaper.png")
#img.show()

subprocess.run(["swaybg", "-m", "fill", "-i", "/tmp/wallpaper.png"])
