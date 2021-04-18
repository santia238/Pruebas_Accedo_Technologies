document.getElementById('btn_register').addEventListener('click', function(e){
  let password_1 = document.getElementById("password").value;
  let password_2 = document.getElementById("password_confirm").value;
  if (password_1.length >= 8 && password_2.length >= 8) {
    if (password_1 != password_2) { 
      e.preventDefault();
      new bootstrap.Modal(document.getElementById('modal_error_passwords')).show()
    }
    else { 
      document.getElementById("form_register").submit()
    }
  }
});

document.getElementById('modal_error_passwords').addEventListener('hidden.bs.modal', function () {
  document.getElementById('password').focus()
})

document.getElementById('modal_error_register').addEventListener('hidden.bs.modal', function () {
  document.getElementById('email').focus()
})

