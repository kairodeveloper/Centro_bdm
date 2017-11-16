$(document).ready(function(){
    $('.slider').slider();
    $('.button-collapse').sideNav({
        menuWidth: 600, // Default is 300
      edge: 'left', // Choose the horizontal origin
      draggable: true, // Choose whether you can drag to open on touch screens,
      closeOnClick: true,
    });
    $('.dropdown-button').dropdown();


});
