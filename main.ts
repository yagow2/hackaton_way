// Arquivo de teste para Code Review AI

// 1️⃣ Função com bug lógico
function sumNumbers(a: number, b: number): number {
    let result = a - b; // bug: deveria ser a + b
    return result;
}

// 2️⃣ Variáveis não usadas e estilo ruim
const unusedVar = 42;
let foo = "hello"  // falta ponto e vírgula

// 3️⃣ Função sem tipagem explícita
function greet(name) {
    return "Hello, " + name;
}

// 4️⃣ Função assíncrona com tratamento de erro ruim
async function fetchData(url: string) {
    const res = await fetch(url)
    const data = await res.json()
    return data
}

// 5️⃣ Classe simples com oportunidade de melhoria
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    describe() {
        console.log(this.name + " is " + this.age + " years old")
    }
}

// Uso das funções
console.log(sumNumbers(5, 3));
console.log(greet("Yago"));

const p = new Person("Alice", 30);
p.describe();
