/* global
 * createCanvas, background, colorMode, HSB,height,width,ellipseMode
 * fill,ellipse, random, noFill,mousePressed,line,text,x,y,condtion
 * floor,mouseX,mouseY, keyPressed , redo, Scribble,
 */



let board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]];

let winCondtions=[
  [[0,0],[0,1],[0,2]],
  [[1,0],[1,1],[1,2]],
  [[2,0],[2,1],[2,2]],
  [[0,0],[1,0],[2,0]],
  [[0,1],[1,1],[2,1]],
  [[0,2],[1,2],[2,2]],
  [[0,0],[1,1],[2,2]],
  [[2,0],[1,1],[0,2]]
]


let player = ["X", "O"];
let currentPlayer;
let win;

function setup() {
  createCanvas(400, 400);
  currentPlayer = 'X';
}


function draw() {
  background(220);
  let w = width / 3;
  let h = height / 3;


  
  line(w, 0, w, height);
  line(w * 2, 0, w * 2, height);
  line(0, h, width, h);
  line(0, h * 2, width, h * 2);

  for (let j = 0; j < 3; j++) {
    for (let i = 0; i < 3; i++) {
      let x = w * i + w / 2;
      let y = h * j + h / 2;
      let spot = board[i][j];

      textSize(32);
      strokeWeight(4);
      if (spot == player[1]) {
        noFill();
      ellipse(x, y, w / 2);
      } else if (spot == player[0]) {
        let xr = w / 4;
       line(x - xr, y - xr, x + xr, y + xr);
       line(x + xr, y - xr, x - xr, y + xr);
      }
      
    }
   
  }

  if(win){

    fill(255)
    text(`${win} has won`,110,200)
    text('Press r to restart',108,250)
  }
  else if(fullBoard()==true){
   fill(255)
    text('Draw',150,200)
    text('Press r to restart',150,300)
  }
}


 function mousePressed(){
   let w = width / 3;
   let h = height / 3;
   let row=floor(mouseY/h) ;
   let columun=floor(mouseX/w);
  if(board[columun][row]!=' '){
    return
  }
   board[columun][row]= currentPlayer;
   if (currentPlayer=='X'){
     currentPlayer='O';
   }
   
   else if (currentPlayer=='O'){
     currentPlayer='X';
   }
  
   win = checkWin(); 
  
   
 }

function checkWin(){
  
  for(let condition of winCondtions){
    let player0=board[condition[0][0]][condition[0][1]]
    let player1=board[condition[1][0]][condition[1][1]]
    let player2=board[condition[2][0]][condition[2][1]]
if (player1==player2&&player0==player1&&player0!=' '){
  return player1

}
  };
  
}


function fullBoard(){
  for(let j=0;j<3;j++){
    for(let i=0;i<3;i++){
      if(board [j][i]==' ')
        return false ;
    }
  }
  return true; 

}
 

  function keyTyped(){
    
    if (key=== 'r'){
     
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]];
      
   }
  }
  


