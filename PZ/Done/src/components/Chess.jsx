import React, { useState, useEffect } from 'react';


const pieces = {
   R: '♜', N: '♞', B: '♝', Q: '♛', K: '♚', P: '♟', 
  r: '♖', n: '♘', b: '♗', q: '♕', k: '♔', p: '♙'  
};

const initialBoard = [
  ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.'],
  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
];

export default function Chessboard() {
  const [board, setBoard] = useState(initialBoard);
  const [draggedPiece, setDraggedPiece] = useState(null);
  const [whsMove, setWhsMove] = useState(0);

  const checkLetterCase = (letter) => letter === letter.toUpperCase() ? 1 : 0;

  const legalMove = (pieceId, to) => {
    const [type, fromRow, fromCol] = pieceId.split(',');
    const from = [parseInt(fromRow), parseInt(fromCol)];
    if (checkLetterCase(type) !== (whsMove % 2)) return false;

    const moveValidators = {
      p: validatePawnMove,
      n: validateKnightMove,
      b: validateBishopMove,
      r: validateRookMove,
      q: validateQueenMove,
      k: validateKingMove
    };

    const fn = moveValidators[type.toLowerCase()];
    return fn ? fn(from, to, type) : false;
  };

  const validatePawnMove = ([r1, c1], [r2, c2], type) => {
    const dir = type === 'p' ? 1 : -1;
    const firstMove = dir * 2;
    const target = board[r2][c2];
    if (r2 === r1 + dir && c1 === c2 && target === '.') return true;
    if (r2 === r1 + firstMove && c1 === c2 && board[r1 + dir][c1] === '.' && target === '.') return true;
    if (r2 === r1 + dir && Math.abs(c2 - c1) === 1 && target !== '.' && checkLetterCase(target) !== checkLetterCase(type)) return true;
    return false;
  };

  const validateKnightMove = ([r1, c1], [r2, c2]) => {
    const moves = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]];
    return moves.some(([dr, dc]) => r1 + dr === r2 && c1 + dc === c2 &&
      (board[r2][c2] === '.' || checkLetterCase(board[r2][c2]) !== checkLetterCase(board[r1][c1])));
  };

  const validateBishopMove = ([r1, c1], [r2, c2]) => {
    if (Math.abs(r2 - r1) !== Math.abs(c2 - c1)) return false;
    const dr = r2 > r1 ? 1 : -1, dc = c2 > c1 ? 1 : -1;
    for (let i = 1; i < Math.abs(r2 - r1); i++) {
      if (board[r1 + i * dr][c1 + i * dc] !== '.') return false;
    }
    return board[r2][c2] === '.' || checkLetterCase(board[r2][c2]) !== checkLetterCase(board[r1][c1]);
  };

  const validateRookMove = ([r1, c1], [r2, c2]) => {
    if (r1 !== r2 && c1 !== c2) return false;
    const dr = r2 === r1 ? 0 : (r2 > r1 ? 1 : -1);
    const dc = c2 === c1 ? 0 : (c2 > c1 ? 1 : -1);
    let row = r1 + dr, col = c1 + dc;
    while (row !== r2 || col !== c2) {
      if (board[row][col] !== '.') return false;
      row += dr; col += dc;
    }
    return board[r2][c2] === '.' || checkLetterCase(board[r2][c2]) !== checkLetterCase(board[r1][c1]);
  };

  const validateQueenMove = (from, to) =>
    validateBishopMove(from, to) || validateRookMove(from, to);

  const validateKingMove = ([r1, c1], [r2, c2]) => {
    const moves = [[0, 1], [0, -1], [1, 0], [1, -1], [1, 1], [-1, 0], [-1, 1], [-1, -1]];
    return moves.some(([dr, dc]) => r1 + dr === r2 && c1 + dc === c2 &&
      (board[r2][c2] === '.' || checkLetterCase(board[r2][c2]) !== checkLetterCase(board[r1][c1])));
  };

  const handleDrop = (e, r, c) => {
    e.preventDefault();
    if (!draggedPiece) return;

    const [type, fromRow, fromCol] = draggedPiece.id.split(',');
    const from = [parseInt(fromRow), parseInt(fromCol)];
    const to = [r, c];

    if (legalMove(draggedPiece.id, to)) {
      const updatedBoard = board.map(row => [...row]);
      updatedBoard[from[0]][from[1]] = '.';
      updatedBoard[to[0]][to[1]] = type;
      setBoard(updatedBoard);
      setWhsMove(whsMove + 1);
    }
    setDraggedPiece(null);
  };

  return (
    <div className="chessboard">
      {board.map((row, r) =>
        row.map((piece, c) => (
          <div
            key={`${r}-${c}`}
            className={`cell ${(r + c) % 2 === 0 ? 'light' : 'dark'}`}
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => handleDrop(e, r, c)}
          >
            {piece !== '.' && (
              <div
                className="piece"
                draggable
                id={[piece, r, c].join(',')}
                onDragStart={(e) => setDraggedPiece(e.target)}
                onDragEnd={() => setDraggedPiece(null)}
              >
                {pieces[piece]}
              </div>
            )}
          </div>
        ))
      )}
    </div>
  );
}
