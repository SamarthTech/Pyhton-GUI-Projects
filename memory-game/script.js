const gameBoard = document.getElementById('game');
const COLORS = ["red", "blue", "green", "orange", "purple", "red", "blue", "green", "orange", "purple"];
let card1 = null;
let card2 = null;
let cardsFlipped = 0;
let noClicking = false;

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

const shuffledColors = shuffle(COLORS);

function createDivsForColors(colorArray) {
  colorArray.forEach(color => {
    const newDiv = document.createElement('div');
    newDiv.dataset.color = color;
    newDiv.addEventListener("click", handleCardClick);
    gameBoard.append(newDiv);
  });
}

function handleCardClick(e) {
  if (noClicking) return;
  if (e.target.classList.contains("flipped")) return;

  const currentCard = e.target;
  currentCard.style.backgroundColor = currentCard.dataset.color;

  if (!card1 || !card2) {
    currentCard.classList.add("flipped");
    card1 = card1 || currentCard;
    card2 = currentCard === card1 ? null : currentCard;
  }

  if (card1 && card2) {
    noClicking = true;
    const color1 = card1.dataset.color;
    const color2 = card2.dataset.color;

    if (color1 === color2) {
      cardsFlipped += 2;
      card1.classList.add("matched");
      card2.classList.add("matched");
      card1.removeEventListener("click", handleCardClick);
      card2.removeEventListener("click", handleCardClick);
      resetCards();
    } else {
      setTimeout(() => {
        card1.style.backgroundColor = "";
        card2.style.backgroundColor = "";
        card1.classList.remove("flipped");
        card2.classList.remove("flipped");
        resetCards();
      }, 1000);
    }
  }

  if (cardsFlipped === COLORS.length) alert("Game over!");
}

function resetCards() {
  card1 = null;
  card2 = null;
  noClicking = false;
}

createDivsForColors(shuffledColors);