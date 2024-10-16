<template>
    <div class="password-generator">
      <h1>Gerador de Senhas</h1>
  
      <div class="settings">
        <label for="length">Comprimento da Senha:</label>
        <input
          id="length"
          type="number"
          v-model="length"
          min="4"
          max="32"
          step="1"
        />
  
        <div>
          <label>
            <input type="checkbox" v-model="includeUppercase" />
            Incluir Letras Maiúsculas
          </label>
          <label>
            <input type="checkbox" v-model="includeLowercase" />
            Incluir Letras Minúsculas
          </label>
          <label>
            <input type="checkbox" v-model="includeNumbers" />
            Incluir Números
          </label>
          <label>
            <input type="checkbox" v-model="includeSymbols" />
            Incluir Símbolos
          </label>
        </div>
  
        <button @click="generatePassword">Gerar Senha</button>
      </div>
  
      <div v-if="generatedPassword" class="password-output">
        <p><strong>Senha Gerada:</strong> {{ generatedPassword }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        length: 12, // Valor inicial para o comprimento da senha
        includeUppercase: true,
        includeLowercase: true,
        includeNumbers: true,
        includeSymbols: true,
        generatedPassword: '',
      };
    },
    methods: {
      generatePassword() {
        if (this.length > 32) {
          alert('O comprimento máximo da senha é 32 caracteres.');
          this.length = 12;
          return;
        }
        const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
        const numberChars = '0123456789';
        const symbolChars = '!@#$%^&*()_+[]{}|;:,.<>?';
  
        let allChars = '';
        if (this.includeUppercase) allChars += uppercaseChars;
        if (this.includeLowercase) allChars += lowercaseChars;
        if (this.includeNumbers) allChars += numberChars;
        if (this.includeSymbols) allChars += symbolChars;
  
        if (!allChars) {
          alert('Selecione ao menos uma opção para gerar a senha.');
          return;
        }
  
        let password = '';
        for (let i = 0; i < this.length; i++) {
          const randomIndex = Math.floor(Math.random() * allChars.length);
          password += allChars[randomIndex];
        }
  
        this.generatedPassword = password;
      },
    },
  };
  </script>
  
  <style scoped>
  .password-generator {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    background-color: #f9f9f9;
  }
  
  .settings {
    margin-bottom: 20px;
  }
  
  .settings input[type="number"] {
    width: 100%;
    padding: 8px;
    margin-top: 10px;
  }
  
  button {
    padding: 10px 20px;
    margin-top: 15px;
    border: none;
    background-color: #3498db;
    color: white;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
  }
  
  button:hover {
    background-color: #2980b9;
  }
  
  .password-output {
    margin-top: 20px;
  }
  
  .password-output p {
    font-size: 18px;
    font-weight: bold;
  }
  </style>
  