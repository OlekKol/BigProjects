
const layout = {
    '1': 'oxxxxxxxxx',
    '2': 'ooxxxxxxxx',
    '3': 'xoooooxxxx',
    '4': 'xxxxxoooxx',
    '5': 'oxxxxooxxx',
    '6': 'ooxxxxoxxx',
    '7': 'xooooooxxx',
    '8': 'ooxxxoxxxx',
    '9': 'oxxxxxxxxx',
    '10': 'ooxxxxxxxx',
};

const container = document.getElementById("maze");
const playerPosition = { row: 0, col: 0 }; 


const rows = [];
for (let row = 1; row <= Object.keys(layout).length; row++) {
    const line = document.createElement("section");
    line.style.display = "flex";

    const rowString = layout[row.toString()];
    const cells = [];
    for (let col = 0; col < rowString.length; col++) {
        const cell = document.createElement("div");
        cell.style.height = "10vw";
        cell.style.width = "10vw";
        cell.classList.add(rowString[col] === 'o' ? "path" : "blockade");
        line.appendChild(cell);
        cells.push(cell);
    }
    rows.push(cells);
    container.appendChild(line);
}

function renderPlayer() {
    rows.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            cell.classList.remove("player");
        });
    });
    rows[playerPosition.row][playerPosition.col].classList.add("player");
}
renderPlayer();

document.addEventListener("keydown", (event) => {
    const { row, col } = playerPosition;
    let newRow = row;
    let newCol = col;

    if (event.key === "w") newRow = Math.max(0, row - 1); 
    if (event.key === "s") newRow = Math.min(rows.length - 1, row + 1); 
    if (event.key === "a") newCol = Math.max(0, col - 1); 
    if (event.key === "d") newCol = Math.min(rows[0].length - 1, col + 1); 


    if (rows[newRow][newCol].classList.contains("path")) {
        playerPosition.row = newRow;
        playerPosition.col = newCol;
        renderPlayer();
    }
});