$(function(){

  var toggleMenu = $('#togle-menu');
  var nav = $('#nav-menu');

  toggleMenu.on('click',function(){
    console.log('----');
    nav.removeClass('mov-header-menu-enabled').addClass('mov-header-menu');
  });

  nav.on('click',function(){
    console.log('*****');
    nav.removeClass('mov-header-menu').addClass('mov-header-menu-enabled');
  });
})
