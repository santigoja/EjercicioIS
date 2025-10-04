<template>
  <div>
    <h1>Menú</h1>
    <button @click="opcion = 1">1. Ver tareas</button>
    <button @click="opcion = 2">2. Marcar como completada</button>
    <button @click="opcion = 3">3. Eliminar tareas</button>
    <button @click="guardarStorage()">4. Guardar en localStorage</button>

    <!-- Ver tareas -->
    <div v-if="opcion === 1">
      <h2>Lista de Tareas</h2>
      <ul>
        <li v-for="(tarea, index) in tareas" :key="index">
          {{ tarea.descripcion }} - {{ tarea.completada ? "✅" : "❌" }}
        </li>
      </ul>
    </div>

    <!-- Marcar como completada -->
    <div v-if="opcion === 2">
      <h2>Marcar tarea como completada</h2>
      <ul>
        <li v-for="(tarea, index) in tareas" :key="index">
          {{ tarea.descripcion }}
          <button @click="marcarComoCompleta(index)">Completar</button>
        </li>
      </ul>
    </div>

    <!-- Eliminar tarea -->
    <div v-if="opcion === 3">
      <h2>Eliminar tarea</h2>
      <ul>
        <li v-for="(tarea, index) in tareas" :key="index">
          {{ tarea.descripcion }}
          <button @click="eliminarTarea(index)">Eliminar</button>
        </li>
      </ul>
    </div>

    <!-- Confirmación de guardado -->
    <div v-if="opcion === 4">
      <h2>✅ Datos guardados en localStorage</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListaTareas",
  data() {
    return {
      opcion: null,
      tareas: [
        { descripcion: "Estudiar Vue.js", completada: false },
        { descripcion: "Hacer ejercicio", completada: true },
        { descripcion: "Leer un libro", completada: false }
      ],
      completadas: []
    };
  },
  methods: {
    marcarComoCompleta(index) {
      const tarea = this.tareas[index];
      tarea.completada = true;
      this.completadas.push(tarea);
      this.tareas.splice(index, 1);
    },
    eliminarTarea(index) {
      this.tareas.splice(index, 1);
    },
    guardarStorage() {
      localStorage.setItem("tareas", JSON.stringify(this.tareas));
      this.opcion = 4;
    }
  },
  mounted() {
    const datosGuardados = localStorage.getItem("tareas");
    if (datosGuardados) {
      this.tareas = JSON.parse(datosGuardados);
    }
  }
};
</script>

<style scoped>
button {
  margin: 5px;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
