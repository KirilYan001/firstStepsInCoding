let menu = document.querySelector('#menu-icon');
let navllist = document.querySelector('.namvlist');

menu.onclick = () =>{
    menu.classList.toggle('bx-x');
    navllist.classList.toggle('open')
}