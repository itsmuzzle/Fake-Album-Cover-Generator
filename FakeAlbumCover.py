from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests

# Helper function to write text to raw images
def display_cover(top,bottom ):
    
    # Use https://picsum.photos/ to grab a random image
    album_art_raw = requests.get('http://picsum.photos/1000/1000/?random')

    # Save the raw image
    with open('album_art_raw.png', 'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)

    # Open the raw image and create Draw object
    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)

    # Set coordinates for album name and band name text
    band_x, band_y = 100, 100
    album_x, album_y = 100, 850

    # Set the border to be black so it's visible on any image
    # We will later set the text color to white
    outline_color ="black"
    
    # Set the band and album name fonts
    band_font = ImageFont.truetype('C:\Windows\Fonts\Coopbl.ttf', 45)
    album_font = ImageFont.truetype('C:\Windows\Fonts\Coopbl.ttf', 60)
    
    # Draw the band name
    draw.text((band_x-1, band_y-1), top, fill=outline_color, font=band_font)
    draw.text((band_x+1, band_y-1), top, fill=outline_color, font=band_font)
    draw.text((band_x-1, band_y+1), top, fill=outline_color, font=band_font)
    draw.text((band_x+1, band_y+1), top, fill=outline_color, font=band_font)

    #Draw the album name
    draw.text((album_x-1, album_y-1), bottom, fill=outline_color, font=album_font)
    draw.text((album_x+1, album_y-1), bottom, fill=outline_color, font=album_font)
    draw.text((album_x-1, album_y+1), bottom, fill=outline_color, font=album_font)
    draw.text((album_x+1, album_y+1), bottom, fill=outline_color, font=album_font)

    # Set the text to white
    draw.text((band_x,band_y),top,(255,255,255), font=band_font)
    draw.text((album_x, album_y),bottom,(255,255,255), font=album_font)

    return img

# Link to random Wikipedia article
wikipedia_link='http://en.wikipedia.org/wiki/Special:Random'

# Random page for band title
band_title_wikipedia_page = requests.get(wikipedia_link)

# Random page for album title
album_name_wikipedia_page = requests.get(wikipedia_link)

# Parse the response as text
band_title_page = band_title_wikipedia_page.text
album_name_page = album_name_wikipedia_page.text

# Locate and clean the band title
band_start = band_title_page.find('<title>')
band_end = band_title_page.find('</title>')
band_title = band_title_page[band_start:band_end][7::].strip('- Wikipedia')
print(band_title)

# Locate and clean the album title
album_start = album_name_page.find('<title>')
album_end = album_name_page.find('</title>')
album_title = album_name_page[album_start:album_end][7::].strip('- Wikipedia')
print(album_title)

# Write the band and album names to the raw image
album_cover = display_cover(album_title, band_title)

# Save the finished image to disk
album_cover.save('fake_album.png')