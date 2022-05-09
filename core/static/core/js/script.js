


let togglebtn = document.querySelector('.toggle-btn')
let navbar = document.querySelector('.navbar')

togglebtn.addEventListener('click', ()=>{
    navbar.classList.toggle('mobile-nav')
})

const allForm = document.querySelectorAll('.form input, .form textarea');

console.log(allForm);



 $(document).ready(function(){
    $('#registration').validate({
        rules:{
            firstname: {
                required: true
            },
            lastname: {
                required: true
            },
            username: {
                required: true,
                minlength: 5
            },
            password: {
                required: true
            },
            conpassword: {
                required: true,
                equalTo: "#password"
            },
            email: {
                required: true,
                email: true
            },
            desc : {
                required: true
            }
        },
        messages: {
            firstname: {
                required: "Por favor ingresa tu primer nombre"
            },
            lastname: {
                required: "Por favor ingresar tus apellidos"
            },
            username: {
                required: "Por favor ingresa tu nombre de usuario"
            },
            password: {
                required: "Por favor ingresa tu contraseña"
            },
            conpassword: {
                required: "Por favor confirma tu contraseña"
            },
            email: {
                required: "Por favor ingresa tu correo electronico",
                email: "Por favor ingresa un email valido"
            },
            desc: {
                required: "Por favor ingresa una descripcion"
            },
            conpassword: {
                required: "Por favor confirma tu contraseña",
                equalTo: "Por favor ingresa la misma contraseña"
            }
            
        }        
    })
})

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("registration").addEventListener('submit', valForm);
});

function valForm(evento) {
    evento.preventDefault();
    var usuario = document.getElementById('username').value;
    var Errores = 0;
    if (usuario.length == 0) {
        document.getElementById("errorNombre").innerHTML = "El nombre es inválido";
        document.getElementById("errorNombre").classList.add("error");
        Errores += 1;
    }
    var clave = document.getElementById('password').value;
    if (clave.length < 6) {
        document.getElementById("errorContra").innerHTML = "La contraseña es inválida";
        document.getElementById("errorContra").classList.add("error");
        Errores += 1;
    }

    if (Errores > 0) {
        return;
    }
    this.submit();
}