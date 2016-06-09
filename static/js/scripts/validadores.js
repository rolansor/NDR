
/*!
 * Validadores GG
 */


$('.validarCadenas').keyup(function () {
    this.value = this.value.replace(/[^A-Z a-z áéíóú]/g,'');
    });

$('.validarNumeros').keyup(function () {
    this.value = this.value.replace(/[^0-9]/g,'');
    });