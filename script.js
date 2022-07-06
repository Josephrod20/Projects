// Add all functions used from https://p5js.org/reference/
// to the global comment for glitch to recognize the code.
/* global
 * createCanvas, background, loadImage, image
 */

let dvdImage;

function setup() {
  createCanvas(800, 600);
  // We only want to load the logo once.
  dvdImage = loadImage(
    "https://cdn.glitch.com/eaea72a4-ac6d-4777-b76e-f37d75959aa5%2Fdvd.jpeg?1515761833387"
  );
  //setup
  x = 50;
  xvelocity = 2;
  y = 50;
  yvelocity = 2;
}

function draw() {
  background(100);
  // Draw the logo at the new position.
  image(dvdImage, x, y, 200, 150);

  //move the logo
  x += xvelocity;
  y += yvelocity;
  //move it left and right
  if (x > 600) {
    xvelocity = -3;
  } else if (x < 0) {
    xvelocity = 3;
  }
  //move up and down
  if (y > 450) {
    yvelocity = -3;
  } else if (y < 0) {
    yvelocity = 3;
  }
}
