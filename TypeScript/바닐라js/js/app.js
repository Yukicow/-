const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")

const HIDDEN_CLASS = "hidden";
const USER_NAME = "username";

let savedUsername = localStorage.getItem(USER_NAME);

if(savedUsername === null){
    loginForm.classList.remove(HIDDEN_CLASS);
    loginForm.addEventListener("submit", onLoginSubmit);
}else {
    showGreeting();
}


function onLoginSubmit(event) {
    event.preventDefault();
    savedUsername = loginInput.value;
    localStorage.setItem(USER_NAME, savedUsername);
    loginForm.classList.add(HIDDEN_CLASS);
    showGreeting();
}

function showGreeting() {
    greeting.innerText = `Hello! ${savedUsername}`
    greeting.classList.remove(HIDDEN_CLASS);
}
