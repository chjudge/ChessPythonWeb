window.addEventListener("DOMContentLoaded", async function () {
    // load the profiles from the API
    await getBoard()
});

async function getBoard() {
    fetch('/api/v1/board').then(response => response.json()).then(data => {
        const boardDiv = document.getElementById('board')
        let board = data[1]['board']

        for (let r = 0; r < board.length; r++) {
            for (let c = 0; c < board[r].length; c++) {
                boardDiv.appendChild(createCell(board[r][c], r, c))
            }
        }
        console.log('board updated at ', data[0]['requested'])
    })
        .catch(error => console.error('get board failed', error))
}

function createCell(name, r, c) {
    const cell = document.createElement('div')
    cell.id = `${r}${c}`
    cell.className = `piece ${name.includes('empty') ? 'empty' : name}`
    cell.innerHTML = ' '
    return cell
}