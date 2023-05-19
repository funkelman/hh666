from PIL import Image, ImageDraw

def generate_img(argument):
    colors = {'c': '#00FFFF', 'y': '#FFFF00', 'm': '#FF00FF', 'r': '#FF0000', 'g': '#00FF00', 'b': '#0000FF'}
    output_width = 2000
    output_height = 3000

    # Calculate the number of icons based on the length of the argument
    num_icons = len(argument) // 6

    # Check if the number of icons exceeds the limit
    if num_icons > 100:
        raise ValueError("The argument string exceeds the maximum limit of 10cargo 0 icons.")

    # Create a new image
    image = Image.new('RGB', (output_width, output_height), 'white')
    draw = ImageDraw.Draw(image)

    # Define grid properties
    square_size = 100
    num_rows = 10
    num_columns = 10

    # Calculate the starting position for the first icon
    start_x = (output_width % (square_size * num_columns)) // 2
    start_y = (output_height % (square_size * num_rows)) // 2

    # Iterate over the icons in the argument string
    for i in range(num_icons):
        icon_x = start_x + (i % num_columns) * square_size * 2
        icon_y = start_y + (i // num_columns) * square_size * 3

        # Iterate over the squares within each icon
        for j in range(6):
            square_x = icon_x + (j % 2) * square_size
            square_y = icon_y + (j // 2) * square_size

            # Get the corresponding letter from the argument
            letter = argument[i * 6 + j]

            # Draw the square with the corresponding color
            draw.rectangle([(square_x, square_y), (square_x + square_size, square_y + square_size)],
                           fill=colors[letter])

            
    # Save the image
    image.save("output.png")

# Test the function
argument = "ymgbrcgrcmybrmcgbygcymbrbcgmryrymbcgmyrcbgcrybmgyrcbgmrbcymgrmgycbbycmgrcrgmbybmrgcygmcbyrmrycgbcmyrbgrgybcmymrgbcbmgrycbgycrmbrmgcybrgmcygcmybrrcmgbycyrmbggrybcmcygrbmgyrmcbgcymrbbrmgcyybgcrmrbycmgycbmrggmybcrgrmbycrmcgbycmybgrcgbrmyygcmbrcrybmgbgcymrbmcryggbcrmycrgmybrbcymgrgybcmbcymgrrbgymcmrcygbgbyrmccybgrmyrbcmgbycrgmgyrmcbrcmgbybmgrycgcbmrycyrmbgrmycbgbgrcmygrcmybrygcmbgbymrcybmgcrbmrgcyrcymbgyrcbgmgmcrybymcgrbgybcmrcyrmgbmycbrgrygmcbbcrymgmgybcrcbygmrcygrbmmcbrgyrymbcgmyrcgbbycrmggmcbyrymgbrcbgycrmcmyrbgrcgbymmyrcbggrybcmgcymbrgcmybrrmgycbrbymcgcgmybrgybrmcmcyrbgmbgyrcymrgbcrgbmcyycbrgmcrgmbybycmgrbcgmrycrbgymcrbmgyymgcrbcgyrbmcgybmrcbgrymgbmcyrycrgmbrgcbymrgbymccbmyrgycmbrgbgcrmymrycgbmcbgyrymcbgrcgmrbybrgmcygcybmrmygrcbrgcybmcbrmygmycgbrbygrcmgrcmbygybrmc"
generate_img(argument)
