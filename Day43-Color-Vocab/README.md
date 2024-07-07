# Spanish Vocabulary

This project presents a simple webpage to help users learn the names of colors in Spanish.

## Project Description

The webpage displays the names of colors in Spanish along with corresponding images. Each color name is styled in its respective color to help with visual learning.

## File Structure

### index.html

This file contains the HTML structure of the webpage. It includes:

- A main title and subtitle.
- Color names in Spanish, each associated with an image representing the color.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Spanish Vocabulary</title>
    <link rel="stylesheet" href="./style.css" />
  </head>

  <body>
    <h1>Colors</h1>
    <h2>Learn the colors in Spanish!</h2>
    <h2 class="color-title" id="red">Rojo</h2>
    <img class="color" src="./assets/images/red.png" alt="red" />

    <h2 class="color-title" id="blue">Azul</h2>
    <img src="./assets/images/blue.png" alt="blue" />

    <h2 class="color-title" id="orange">Anaranjado</h2>
    <img src="./assets/images/orange.png" alt="orange" />

    <h2 class="color-title" id="green">Verde</h2>
    <img src="./assets/images/green.png" alt="green" />

    <h2 class="color-title" id="yellow">Amarillo</h2>
    <img src="./assets/images/yellow.png" alt="yellow" />
  </body>
</html>
```

### style.css

This file contains the CSS styles for the webpage. It includes:

- Styling for images to set their height and width.
- Styling for color titles to display them in their respective colors.

```css
img {
  height: 200px;
  width: 200px;
}

.color-title {
  font-weight: normal;
}

#red {
  color: red;
}

#blue {
  color: blue;
}

#orange {
  color: orange;
}

#green {
  color: green;
}

#yellow {
  color: yellow;
}
```

## How to Use

1. **Download or clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Open the `index.html` file** in a web browser to view the content.

## Customization

- **Add more colors**:

  1. Add new color sections in `index.html` with corresponding images and Spanish names.
  2. Define new styles in `style.css` for the new colors.

- **Change images**:
  Replace the images in the `./assets/images/` directory with your own images, ensuring they have the same filenames or update the `src` attribute in `index.html`.
