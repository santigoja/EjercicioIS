<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");
const isLogin = ref(true); // true = login, false = registro
const message = ref("");

const handleSubmit = async () => {
  const url = isLogin.value
    ? "http://127.0.0.1:8000/login"
    : "http://127.0.0.1:8000/register";

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      message.value = "❌ " + error.detail;
    } else {
      const data = await response.json();
      message.value = "✅ " + data.message;
    }
  } catch (err) {
    message.value = "⚠️ Error de conexión con el servidor";
  }
};
</script>

<template>
  <div class="form-container">
    <h2>{{ isLogin ? "Iniciar Sesión" : "Registrarse" }}</h2>

    <form @submit.prevent="handleSubmit">
      <label>Email:</label>
      <input v-model="email" type="email" required />

      <label>Contraseña:</label>
      <input v-model="password" type="password" required />

      <button type="submit">
        {{ isLogin ? "Entrar" : "Registrar" }}
      </button>
    </form>

    <p class="toggle">
      <a href="#" @click.prevent="isLogin = !isLogin">
        {{ isLogin ? "¿No tienes cuenta? Regístrate" : "¿Ya tienes cuenta? Inicia sesión" }}
      </a>
    </p>

    <p class="msg">{{ message }}</p>
  </div>
</template>

<style scoped>
.form-container {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}
label {
  display: block;
  margin-top: 10px;
}
input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  margin-top: 15px;
  padding: 10px;
  width: 100%;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background: #36996c;
}
.toggle {
  margin-top: 10px;
}
.msg {
  margin-top: 15px;
  font-weight: bold;
}
</style>
