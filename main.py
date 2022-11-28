import os

try:
    from pypresence import Presence
except:
    if os.name == "nt":
        os.system("python -m pip install pypresence")
    else:
        os.system("python3 -m pip install pypresence")

application_id = "DISCORD APP ID HERE"

RPC = Presence(client_id = application_id)
RPC.connect()

def rpcUpdate(RPC, buttonsOn, buttons, textOn, details, state, image, imagecaption):
    if (buttonsOn):
        if (textOn):
            RPC.update(buttons=buttons, details=details, state=state, large_image = image, large_text = imagecaption)
        else:
            RPC.update(buttons=buttons, large_image = image, large_text = imagecaption)
    else:
        if (textOn):
            RPC.update(details=details,state=state,large_image=image,large_text=imagecaption)
        else:
            RPC.update(large_image=image,large_text=imagecaption)

buttons = [{
        "label": "My Website", # Top button text.
        "url": "https://freakish.dev" # Top button link.
    },
    {
        "label": "Follow Me!", # Bottom button text.
        "url": "https://github.com/SomeRandom-Dev" # Bottom button link.
    }
]

TOPTEXT = "please stop looking"
BOTTOMTEXT = "at my profile :)"

IMAGEKEY = "KEY" # The image key, from the list above
IMAGECAPTION = "CAPTION" # The text showed when the image is hovered over

buttonsenabled = True # Set to false to disable the buttons.
textenabled = True # Set to false to disable the text.

rpcUpdate(RPC, buttonsenabled, buttons, textenabled, TOPTEXT, BOTTOMTEXT, IMAGEKEY, IMAGECAPTION)
while True:
    input()
