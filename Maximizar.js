/*
En este código, la función maximizeNumber convierte el número en una cadena, luego lo divide en un array de caracteres, 
lo ordena en orden descendente y luego lo une nuevamente para formar el número máximo posible. 
Esto se logra al tener los dígitos más grandes en las posiciones más significativas.
*/
function maximizeNumber(num) {
    const numStr = num.toString();
    const numArray = numStr.split('');
    numArray.sort((a, b) => b - a);
    const maxNum = parseInt(numArray.join(''));
    return maxNum;
}

// Ejemplo de uso
const valor = 120;
const maximizedValue = maximizeNumber(valor);
console.log(`El número más grande posible al reorganizar los dígitos de ${valor} es ${maximizedValue}.`);