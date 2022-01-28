
el = document.getElementById('id_price');
el.addEventListener('change', ChangeValueProduct);
el = document.getElementById('id_discount');
el.addEventListener('change', ChangeValueProduct);

function ChangeValueProduct(){
    el_price = document.getElementById('id_price');
    el_discount = document.getElementById('id_discount');
    el_price_discount = document.getElementById('id_price_discount');
    if (el_price.value != 0) {
        el_price_discount.value = el_price.value * (1-el_discount.value/100)
    }



}