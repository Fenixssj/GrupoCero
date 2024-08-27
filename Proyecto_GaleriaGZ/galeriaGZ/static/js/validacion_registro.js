$(document).ready(function () {
    // Formulario de registro de nuevo usuario:
    $("form.needs-validation").on("submit", function (event) {
      let isValid = true;

      // Nombre de usuario:
      let username = $("input[name='username']");
      let usernameValue = username.val().trim();
      if (!usernameValue) {
        username.next('.error-message').text("Por favor, ingrese un nombre de usuario");
        isValid = false;
      } else {
        username.next('.error-message').text("");
      }

      // Contraseña:
      let password = $("input[name='password']");
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

      // Confirmación de contraseña:
      let confirmPassword = $("input[name='confirm_password']");
      let confirmPasswordValue = confirmPassword.val();

      if (!confirmPasswordValue) {
        confirmPassword.next('.error-message').text("Por favor, ingrese nuevamente su contraseña");
        isValid = false;
      } else if (confirmPasswordValue !== passwordValue) {
        confirmPassword.next('.error-message').text("Las contraseñas no coinciden");
        isValid = false;
      } else {
        confirmPassword.next('.error-message').text("");
      }

      if (!isValid) {
        event.preventDefault();
      }
    });
});