let get_password = document.getElementById("password");
let get_conpassword = document.getElementById("conpassword");
let get_conpassword_func = document.getElementById("conpassword");
let get_nav = document.getElementsByClassName("navbar");
let statebar = document.getElementById("statusc");
let file_count = document.getElementById("val");

if (get_password){
    get_password.addEventListener("blur" , function(e){
    
        if(get_password.value.length < 8){
            Swal.fire({
                title: 'Error',
                text: 'your password lentgh is small',
                icon: 'error',
                confirmButtonText: 'OK'
            });
            get_password.value = ""
        }
    })
}

if (get_conpassword){
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
}

if (statebar){
    
    if (file_count.innerHTML < 8){
        statebar.innerHTML = "😴"
    }
    if (file_count.innerHTML >= 8){
        statebar.innerHTML = "🙂"
    }
    if (file_count.innerHTML >= 11){
        statebar.innerHTML = "😍"
    }
    if (file_count.innerHTML >= 25){
        statebar.innerHTML = "🤑"
    }
    if (file_count.innerHTML >= 35){
        statebar.innerHTML = "👑"
    }
}
