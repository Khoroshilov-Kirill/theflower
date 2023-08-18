function addHandlers(count) {
  var minus = count.querySelector(".minus");
  var number = count.querySelector(".number");
  var plus = count.querySelector(".plus");
  plus.addEventListener("click", function() {
    if (number.innerText > number.dataset.amount-1) {
        number.innerText = number.dataset.amount;
    } else {
    number.innerText++;
    }
 });
  minus.addEventListener("click", function() {
  if (number.innerText < 1) {
    number.innerText = 0;
    } else {
    number.innerText--;
    }
  });
}

var counts = document.querySelectorAll(".count");
counts.forEach(addHandlers);