import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

url = "https://audreychr33.github.io/andrea-chrysostomou/"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=12,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Add logo
logo = Image.open("logo1.png")

# Resize logo
logo_size = 120
logo = logo.resize((logo_size, logo_size))

# Position logo
pos = (
    (img.size[0] - logo_size) // 2,
    (img.size[1] - logo_size) // 2
)

img.paste(logo, pos)

# Save high-quality
img.save("andrea_qr_pro.png", dpi=(300,300))

print("Professional QR with logo generated!")