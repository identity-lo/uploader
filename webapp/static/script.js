let get_password = document.getElementById("password");
let get_conpassword = document.getElementById("conpassword").value;
let get_conpassword_func = document.getElementById("conpassword")


get_conpassword_func.addEventListener("blur" , function(e){
    if (get_password.value == e.target.value){ 
    }
    else{
        Swal.fire({
            title: 'Error',
            text: 'your password confirm is incorrect',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }
});