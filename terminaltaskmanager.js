/**
 * Classe TaskManager para gerenciar uma lista de afazeres simples.
 */
class TaskManager {
    constructor() {
        // Inicializa o array de tarefas vazio
        this.tasks = [];
    }

    /**
     * Adiciona uma nova tarefa ao sistema.
     * @param {string} description - O que precisa ser feito.
     */
    addTask(description) {
        const task = {
            id: this.tasks.length + 1,
            description: description,
            completed: false,
            createdAt: new Date().toLocaleDateString('pt-BR')
        };
        this.tasks.push(task);
        console.log(`✅ Tarefa "${description}" adicionada!`);
    }

    /**
     * Lista todas as tarefas formatadas no console.
     */
    listTasks() {
        console.log("\n--- MINHA LISTA DE TAREFAS ---");
        if (this.tasks.length === 0) {
            console.log("Nenhuma tarefa pendente.");
        } else {
            this.tasks.forEach(task => {
                const status = task.completed ? "[X]" : "[ ]";
                console.log(`${task.id}. ${status} ${task.description} (${task.createdAt})`);
            });
        }
        console.log("-----------------------------\n");
    }

    /**
     * Marca uma tarefa como concluída pelo ID.
     * @param {number} id 
     */
    completeTask(id) {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = true;
            console.log(`⭐ Tarefa ${id} marcada como concluída!`);
        } else {
            console.log("❌ Tarefa não encontrada.");
        }
    }
}

// Exemplo de uso:
const meuGerenciador = new TaskManager();

meuGerenciador.addTask("Estudar TypeScript");
meuGerenciador.addTask("Finalizar commits do dia");
meuGerenciador.completeTask(1);
meuGerenciador.listTasks();
