console.log('page loaded');
const login = document.getElementById("login");
const username_error = document.getElementById("username_error");
const password_error = document.getElementById("password_error");
let has_error = false;

login.addEventListener('click', (e) => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username.length < 8) {
        username_error.style.display = 'inline';
        if (username.length == 0) {
            username_error.textContent = "please enter the username!"
        }
        has_error = true
    }
    else {
        username_error.style.display = 'none'
        has_error = false
    }
    if (password.length < 8) {
        password_error.style.display = 'inline';
        if (password.length == 0) {
            password_error.textContent = "please enter the password!"
        }
        has_error = true
    }
    else {
        password_error.style.display = 'none'
        has_error = false
    }
    if (has_error == false) {
        document.getElementById("h1").textContent = `Hello ${username}`
    }
    else {
        e.preventDefault();
    }
})