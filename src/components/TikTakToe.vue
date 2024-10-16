<template>
  <div class="tic-tac-toe">
    <h1>Jogo da Velha</h1>
    <div class="board">
      <div
        class="cell"
        v-for="(cell, index) in cells"
        :key="index"
        @click="makeMove(index)"
      >
        {{ cell }}
      </div>
    </div>
    <div v-if="winner" class="message">
      <h2>{{ winner }} ganhou!</h2>
      <button @click="resetGame">Recomeçar Jogo</button>
    </div>
    <div v-else-if="isDraw" class="message">
      <h2>Empate!</h2>
      <button @click="resetGame">Recomeçar Jogo</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cells: Array(9).fill(null),
      currentPlayer: 'X',
      winner: null,
    };
  },
  computed: {
    isDraw() {
      return !this.winner && this.cells.every(cell => cell);
    },
  },
  methods: {
    makeMove(index) {
      if (this.cells[index] || this.winner) return;

      // Atribuir diretamente à célula
      this.cells[index] = this.currentPlayer; 
      this.checkWinner();
      this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
    },
    checkWinner() {
      const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
      ];

      for (const combination of winningCombinations) {
        const [a, b, c] = combination;
        if (this.cells[a] && this.cells[a] === this.cells[b] && this.cells[a] === this.cells[c]) {
          this.winner = this.cells[a];
          return;
        }
      }
    },
    resetGame() {
      this.cells = Array(9).fill(null);
      this.winner = null;
      this.currentPlayer = 'X';
    },
  },
};
</script>

<style scoped>
.tic-tac-toe {
  text-align: center;
}

.board {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  grid-template-rows: repeat(3, 100px);
  gap: 5px;
  margin: 20px auto;
}

.cell {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2em;
  border: 2px solid #333;
  cursor: pointer;
}

.cell:hover {
  background-color: #f0f0f0;
}

.message {
  margin-top: 20px;
}
</style>
