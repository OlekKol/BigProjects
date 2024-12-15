const chessboard = document.getElementById("chessboard");

const pieces = {
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟'
};

let boardState = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
];

let draggedPiece = null;
let whs_move = 0;

function renderBoard() {
    chessboard.innerHTML = "";

    for (let r = 0; r < 8; r++) {
        for (let c = 0; c < 8; c++) {
            const cell = document.createElement("div");
            cell.classList.add("cell", (r + c) % 2 === 0 ? "light" : "dark");
            cell.dataset.r = r;
            cell.dataset.c = c;

            const piece = boardState[r][c];
            if (piece !== '.') {
                const id = [piece, r, c];
                const pieceElement = document.createElement("div");
                pieceElement.id = id.join(",");
                pieceElement.textContent = pieces[piece];
                pieceElement.classList.add("piece");
                pieceElement.draggable = true;
                cell.appendChild(pieceElement);
            }

            chessboard.appendChild(cell);
        }
    }
}

chessboard.addEventListener("dragstart", (e) => {
    if (e.target.classList.contains("piece")) {
        draggedPiece = e.target;
        setTimeout(() => {
            e.target.style.visibility = "hidden";
        }, 0);
    }
});

chessboard.addEventListener("dragend", (e) => {
    if (draggedPiece) {
        draggedPiece.style.visibility = "visible";
        draggedPiece = null;
    }
});

chessboard.addEventListener("dragover", (e) => {
    e.preventDefault();
});

chessboard.addEventListener("drop", (e) => {
    e.preventDefault();
    const targetCell = e.target.classList.contains("cell") ? e.target : e.target.parentElement;
    const targetRow = parseInt(targetCell.dataset.r);
    const targetCol = parseInt(targetCell.dataset.c);
    const targetPosition = [targetRow, targetCol];

    if (legalMove(draggedPiece, targetPosition, whs_move)) {
        const pieceInfo = draggedPiece.id.split(",");
        const currentPiece = pieceInfo[0];
        const currentPosition = [parseInt(pieceInfo[1]), parseInt(pieceInfo[2])];

        boardState[currentPosition[0]][currentPosition[1]] = '.';
        boardState[targetPosition[0]][targetPosition[1]] = currentPiece;

        draggedPiece.id = [currentPiece, targetRow, targetCol].join(",");
        whs_move += 1;
        renderBoard();
    } else {
        console.log('Invalid move. Turn remains the same.');
    }

    console.log(boardState.map(row => row.join(" ")).join("\n"));
});

function checkLetterCase(letter) {
    return letter === letter.toUpperCase() ? 1 : 0;
}

function legalMove(piece, targetPosition, whs_move) {
    const pieceInfo = piece.id.split(",");
    const currentPiece = pieceInfo[0];
    const currentPosition = [parseInt(pieceInfo[1]), parseInt(pieceInfo[2])];

    if (checkLetterCase(currentPiece) !== (whs_move % 2)) {
        console.log("Not your turn.");
        return false;
    }

    switch (currentPiece.toLowerCase()) {
        case 'p': return validatePawnMove(currentPosition, targetPosition, currentPiece);
        case 'n': return validateKnightMove(currentPosition, targetPosition);
        case 'b': return validateBishopMove(currentPosition, targetPosition);
        case 'r': return validateRookMove(currentPosition, targetPosition);
        case 'q': return validateQueenMove(currentPosition, targetPosition);
        case 'k': return validateKingMove(currentPosition, targetPosition);
        default: return false;
    }
}

function validatePawnMove(currentPosition, targetPosition, currentPiece) {
    const direction = currentPiece === 'p' ? 1 : -1;
    const firstMoveDirection = direction * 2;
    const [startRow, startCol] = currentPosition;
    const [endRow, endCol] = targetPosition;

    if (endRow === startRow + direction &&
         endCol === startCol && 
         boardState[endRow][endCol] === '.') {
        return true;
    }

    if (endRow === startRow + firstMoveDirection && 
        endCol === startCol && 
        boardState[startRow + direction][startCol] === '.' && 
        boardState[endRow][endCol] === '.') {
        return true;
    }

    if (endRow === startRow + direction && 
        Math.abs(endCol - startCol) === 1 && 
        boardState[endRow][endCol] !== '.' && 
        checkLetterCase(boardState[endRow][endCol]) !== checkLetterCase(currentPiece)) {
        return true;
    }

    return false;
}

function validateKnightMove(currentPosition, targetPosition) {
    const possibleMoves = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]];
    const [startRow, startCol] = currentPosition;
    const [endRow, endCol] = targetPosition;

    for (const [dRow, dCol] of possibleMoves) {
        if (startRow + dRow === endRow && startCol + dCol === endCol) {
            const targetPiece = boardState[endRow][endCol];
            if (targetPiece === '.' || checkLetterCase(targetPiece) !== checkLetterCase(boardState[startRow][startCol])) {
                return true;
            }
        }
    }

    return false;
}

function validateBishopMove(currentPosition, targetPosition) {
    const [startRow, startCol] = currentPosition;
    const [endRow, endCol] = targetPosition;

    if (Math.abs(endRow - startRow) !== Math.abs(endCol - startCol)) return false;

    const rowDirection = endRow > startRow ? 1 : -1;
    const colDirection = endCol > startCol ? 1 : -1;

    let row = startRow + rowDirection;
    let col = startCol + colDirection;

    while (row !== endRow && col !== endCol) {
        if (boardState[row][col] !== '.') return false;
        row += rowDirection;
        col += colDirection;
    }

    const targetPiece = boardState[endRow][endCol];
    if (targetPiece === '.' || checkLetterCase(targetPiece) !== checkLetterCase(boardState[startRow][startCol])) {
        return true;
    }

    return false;
}

function validateRookMove(currentPosition, targetPosition) {
    const [startRow, startCol] = currentPosition;
    const [endRow, endCol] = targetPosition;

    if (startRow !== endRow && startCol !== endCol) return false;

    const rowDirection = startRow === endRow ? 0 : (endRow > startRow ? 1 : -1);
    const colDirection = startCol === endCol ? 0 : (endCol > startCol ? 1 : -1);

    let row = startRow + rowDirection;
    let col = startCol + colDirection;

    while (row !== endRow || col !== endCol) {
        if (boardState[row][col] !== '.') return false;
        row += rowDirection;
        col += colDirection;
    }

    const targetPiece = boardState[endRow][endCol];
    if (targetPiece === '.' || checkLetterCase(targetPiece) !== checkLetterCase(boardState[startRow][startCol])) {
        return true;
    }

    return false;
}

function validateQueenMove(currentPosition, targetPosition) {
    return validateBishopMove(currentPosition, targetPosition) || validateRookMove(currentPosition, targetPosition);
}

function validateKingMove(currentPosition, targetPosition){
    const possibleMoves = [[0, 1], [0, -1], [1, 0], [1, -1], [1, 1], [-1, 0], [-1, 1], [-1, -1]];
    const [startRow, startCol] = currentPosition;
    const [endRow, endCol] = targetPosition;

    for (const [dRow, dCol] of possibleMoves) {
        if (startRow + dRow === endRow && startCol + dCol === endCol) {
            const targetPiece = boardState[endRow][endCol];
            if (targetPiece === '.' || checkLetterCase(targetPiece) !== checkLetterCase(boardState[startRow][startCol])) {
                return true;
            }
        }
    }

    return false;
}

renderBoard();
