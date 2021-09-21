$(document).ready(function(){
	$('.slider').slick({
		autoplay:true,
		autoplaySpeed: 5000,
		adaptiveHeight:true,
	});
});
$(document).ready(function(){
  $('.slider').hover(
    function(e) {
      $('.slick-next,.slick-prev').toggleClass('active__hover')
    }
  );
});
