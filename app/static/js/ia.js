'use strict';

const canvas = document.querySelector("#pongIaCanvas");
const ctx = canvas.getContext('2d');

const paddleWidth = 10;
const paddleHeight = 100;
const paddleSpeed = 2;
const paddleSpeedIa = 2;
const ballRadius = 10;
const initialBallSpeed = 1.5;
const maxBallSpeed = 4;
const keyState = {};

let IaSpeed = 0;
let IaPrecision = 0;
let player1Score = 0;
let computerScore = 0;
let ballSpeedX = initialBallSpeed;
let ballSpeedY = initialBallSpeed;

let player1Y = canvas.height / 2 - paddleHeight / 2;
let computerY = canvas.height / 2 - paddleHeight / 2;
//let computerCentreY = computerY + paddleHeight / 2;
let ballX = canvas.width / 2;
let ballY = canvas.height / 2;

//Fonction pour dessiner des rectangles
function drawRect(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
}

// Fonction pour dessiner une ligne au milieu
function drawLine() {
    ctx.strokeStyle = 'white';
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.stroke();
}

//Fonction pour dessiner un cercle
function drawCircle(x, y, radius, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fill();
}

//Fonction pour écrire du texte
function drawText(text, x, y, color, font = '20px Arial') {
    ctx.fillStyle = color;
    ctx.font = font;
    ctx.fillText(text, x, y);
}

function draw() {
    // Nettoyer le canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Dessiner les deux joueurs
    drawRect(0, player1Y, paddleWidth, paddleHeight, 'white');
    drawRect(canvas.width - paddleWidth, computerY, paddleWidth, paddleHeight, 'white');

    //Dessiner la ligne du milieu
    drawLine();

    // Dessiner la balle
    drawCircle(ballX, ballY, ballRadius, 'white');

    // Ecrire les scores
    drawText(player1Score, canvas.width / 4, 50, 'white');
    drawText(computerScore, 3 * canvas.width / 4, 50, 'white');
}

function getRandomNumber(min, max) {
    return Math.random() * (max - min) + min;
}

// Fonction pour la direction vers le haut à gauche
function startTopLeft(ballX, ballY) {
    if (Math.random() < 0.5)
    {
        ballSpeedX = -1 * initialBallSpeed;
        ballSpeedY = -1 * initialBallSpeed;
    }
    else
    {
        ballSpeedX = -1 * initialBallSpeed;
        ballSpeedY = -1.4 * initialBallSpeed;
    }
}

// Fonction pour la direction vers le haut à droite
function startTopRight(ballX, ballY) {
    if (Math.random() < 0.5)
    {
        ballSpeedX = 1 * initialBallSpeed;
        ballSpeedY = -1 * initialBallSpeed;
    }
    else
    {
        ballSpeedX = 1 * initialBallSpeed;
        ballSpeedY = -0.5 * initialBallSpeed;
    }
}

// Fonction pour la direction vers le bas à gauche
function startBottomLeft(ballX, ballY) {
    if (Math.random() < 0.5)
    {
        ballSpeedX = -1 * initialBallSpeed;
        ballSpeedY = 1 * initialBallSpeed;
    }
    else
    {
        ballSpeedX = -1 * initialBallSpeed;
        ballSpeedY = 1.4 * initialBallSpeed;
    }
}

// Fonction pour la direction vers le bas à droite
function startBottomRight(ballX, ballY) {
    if (Math.random() < 0.5)
    {
        ballSpeedX = 1 * initialBallSpeed;
        ballSpeedY = 1 * initialBallSpeed; 
    }
    else
    {
        ballSpeedX = 1 * initialBallSpeed;
        ballSpeedY = 1.4 * initialBallSpeed;
    }
}

// Choisir une direction de manière aléatoire
function chooseRandomDirection(ballX, ballY) {
    const directions = [
        startTopLeft,
        startTopRight,
        startBottomLeft,
        startBottomRight
    ];
    console.log("TEST");
    const randomIndex = Math.floor(Math.random() * directions.length);
    const randomDirectionFunction = directions[randomIndex];
    randomDirectionFunction(ballX, ballY);
}


function update() {
    // Faire bouger la balle
    //if (ballSpeedX < maxBallSpeed && ballSpeedY < maxBallSpeed)
    //{
        ballX += ballSpeedX;
        ballY += ballSpeedY;
    //}

    // Envoyer la balle dans l'autre sens si elle touche le haut ou le bas
    if ((ballY + ballRadius >= canvas.height || ballY - ballRadius <= 0)) {
        ballSpeedY = -ballSpeedY * getRandomNumber(0.8, 1.2);
        ballY += ballSpeedY;
    }

    // Envoyer la balle de l'autre côté si elle touche un joueur
    else if (ballX - ballRadius < paddleWidth &&
        ballY + ballRadius > player1Y &&
        ballY - ballRadius < player1Y + paddleHeight) {
        ballSpeedX = -ballSpeedX * getRandomNumber(0.8, 1.2); //0,8, 1,2
        ballX += ballSpeedX;
    }

    else if (ballX + ballRadius > canvas.width - paddleWidth &&
        ballY + ballRadius > computerY &&
        ballY - ballRadius < computerY + paddleHeight) {
        ballSpeedX = -ballSpeedX * getRandomNumber(0.8, 1.2);
        ballX += ballSpeedX;
    }

    // Si la balle est sortie du jeu, remettre la balle au centre
    if (ballX - ballRadius < 0) {
        computerScore++;
        resetBall();
        resetPaddles();
    } else if (ballX + ballRadius > canvas.width) {
        player1Score++;
        resetBall();
        resetPaddles();
    }

    // Augmenter la vitesse de la balle progressivement sur une même manche
    if (Math.abs(ballSpeedX) < maxBallSpeed) {
        ballSpeedX += ballSpeedX > 0 ? 0.0001 : -0.0001;
    }
	else
	{
		ballSpeedX = maxBallSpeed;
	}

    if (Math.abs(ballSpeedY) < maxBallSpeed) {
        ballSpeedY += ballSpeedY > 0 ? 0.0001 : -0.0001;
    }
	else
	{
		ballSpeedY = maxBallSpeed;
	}
}

//Replacer la balle au centre
function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballSpeedX = initialBallSpeed;
    ballSpeedY = initialBallSpeed;
    chooseRandomDirection(ballX, ballY);
}

function resetPaddles() {
    player1Y = (canvas.height - paddleHeight) / 2;
    computerY = (canvas.height - paddleHeight) / 2;
}


// mise à jour de l'état des touches
function handleKeydown(event) {
    keyState[event.key] = true;
}

function handleKeyup(event) {
    keyState[event.key] = false;
}

//Déplacer les joueurs selon les touches du clavier
function handleKeyPress() {

    if (keyState["ArrowUp"] && player1Y > 0)
        player1Y -= paddleSpeed;
    if (keyState["ArrowDown"] && player1Y < canvas.height - paddleHeight)
        player1Y += paddleSpeed;
}

let difficultylevel = "easy";
//function for the IA is easy to beat
function computerMovement() {

	let paddleSpeedIaAdjusted = paddleSpeedIa;

	let precision = 0.5;
	if (difficultylevel === "easy") {
		precision = getRandomNumber(0.3, 0.6);
	}
	else if (difficultylevel === "medium") {
		precision = getRandomNumber(0.6, 0.9);
	}
	else if (difficultylevel === "hard") {
		precision = getRandomNumber(0.9, 1.2);
	}

	if (ballY > computerY + paddleHeight / 2 && computerY < canvas.height - paddleHeight) {
		computerY += paddleSpeedIa * precision;
	} else if (ballY < computerY + paddleHeight / 2 && computerY > 0) {
		computerY -= paddleSpeedIa * precision;
	}
}

// Boucle sur le jeu 
function gameLoop() {
    update();
    draw();
    handleKeyPress();
	computerMovement();
    if (player1Score < 5 && computerScore < 5) {
        requestAnimationFrame(gameLoop);
    } else {
        endGame();
    }
}

// Afficher qui a gagné
function endGame() {
    if (player1Score === 5) {
        drawText("You win !", 350, 250, 'red');
    } else {
        drawText("IA wins !", 350, 250, 'red');
    }
    
}

document.addEventListener('keydown', handleKeydown);
document.addEventListener('keyup', handleKeyup);
gameLoop();