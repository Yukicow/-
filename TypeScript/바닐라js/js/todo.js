const toDoForm = document.getElementById("todo-form");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.getElementById("todo-list");

let toDos = JSON.parse(localStorage.getItem("toDos"));

if(toDos === null){
    toDos = [];
}else{
    toDos.forEach(item => paintToDo(item));
}

function saveTodo(toDos) {
    localStorage.setItem("toDos" ,JSON.stringify(toDos));
}


function deleteToDo(event) {
    const li = event.target.parentElement;
    toDos = toDos.filter((todo) => todo.id !== parseInt(li.id));
    li.remove();
    saveTodo(toDos);
}


function paintToDo(newTodo) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    const button = document.createElement("button");

    li.id = newTodo.id;
    span.innerText = newTodo.text;
    button.innerText = "X"
    button.addEventListener("click", deleteToDo);

    li.appendChild(span);
    li.appendChild(button);

    toDoList.prepend(li)
}

function handleSubmit(event) {
    event.preventDefault();

    const newTodo = {
        id: Date.now(),
        text: toDoInput.value
    }
    
    toDos.push(newTodo);
    toDoInput.value = "";

    saveTodo(toDos);
    paintToDo(newTodo);
}

toDoForm.addEventListener("submit", handleSubmit);