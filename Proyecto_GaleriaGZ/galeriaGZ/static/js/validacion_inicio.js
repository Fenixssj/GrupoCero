$(document).ready(function () {
    // Formulario de inicio de sesión
    $("form.needs-validation").on("submit", function (event) {
      let isValid = true;

      // Usuario:
      let username = $("input[type='text'][name='username']");
      let usernameValue = username.val();

      if (!usernameValue) {
        username.next('.error-message').text("Por favor, ingrese su usuario");
        isValid = false;
      } else {
        username.next('.error-message').text("");
      }

      // Contraseña:
      let password = $("input[type='password'][name='password']");
      let passwordValue = password.val();

      if (!passwordValue) {
        password.next('.error-message').text("Por favor, ingrese su contraseña");
        isValid = false;
      } else if (passwordValue.length < 6) {
        password.next('.error-message').text("La contraseña debe tener al menos 6 caracteres");
        isValid = false;
      } else {
        password.next('.error-message').text("");
      }

      if (!isValid) {
        event.preventDefault();
      }
    });
});