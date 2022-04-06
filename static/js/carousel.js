$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    items: 1,
    autoPlay: true,
    autoPlaySpeed: 1000,
    autoPlayTimeout: 300,
    animate: "fadeout",
    loop: true,
    margin: 10,
    singleItem: true,
    nav: false,
    dots: true,
  });
});
